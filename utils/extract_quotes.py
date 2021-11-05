import os
import time
import argparse

from tqdm import tqdm
import pandas as pd
from multiprocesspandas import applyparallel
import numpy as np

# tqdm for pandas
tqdm.pandas()

# Config part
DATA_PATH = "data"
PKL_PATH = os.path.join(DATA_PATH, "pkl")
RESOURCES_PATH = os.path.join(DATA_PATH, "resources")


def get_pkl_year(year: int) -> list:
    """
    Returns a list of the pkl files present in `data/pkl/{year}`.
    """

    dirs = os.listdir(os.path.join(PKL_PATH, str(year)))

    return [os.path.join(str(year), dir) for dir in dirs]


def extract_subset(orig_df: pd.DataFrame, multiproc=False) -> pd.DataFrame:
    """
    This function extracts the quotes of speakers that are in the congress list.

    It returns the number of extracted quotes and the extracted dataframe.
    """

    if multiproc:
        orig_df["subset"] = orig_df["speaker"].parallel_apply(
            lambda x: pd.Series(x.lower()).isin(congress_members)
        )
    else:
        orig_df["subset"] = orig_df["speaker"].progress_apply(
            lambda x: pd.Series(x.lower()).isin(congress_members)
        )

    return orig_df["subset"].sum(), orig_df[orig_df["subset"] == True]


parser = argparse.ArgumentParser(
    description="Extract quotes from politicians from multiple pkl files"
)
parser.add_argument(
    "year", type=int, help="Name of the year folder from which to extract the pkl files"
)
parser.add_argument(
    "-m",
    type=bool,
    default=False,
    help="Use multiprocessing. Set to False if it fails",
)

args = parser.parse_args()

if __name__ == "__main__":
    # Get politicians list
    politicians_filepath = os.path.join(RESOURCES_PATH, "congress_biolist.json")
    politicians_df = pd.read_json(politicians_filepath).drop("congresses", axis=1)

    politicians_df["fullName"] = (
        politicians_df["givenName"] + " " + politicians_df["familyName"]
    )
    politicians_df["fullName"] = politicians_df["fullName"].str.lower()

    congress_members = politicians_df["fullName"].tolist()

    # The datasets were already loaded from the json.bz2 format and converted to .pkl in `data/pkl`

    year = args.year
    files = get_pkl_year(year)

    # Extract the quotes of interest of each chunk
    all_extracted = []
    for i, file in enumerate(files):
        try:
            df = pd.read_pickle(os.path.join(PKL_PATH, file))
        except FileNotFoundError:
            print(f"{file} not found, trying next file")
            continue

        t0 = time.time()
        _, subset_df = extract_subset(df, multiproc=args.m)
        all_extracted.append(subset_df)
        elapsed = time.time() - t0
        print(f"Done in {elapsed:.2f}s")

    # Merge them into a new df
    df_extracted = pd.concat(all_extracted)

    # Save the df as pkl
    pkl_name = f"extracted-quotes-{year}.pkl"
    df_extracted.to_pickle(os.path.join(PKL_PATH, pkl_name))

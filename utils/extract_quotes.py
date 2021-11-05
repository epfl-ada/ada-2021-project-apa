import os
import json
import time
import bz2

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


def extract_subset(orig_df: pd.DataFrame, multiproc=False) -> pd.DataFrame:
    """
    This function extracts the quotes of speakers that are in the congress list.

    It returns the number of extracted quotes and the extracted dataframe.
    """
    if multiproc:
        orig_df["subset"] = orig_df["speaker"].apply_parallel(
            lambda x: pd.Series(x).isin(congress_members)
        )
    else:
        orig_df["subset"] = orig_df["speaker"].progress_apply(
            lambda x: pd.Series(x).isin(congress_members)
        )

    return orig_df["subset"].sum(), orig_df[orig_df["subset"] == True]


if __name__ == "__main__":
    politicians_filepath = os.path.join(RESOURCES_PATH, "congress_biolist.json")
    politicians_df = pd.read_json(politicians_filepath).drop("congresses", axis=1)

    politicians_df["fullName"] = (
        politicians_df["givenName"] + " " + politicians_df["familyName"]
    )
    politicians_df["fullName"] = politicians_df["fullName"].str.lower()

    congress_members = politicians_df["fullName"].tolist()

    # The datasets were already loaded from the json.bz2 format and converted to .pkl in `data/pkl`

    # Get the names
    quotes_datasets = [
        os.path.join("data", "pkl", f"quotes-20{i:02d}.pkl") for i in range(8, 21)
    ]

    # For each dataset, extract the quotes from congress members
    # and save the extracted quotes as pkl for easier handling
    for i, dataset in enumerate(quotes_datasets, start=1):
        print(f"{i}/{len(quotes_datasets)} {dataset}:")
        try:
            complete_df = pd.read_pickle(os.path.join(DATA_PATH, dataset))
        except FileNotFoundError:
            print(f"{dataset} not found, trying next file")
            continue

        t0 = time.time()
        _, subset_df = extract_subset(complete_df)
        subset_df.to_pickle(os.path.join("data", "pkl", f"extracted_{dataset}"))
        elapsed = time.time() - t0
        print(f"Done in {elapsed:.2f}s")

"""
Very small utility script to convert a .json.bz2 archive into a .pkl file.

usage: load_df.py [-h] [-m M] file_name

Load .json.bz2 archive as .pkl.

positional arguments:
  file_name   (str) The filename of your archive. Should be located in `data/`.

optional arguments:
  -h, --help  show this help message and exit
  -m M        Choose mode. Either "pandas" or "bz2".

This is useful if you are memory-limited and need to spear every bit of RAM you can. This script allows, for example, not to have VScode running.
"""

import os
import bz2
import json
import argparse
import time

from tqdm import tqdm
import pandas as pd

DATA_PATH = "data"
PKL_PATH = os.path.join(DATA_PATH, "pkl")


def load_df(file_name: str, mode: str = "pandas", save: bool = True) -> pd.DataFrame:
    """
    Load a dataset in DataFrame from a .json.bz2 archive.

    file_name: str
        Name of .json.bz2 archive to load from `DATA_PATH`.

    mode: str = "pandas" | "bz2"
        Either use pandas read_json function or homemade bz2 function. This is usually faster (but makes my computer crash for some reason).

    save: bool
        Save the dataframe as a pickle file in `PKL_PATH`.
    """

    file_path = os.path.join(DATA_PATH, file_name)
    pkl_path = os.path.join(PKL_PATH, f"{file_name}.pkl")

    if mode == "bz2":
        keys = ["quoteID", "quotation", "speaker", "date", "numOccurrences", "phase"]

        with bz2.open(file_path, "rb") as quote_file:
            df = pd.DataFrame(
                [
                    dict(zip(keys, map(json.loads(instance).get, keys)))
                    for instance in tqdm(quote_file)
                ]
            )
    else:
        df = pd.read_json(file_path)

    if save:
        if !os.path.exists(pkl_path):
            file_name = file_name.strip(".json.bz2")
            df.to_pickle(os.path.join(PKL_PATH, pkl_path))

    return df


parser = argparse.ArgumentParser(description="Load .json.bz2 archive as .pkl")
parser.add_argument(
    "file_name",
    type=str,
    help="(str) The filename of your archive. Should be located in `data/`.",
)
parser.add_argument(
    "-m", default="pandas", help='Loading mode. Either "pandas" or "bz2".'
)
args = parser.parse_args()

if __name__ == "__main__":
    t0 = time.time()
    print("Converting", args.file_name)

    df = load_df(args.file_name, mode=args.m)

    elapsed = (time.time() - t0) / 60
    print(f"Done in {elapsed:.2f} min. {len(df)} line converted.")

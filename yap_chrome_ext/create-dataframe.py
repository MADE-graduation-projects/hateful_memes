"""Create dataframe from .txt files created by chrome extension"""


import os
import sys

from argparse import ArgumentParser

import numpy as np
import pandas as pd


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("data_dir", help="Path to dir containing .txt files")
    return parser.parse_args()


def get_files(data_dir):
    for (dirpath, dirnames, filenames) in os.walk(data_dir):
        return [os.path.join(data_dir, fn) for fn in filenames]


def main(args):
    files = get_files(args.data_dir)
    data = []

    for file in files:
        with open(os.path.join(args.data_dir, file), encoding="utf-8") as read:
            text = read.readline()
            rows = text.split('*')
            for row in rows:
                arr = row.split('|')
                if len(arr) == 2:
                    arr.append(file)
                    data.append(arr)
                    
    dataframe = pd.DataFrame(np.array(data), columns=['nick', 'image_url', 'topic'])
    dataframe.to_csv(path_or_buf=os.path.join(args.data_dir, 'images.csv'), index=False)


if __name__ == "__main__":
    args = parse_arguments()
    main(args)

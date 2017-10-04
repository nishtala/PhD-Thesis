#!/usr/bin/env python
import os
import sys
import fnmatch
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

globstring = '*.pd'
folder = '/home/nishtala/Dropbox/UPC/dropbox-thesis-directive/logs/'

def recursive_file_search(path, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

def process_df_monthly(filename):
    df = pd.read_pickle(filename)
    df.index = pd.DatetimeIndex(df.timestamp)
    del df['timestamp']
    df.columns = [os.path.splitext(os.path.basename(filename))[0]]
    print df
    return df.resample('D', 'last').fillna(method='ffill')

def download_history_for_files(folder, globstring):
    files = recursive_file_search(folder, globstring)

    for f in files:
        a = process_df_monthly(f)

def main():
    download_history_for_files(folder, globstring)



if __name__ == '__main__':
    main()

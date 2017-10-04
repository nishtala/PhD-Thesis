import os
from glob import glob
from dateutil.parser import parse
import pandas as pd
from subprocess import *
import fnmatch

def do_count(globstring):
    files = glob(globstring)
    results = []
    for f in files:
        try:
            res = check_output(['texcount','-brief','-total','-1','-sum',f]).rstrip('\n')
        except:
            continue#pass
        try:
            res = int(res)
        except:
            res = int(res.split('\n')[1])

        splitted = os.path.basename(f).split("_")
        datestr = splitted[0]
        timestr = splitted[1]
        timestr = timestr[:2] + ":" + timestr[2:4] + ":" + timestr[4:].split(".")[0]
        #results.append((datestr,res))
        dropboxpath = os.path.relpath(f, '/home/nishtala/Dropbox/UPC/dropbox-thesis-directive/logs/').replace("\\", "/")
        saveme =  dropboxpath.split("/")[0]
        results.append((saveme, parse(datestr + " " + timestr), res))

    return results


def do_all_counts(root):
    folders = [x[0] for x in os.walk("/home/nishtala/Dropbox/UPC/dropbox-thesis-directive/logs/")][1:]
    results = []
    for folder in folders:
        res = do_count(os.path.join(folder, '*.tex'))
        results.append(res)
    return results

def process_df_monthly(filename):
    df = pd.read_pickle(filename)
    df.index = pd.DatetimeIndex(df.timestamp)
    del df['timestamp']
    df.columns = [os.path.splitext(os.path.basename(filename))[0]]
    return df.resample('D', 'last').fillna(method='ffill')


def make_plot():
    res = period_of_int.plot(subplots=True, legend=False, grid=False, style=['r', 'g', 'b', 'y', 'k'])
    for ax in res:
        ax.yaxis.set_label_position('left')
        ax.yaxis.set_ticklabels([])
        ax.set_ylabel(ax.legendlabels[0], labelpad=20, rotation=0, horizontalalignment='right')
        ax.grid(axis='x', which='both')

def process(results):

    for i in range(len(results)):
        for j in range(len(results[i])):
            print results[i][0][0],
            print results[i][j][1], results[i][j][2]


def main():
    folder = "/home/nishtala/Dropbox/UPC/dropbox-thesis-directive/logs/"
    root = "/home/nishtala/Dropbox/"
    all_results = do_all_counts(root)

    process(sorted(all_results, key=lambda x: x[0]))



if __name__ == '__main__':
    main()

#!/usr/bin/env python

#http://www.tysto.com/uk-us-spelling-list.html
#uk-spell.csv -- uk spelling
#us-spell.csv -- us spelling
import os
import csv
import numpy
import argparse
import string
from argparse import PARSER
import re
import subprocess

def scandir(files_path):
    sfilelist = os.listdir(files_path)
    filelist = sanitize_filelist(sfilelist)
    return filelist

def sanitize_filelist(filelist):
    sanitized_filelist = []
    for file in range(len(filelist)):
        if filelist[file][-4:] == ".tex":
            sanitized_filelist += [filelist[file]]
    return sanitized_filelist

def parse_files(dataset_path):
    spell = []
    dataset = csv.reader(open(dataset_path, 'rb'), delimiter=' ')
    for line in dataset:
        spell.append(line[0])
    return spell

def spell_check(line, SPELLS, dataset_path):
    word1 = " ".join(re.findall("[a-zA-Z]+", line))
    word1 = word1.split(' ')
    for j in range(len(word1)):
        if word1[j] not in SPELLS:
            print "spell error:", dataset_path, word1[j]

def US_UK(line, US_SPELL, UK_SPELL, j, dataset_path):
    word1 = " ".join(re.findall("[a-zA-Z]+", line[j].lower()))
    word1 = word1.split(' ')
    for k in range(len(word1)):
        if word1[k] in US_SPELL:
            US_idx = US_SPELL.index(word1[k])
            if US_SPELL[US_idx] != UK_SPELL[US_idx]:
                print dataset_path, word1[k], US_SPELL[US_idx], UK_SPELL[US_idx]
        else:
            pass

    #if line[j].lower() in US_SPELL:
    #    US_idx = US_SPELL.index(line[j].lower())
    #    if US_SPELL[US_idx] != UK_SPELL[US_idx]:
    #        print dataset_path, line[j], US_SPELL[US_idx], UK_SPELL[US_idx]

def parse_and_check(dataset_path, US_SPELL, UK_SPELL, SPELLS, args):
    dataset = csv.reader(open(dataset_path, 'rb'), delimiter=' ')
    for line in dataset:
        for j in range(len(line)):
            if args.spell:
                spell_check(line[j].lower(), SPELLS, dataset_path)
            if args.us_uk:
                US_UK(line, US_SPELL, UK_SPELL, j, dataset_path)

def suggestions(output_path, tex_path):
    cmd = 'detex ' + tex_path + ' | diction -bs > ' + output_path
    os.system(cmd)

def main(args):
    input_files_path = str(args.input[0])
    all_folders = filter(lambda x: os.path.isdir(os.path.join(input_files_path, x)), os.listdir(input_files_path))
    output = '/home/nishtala/Dropbox/UPC/PhD-Thesis/suggestions/'
    #1-1 mapping
    UK_SPELL = parse_files('/home/nishtala/Dropbox/UPC/PhD-Thesis/us-uk-spell/' + 'uk-spell.csv')
    US_SPELL = parse_files('/home/nishtala/Dropbox/UPC/PhD-Thesis/us-uk-spell/' + 'us-spell.csv')
    SPELLS = parse_files('/home/nishtala/Dropbox/UPC/PhD-Thesis/us-uk-spell/' + 'words.txt')
    SPELLS = SPELLS + ['']
    for folder in all_folders:
        folder_path  = input_files_path + folder + "/"
        tex_files = scandir(folder_path)
        for texs in tex_files:
            if texs != 'glyphtounicode.tex':
                tex_path = folder_path + texs
                parse_and_check(tex_path, US_SPELL, UK_SPELL, SPELLS, args)
                if args.detex:
                    suggestions(output+texs, tex_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', nargs=1, help='input path')
    parser.add_argument('--spell', action='store_true', default=False, help='spell check')
    parser.add_argument('--us_uk', action='store_true', default=False, help='us_uk')
    parser.add_argument('--detex', action='store_true', default=False, help='for word suggestions')
    args = parser.parse_args()
    main(args)

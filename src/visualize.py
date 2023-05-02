#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)
#    print("counts=", counts)
    
# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

keys = []
values = []
for k,v in items[:10]:
    keys = keys + [k]
    values = values + [v]
plt.xticks(range(len(keys)), keys)
plt.bar(range(len(keys)), values)

if 'lang' in str(args.input_path):
    plt.title('Spread of Coronavirus in Through Language in Twitter')
    plt.xlabel('languange')
    plt.ylabel('count')
    plt.legend()
    plt.savefig(f'{args.key} + _country.png')

if "country" in str(args.input_path):
    plt.title('Spread of Coronavirus in countries in Twitter')
    plt.xlabel('countries')
    plt.ylabel('count')
    plt.legend()
    plt.savefig(f'{args.key} + _country.png')

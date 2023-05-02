#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_hashtags', nargs='+', required=True)
args = parser.parse_args()

# imports
import os
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt 
import json
from collections import Counter,defaultdict

total = {}

for hashtag in args.input_hashtags:
    day_totals = {}
# loop over each day
    for day in sorted(os.listdir('outputs')):
        output_file = os.path.join('outputs', day)
        date = output_file[18:26]
# generate count  
        if os.path.isfile(output_file):
            if 'lang' in output_file:
                count = 0
                with open(output_file) as f:
                    text = json.load(f)
                    for k in text:
                        if k == hashtag:
                            for key in text[k]:
                                count += text[k][key]
                day_totals[date] = count
    total[hashtag] = day_totals
plt.figure(figsize=(12,10))
dates = []
for hashtag, day_total in total.items():
    x_axis = []
    y_axis = []
    for x, y in day_total.items():
        x_axis = x_axis + [x]
        y_axis = y_axis + [y]
        dates = dates + [x]
    plt.plot(range(len(x_axis)), y_axis)
plt.title('Count of hashtags through 2020')
plt.legend()
plt.ylabel('tweet count')
plt.xlabel("day of the year") 

plt.savefig(f'{args.input_hashtags}_.png')

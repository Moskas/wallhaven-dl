#!/bin/python
import argparse
#import sys
import os
from wallhaven.api import Wallhaven

parent_dir = "path were you want to download wallpapers" # ex /home/user/downloads/

wallhaven = Wallhaven(api_key="your api key here") # comment out if you want to use it without api key
parser = argparse.ArgumentParser()
parser.add_argument('-q', help='query', type=str)
parser.add_argument('-c', help='categories 000')
parser.add_argument('-p', help='purity 000')
parser.add_argument('-s', help="sorting date_added*, relevance, random, views, favorites, toplist")
#parser.add_argument('-u', help="print out urls")
parser.add_argument('-r', help="set resolution ex: 1920x1080")
parser.add_argument('-R', help="set ratio ex: 16:9 or 9:16")
args = parser.parse_args()

wallhaven.params["q"] = args.q
if args.q != None:
    path = os.path.join(parent_dir, args.q)
    try:
        os.mkdir(path)
    except OSError as error:
        print("Using existing directory")
else:
    path = parent_dir

if args.c!=None:
    wallhaven.params["categories"] = args.c
else:
    wallhaven.params["categories"] = "110"
if args.s!=None:
    wallhaven.params["sorting"] = args.s
else:
    wallhaven.params["sorting"] = "date_added"

if args.p!=None:
    wallhaven.params["purity"] = args.p
else:
    wallhaven.params["purity"] = '100'

if args.R!=None:
    wallhaven.params["ratios"] = args.R
else:
    wallhaven.params["ratios"] = "16x9"

results = wallhaven.search()
for wallpaper in results.data:
    wallpaper.save(path)

"""You're working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews. 
Your manager asks you to take those reviews (saved as .txt files) and display them on your company's website. To do this, you'll need to write a 
script to convert those .txt files and process them into Python dictionaries, then upload the data onto your company's website (currently using Django)."""

#!/usr/bin/env python3
import os
import requests

# set source dir for feedback file:
src_dir = "/data/feedback/"

# capture list of files:
files = os.listdir(src_dir)

# function to read file lines into list:
def readlines(file):
    with open(src_dir + file) as f:
        lines = f.read().splitlines()
    return lines


# load feedback entries into dictionary:
feedback = []
keys = ["title", "name", "date", "feedback"]
for file in files:
    lines = readlines(file)
    feedback.append(dict(zip(keys, lines)))

# set host url:
url = "http://localhost/feedback/"

# post feedback entries:
for entry in feedback:
    response = requests.post(url, data=entry)
    if response.ok:
        print("loaded entry")
    else:
        print(f"load entry error: {response.status_code}")



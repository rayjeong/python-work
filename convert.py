#! /usr/bin/env python3

import os
import requests
import json


dict = {}
my_dict = { 'title':[], 'name':[], 'date':[], 'feedback':[]} 
fields =['title', 'name', 'date', 'feedback']
id = 1


path = "/data/feedback"
API_ENDPOINT = "http://10.10.10.10/feedback/?format=api"

dirlist = os.listdir( path ) 
#print(dirlist)
os.chdir(path)

filename = "feed.txt"

for filename in dirlist:
  my_dict = { 'title':[], 'name':[], 'date':[], 'feedback':[]} 
  with open(filename) as fh:
      
    i = 0

    for line in fh:
          
        description = line.strip()
        # for output see below
        print(description) 
      
        if i<len(fields): 
          my_dict[fields[i]].append(description)
          i = i + 1
                  
    dict[response] = my_dict
    print(my_dict)

    r = requests.post(url = API_ENDPOINT, data = my_dict)
  
  
# creating json file        
#out_file = open("test2.json", "w")
#json.dump(dict1, out_file, indent = 4)
#out_file.close()


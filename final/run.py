#! /usr/bin/env python3

import os
import requests
import json

dict = {}
my_dict = { 'name':[], 'weight':[], 'description':[], 'image_name':[]} 
fields =['name', 'weight', 'description', 'image_name']
id = 1


path = "supplier-data/descriptions/"
new = "new/"
weight = 0
API_ENDPOINT = "http://localhost/fruits/?format=api"

dirlist = os.listdir( path ) 
#print(dirlist)
os.chdir(path)

#filename = "test.txt"

for filename in dirlist:
    with open(filename) as fh:
        i = 0
        for line in fh:
            description = line.strip()
            print (description)
      
            if i<len(fields): 
                if i == 1:
                   weight=int(description.strip('lbs'))
                   description = weight
                my_dict[fields[i]] = description
                i = i + 1

                if i == 3:
                   description = filename.strip('.txt') + ".jpg"
                   my_dict[fields[i]] = description
                  
    print(my_dict)

    r = requests.post(url = API_ENDPOINT, data = my_dict)
  


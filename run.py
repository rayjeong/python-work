#! /usr/bin/env python3

import os
#import requests
import json

path = "/data/feedback"
dirlist = os.listdir( "." ) 

print(dirlist)

filename = "feed.txt"

# resultant dictionary
dict = {}
my_dict = { 'title':[], 'name':[], 'date':[], 'feedback':[]} 
  
# fields in the sample file 
fields =['title', 'name', 'date', 'feedback']
  
fileno = 0

response="response" + str(fileno)
with open(filename) as fh:
      
    fileno = fileno + 1
    i = 0
    # for automatic creation of id for each employee
    response_no ='response1'
    for line in fh:
          
        description = line.strip()
          
        # for output see below
        print(description) 
      
        if i<len(fields): 
          my_dict[fields[i]].append(description)
          i = i + 1
                  
        # appending the record of each employee to
        # the main dictionary


#print(my_dict)
dict[response] = my_dict
#dict["response1"] = my_dict
print(dict)


  
  
# creating json file        
#out_file = open("test2.json", "w")
#json.dump(dict1, out_file, indent = 4)
#out_file.close()


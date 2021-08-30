#!/usr/bin/env python3

import sys
import os
import reports
from datetime import date
import emails


dict = {}
today = str(date.today())
path = "supplier-data/descriptions/"
weight = 0

#print(dirlist)


def get_data(fname):
    my_dict = { 'name':[], 'weight':[]} 
    fields =['name', 'weight']
    
    with open(fname) as fh:
        i = 0
        for line in fh:
           description = line.strip()
#          print (description)
     
           if i<len(fields): 
               my_dict[fields[i]] = description
               i = i + 1
                  
        return(my_dict)



def main(argv):
  title = "Processed Update on " + today 
  print (title)
  data = {}
  table_data = []
  i = 0
  body = ""
  summary = []
  all_summary = []
  string = ""

  dirlist = os.listdir( path ) 
  os.chdir(path)



  for filename in dirlist:
#      print(filename)
      data = get_data(filename)
#      print (data)
    
      summary = [
         "name: {}".format(data['name']),
         "weight: {}".format(data['weight']),
	 ""] 
      all_summary.append(summary)
#  print(all_summary)


  for each in all_summary:
#     print(each, sep=',')
     for entry in each:
#         print(entry)
          body = body + "\n" + entry  
  print(body)
    

  reports.generate("/tmp/processed.pdf", title, body)

  sender = "automation@example.com"
  receiver = ""
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attach = "/tmp/processed.pdf"

  message = emails.generate(sender, receiver, subject, body, attach)
  emails.send(message)

if __name__ == "__main__":
    main(sys.argv)


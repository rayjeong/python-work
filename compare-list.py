#!/usr/bin/env python3

import sys
inputfile1 = sys.argv[1]
inputfile2 = sys.argv[2]

list1=[]
list2=[]
new_string = ""
count = 0

with open(inputfile1, 'r') as file1:
	list1 = file1.readlines()
#	print(list1)
file1.closed

with open(inputfile2, 'r') as file2:
	list2 = file2.readlines()
#	print(list2)
file2.closed

set1 = set(list1)
set2 = set(list2)

# Elements in list1 but not in list2
only_in_list1 = set1 - set2
# Elements in list2 but not in list1
only_in_list2 = set2 - set1

# Convert sets back to lists for printing
only_in_list1 = list(only_in_list1)
only_in_list2 = list(only_in_list2)

# Print results
#print("Elements in list1 but not in list2:")
print("not in UNIXINV")
for item in only_in_list1:
   print(item)

#print("\nElements in list2 but not in list1:")
print("not in GCP")
for item in only_in_list2:
   print(item)

#if __name__ == "__main__":
    #print("System Uptime:", formatted_uptime)

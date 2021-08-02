import json
  
  
# the file to be converted
filename = 'data.txt'
  
# resultant dictionary
dict1 = {}
  
# fields in the sample file 
fields =['name', 'designation', 'age', 'salary']
  
with open(filename) as fh:
      
  
      
    # count variable for employee id creation
    l = 1
      
    for line in fh:
          
        # reading line by line from the text file
        description = list( line.strip().split(None, 4))
          
        # for output see below
        print(description) 
          
        # for automatic creation of id for each employee
        sno ='emp'+str(l)
      
        # loop variable
        i = 0
        # intermediate dictionary
        dict2 = {}
        while i<len(fields):
              
                # creating dictionary for each employee
                dict2[fields[i]]= description[i]
                i = i + 1
                  
        # appending the record of each employee to
        # the main dictionary
        dict1[sno]= dict2
        l = l + 1

    print(dict1)
  
  
# creating json file        
out_file = open("test2.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()


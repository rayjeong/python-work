#def  chunk_it( input )

#read in data

#save string
#is it 5 
# read another
# add to string
#else
# write output
#
#keep going until eof 

import sys
inputfile = sys.argv[1]
outputfile = inputfile + ".out"

new_string = ""
count = 0
with open(inputfile) as f:
  with open(outputfile,'w+') as out:
    for line in f:
        while count < 5:
          if count == 0:
            new_string += line[:-1]
          else:
            new_string += ":" + line[:-1]
          count += 1
        #print (new_string)
        out.write(new_string + "\n") 
        count = 0
        new_string = ""
    #print (new_string)
    out.write(new_string + "\n") 
  out.closed
f.closed

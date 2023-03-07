#!/usr/bin/env python3

import sys
inputfile = sys.argv[1]
outputfile = inputfile + ".out"

new_string = ""
count = 0
with open(inputfile) as f:
  with open(outputfile,'w+') as out:
    for line in f:
          if count == 0:
            new_string += line[:-1]
            count += 1
          else:
            if count < 10:
              new_string += ":" + line[:-1]
              count += 1
          if count == 10:
            #print (new_string)
            out.write(new_string + "\n")
            count = 0
            new_string = ""
    #print (new_string)
    out.write(new_string + "\n")
  out.closed
f.closed

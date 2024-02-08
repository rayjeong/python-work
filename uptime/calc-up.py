#!/usr/bin/env python3

import sys
inputfile = sys.argv[1]
outputfile = inputfile + ".out"

new_string = ""
count = 0
with open(inputfile, 'r') as file:
          for line in file:
            #uptime_seconds = float(f.readline().split()[0])
            #hostname = line.split()[0]
            #hostname = line.split(" ", 0)
            uptime_days = line.split()
            if int(uptime_days[9]) >= 120:
              print (uptime_days[0],uptime_days[9])
file.closed





#if __name__ == "__main__":
    #print("System Uptime:", formatted_uptime)

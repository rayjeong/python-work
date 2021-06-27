#!/usr/bin/env python

from multiprocessing import Pool
import os
import subprocess

src = "../data/prod/"
dest = "../../data/prod_backup/"

filelist = []

def run(filelist):
  # Do something with task here
  #  print("Handling {}".format(task))
    subprocess.call(["rsync", "-arq", filelist, dest])
    #print (filelist, dest)

if __name__ == "__main__":
  os.chdir(src)

  for root, dirs, files in os.walk(".", topdown=True):
    for name in dirs:
      #print(os.path.join(root, name))
      filelist.append(os.path.join(root, name))
    for name in files:
      #print(os.path.join(root, name))
      filelist.append(os.path.join(root, name))


  # Create a pool of specific number of CPUs
  p = Pool(len(filelist))
  # Start each task within the pool	
  p.map(run, filelist)

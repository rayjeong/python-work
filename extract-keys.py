#!/usr/bin/env python
import subprocess
import sys
def parse_pubkey(pubfile):
    """Return the key-type and key from a public-key file.
    """
    try:
        keystr = subprocess.check_output(
            'ssh-keygen -i -f %s 2>/dev/null' % pubfile,
            shell=True)
    except subprocess.CalledProcessError:
          with open(pubfilename) as f:
            Lines = f.readlines()
            for keystr in Lines:
              #keystr = f.read()
              key1 = keystr.split()[0:2]
              keyname = keystr.split()[2]
              print ( key1)
              print ( keyname)
              with open (keyname, "w") as outfile:
                outfile.write( keystr )
              outfile.close()
    return
if __name__ == '__main__':
    pubfilename = sys.argv[1]
    print parse_pubkey(pubfilename)

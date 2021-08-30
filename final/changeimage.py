#!/usr/bin/env python3

import os
import sys
from PIL import Image


path = 'supplier-data/images'

for file in os.listdir(path):
    current = os.path.join(path, file)
    print (current)
    if current.endswith((".tiff")):
        target = os.path.splitext(current)[0] + ".jpeg"
        print (target)
        if os.path.isfile(current):
            im = Image.open(current)
            im.convert('RGB').resize((600,400)).save(target)




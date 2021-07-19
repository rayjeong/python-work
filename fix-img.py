#!/usr/bin/env python3

import os
import sys
from PIL import Image


path = '.'

for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current):
        im = Image.open(current)
        im.convert('RGB').rotate(90).resize((128,128)).save("/opt/icons/" + current)


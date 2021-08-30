#!/usr/bin/env python3

import os
import requests
from PIL import Image

path = 'supplier-data/images/'
url = "http://localhost/upload/"


for file in os.listdir(path):
    current = os.path.join(path, file)
    #print (current)
    if current.endswith((".jpeg")):
        with open(current, 'rb') as opened:
            r = requests.post(url, files={'file': opened})



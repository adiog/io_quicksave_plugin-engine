#!/usr/bin/python

import PIL
from PIL import Image

def capture_crop(output_file, output_crop_file):
    basewidth = 320
    baseheight = 240
    img = Image.open(output_file)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS).crop((0,0,basewidth,baseheight))
    img.save(output_crop_file)


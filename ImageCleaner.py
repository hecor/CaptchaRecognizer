#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from operator import itemgetter
import sys

def get_top_colors(im):
    his = im.histogram()
    values = {}
    for i in range(256):
        values[i] = his[i]
    top_colors = []
    for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:2]:
        top_colors.append(j)
    return top_colors

def clear_isolated_points(im):
    im2 = Image.new("P", im.size, 255)

    for x in range(1, im2.size[1]-1):
        for y in range(1, im2.size[0]-1):
            pix = im.getpixel((y,x))
            pix1 = im.getpixel((y-1,x))
            pix2 = im.getpixel((y+1,x))
            pix3 = im.getpixel((y,x-1))
            pix4 = im.getpixel((y,x+1))
#            print pix1, pix2, pix3, pix4
            if pix == 0 and ((pix1 == 0 and pix2 == 0) or (pix3 == 0 and pix4 == 0)):
                im2.putpixel((y,x), 0)

    return im2

def get_clean_image(im):
    top_colors = get_top_colors(im)
    im2 = Image.new("P", im.size, 0)

    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y,x))
            if pix in top_colors:
                im2.putpixel((y,x),255)

    im2 = clear_isolated_points(im2)
    im2 = clear_isolated_points(im2)
    return im2

def split_image(im2):
    start = 5
    interval = 15
    height = 22
    ims = []
    for i in range(4):
      im3 = im2.crop((start+i*interval , 0, start+(i+1)*interval, height))
      ims.append(im3)
    return ims


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'usage: ./clearImage.py imageName'
        sys.exit(-1)

    im = Image.open(sys.argv[1])
    im = im.convert("P")

    im2 = get_clean_image(im)
    ims = split_image(im2)
    os.chdir('./testcase')
    ims[0].save(testcases[i][0] + "_" + str(i) + '.gif')
    ims[1].save(testcases[i][1] + "_" + str(i) + '.gif')
    ims[2].save(testcases[i][2] + "_" + str(i) + '.gif')
    ims[3].save(testcases[i][3] + "_" + str(i) + '.gif')




#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image
from clearImage import *

trainingsets = [ 'xr7j', 'v6ke', '7fht', '1s78', '6uq5', 'apjy', 'gt49', 'ylm9', '959e', '3x18', 
                 'nutv', 'ohqm', 'qrxf', '5vgb', 'qzcp', 'se53', 'gwa2', 'dm9y', 'om3z', 'xjdq',
                 'swb1', 'w17p', 'zpuu', 'mr5o', 'ccq7', 'iifz', 'um33', 'urba', 't1t6', 'h6jz',
                 '4wjy', 'bhp4', '2htr', 'am5s', '5apt', 'w5ig', 'hpzj', '2hn3', 'vyki', 'hxbv',
                 '85g9', 'oyb7', 'gd38', '5y6e', 'r132', 'kovy', '33wx', 'ab5o', 'p9s1', 'kwyu',
                 'b9cq', 'fp15', 'f1zh', 'vd4n', '2xzw', '3n4n', 'qz3x', '76wj', 'eiff', 'gg93',
                 'cucy', '7ox5', '1gkd', 'ce6t', '7a57', 'lfde', 'g9ea', 'zs41', 'bg4v', '3crt',
                 'q4i8', 'n4nw', '1h7e', 'uzzf', '99ny', 'd5vi', 'f46a', 's8h2', 'dz7f', 'qb3y',
                 'vr6d', 'j1om', '9vw3', '7ssz', 'nc3m', 'g4bv', 'qgtt', 'x15e', '5mpk', 'zkg8',
                 'v29b', 'p1vf', 'hak2', 'cdig', '861i', 'dpur', 'ec92', 'veg5', 'weav', 'jnsh',]

os.chdir('./testcase/trainingsets')
for i in range(0, 100):
    im = Image.open('training%i.jpg' % i)
    im = im.convert("P")
    im2 = get_clean_image(im)
    ims = split_image(im2)

    # save the images
    ims[0].save('../icons/' + testcases[i][0].lower() + "_" + str(i) + '.gif')
    ims[1].save('../icons/' + testcases[i][1].lower()  + "_" + str(i) + '.gif')
    ims[2].save('../icons/' + testcases[i][2].lower()  + "_" + str(i) + '.gif')
    ims[3].save('../icons/' + testcases[i][3].lower()  + "_" + str(i) + '.gif')
    


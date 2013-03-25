#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image
import math
from ImageCleaner import *

class CaptchaRecognizer:
    def __init__(self, trainingicons_dirpath):
        self.trainingset = {}
        self.load_trainingset(trainingicons_dirpath)

    def magnitude(self, concordance):
        total = 0
        for word,count in concordance.iteritems():
            total += count ** 2
        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.iteritems():
            if concordance2.has_key(word):
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

    def buildvector(self, im):
        d1 = {}
        count = 0
        for i in im.getdata():
            d1[count] = i
            count += 1
        return d1

    def load_trainingset(self, dirpath):
        iconset =  ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for s in iconset:
            self.trainingset[s] = []
        for imageName in os.listdir(dirpath):
            if imageName[-3:] == "gif":
                self.trainingset[imageName[0]].append(self.buildvector(Image.open(os.path.join(dirpath, imageName))))

    def recognize_char(self, im):
        guess = []
        imv = self.buildvector(im)
        for c in self.trainingset.keys():
            vs = self.trainingset[c]
            for v in vs:
                guess.append( (self.relation(v, imv), c) )
        guess.sort(reverse=True)
        return guess[0][1]

    def recognize_captcha(self, imageName):
        im = Image.open(imageName)
        im = im.convert("P")
        im = get_clean_image(im)
        ims = split_image(im)
        recognized_chars = []
        
        for im in ims:
            recognized_chars.append(self.recognize_char(im))
        return ''.join(recognized_chars)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print 'usage: ./*** filename'
        sys.exit(-1)

    cr = CaptchaRecognizer('./testcase/icons')
    print cr.recognize_captcha(sys.argv[1])


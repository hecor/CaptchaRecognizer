#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CaptchaRecognizer import *
from datetime import datetime

print str(datetime.now())

testsets = ['vtsu', 's7xc', 'hinc', '96sc', 'gcuu', '9sfx', 'wgl2', 'qmw1', 'qwon', 'kur5',
            'q3hz', '81u6', 't1tj', '7sdx', 'pxt9', '54uy', 'oyry', 'p6qc', 'r7b2', '7nah',
            'y24u', '9acp', '5hsb', 'rswo', '1x52', 'a73g', 'pya6', 's5fb', '915o', '6xyt',
            '68gm', '1v36', 'qerv', 'duvx', 'mesd', 'kq9b', 't8q6', 'qne1', 'zqav', 'rypq',
            'u5jy', 'quf1', 'p5ay', '7nz7', 'gnu8', 'b4w9', 'n87n', 'r7mx', 'ltfo', 'k8ih',
            '3crk', 'c28y', 'hy7n', 'w24b', 'ea1x', '1vec', '6dmk', 'vgvq', 'nxbw', 'qb2q',
            'r6vz', 'ppak', 'tgn7', 'vp5b', '4f99', 'jz3x', 'fdw1', 'x6xr', 'yn4v', '6ce5',
            '2rsv', '7evt', 'fe8w', 'g3zq', 'mtsj', 'ozlr', '5mrc', 'e5x6', 'bjwf', 'u2g7',
            'qn6q', 'ramz', 'z4qd', 'jcgw', 'pk89', 'ft2x', '3jap', 'eab7', 'chm8', 'x8z3',
            'qipi', 'bjyp', 'd441', 'sypb', 'x7pv', '8w1g', 'jv16', 'dcy9', 's48v', '5psb',]

total = 100.0
correct = 0

cr = CaptchaRecognizer('./testcase/icons')
for i in range(0, 100):
    if cr.recognize_captcha('./testcase/testsets/test%i.jpg'%i) == testsets[i]:
        correct += 1

print 'correct:', correct
print 'precision:', correct/total
print str(datetime.now())



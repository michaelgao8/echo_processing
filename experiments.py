# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:56:14 2018

@author: micha
"""

import mudicom

test = mudicom.load("USm.1.2.840.113654.431393207.102105248952208360607505294111270764638.dcm")

img = test.image
img = test.image.numpy
#
#test_image2 = img.numpy
#image_list = []
#
#for i in range(3*320*240, *320*240):
#    image_list.append(test_image2[i*3])
#    
#test_image3 = np.asarray(image_list)
#test_image3.shape = (320, 240)

import numpy as np
import matplotlib
import itertools
dim_list = [3, 320, 240, 10]
itertools.permutations(dim_list)

for i in itertools.permutations(dim_list):
    
    img.shape = i
    frame_dim = np.where(np.isin(img.shape, 10) == True)[0][0]
    print(frame_dim)
    
    slicer = [":", ":", ":", ":"]
    slicer[frame_dim] = "0"
    slice_call = "[" +  ",".join(slicer) + "]"
    print(slice_call)
    
    print_img = eval("img"+slice_call)
    print(print_img.shape)
    # Put into 320 x 240 x 3
    threetwenty = np.where(np.isin(print_img.shape, 320))[0][0]
    twoforty = np.where(np.isin(print_img.shape, 240))[0][0]
    three = np.where(np.isin(print_img.shape, 3))[0][0]
    
    print_img = print_img.transpose(twoforty, threetwenty, three)
    
    matplotlib.pyplot.imshow(print_img)

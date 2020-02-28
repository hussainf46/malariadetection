# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:09:17 2019

@author: Dell
"""

import cv2,os
import numpy as np 
import csv 
import glob
from skimage import color 
 
label = "Parasitized"
dirlist=glob.glob("cell_images/"+label+"/*.png")
file = open("csv/datasets.csv","a")


def rgb2gray(rgb):
	return np.dot(rgb[...,:3], [0.299,0.587,0.144])

j=0
for img_path in dirlist[0:5]:
	im = cv2.imread(img_path,0)
	im = cv2.GaussianBlur(im,(5,5),2)
	#im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	
	ret,thresh = cv2.threshold(im,127,255,0)
	#print(ret)
	#if j < 2:
	#	print(thresh)
	contours,hierarchy =  cv2.findContours(thresh,1,2)
	
	file.write(label)
	file.write(",")
	#print(contours[1])
	for i in range(5):
		try:
			#cnt = contours[i]
			area = cv2.contourArea(contours[i])
			print(area)
			file.write(str(area))
		except:
			file.write("0")
		#file.write(",")
		
	file.write("\n")
			
			    
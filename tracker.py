#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:20:05 2018

@author: hanning
"""

import colotracker
import cv2
cv2.namedWindow("tracking")
camera = cv2.VideoCapture("/home/hanning/workstation/workstation/Video/People.avi")
init_once = False
my_tracker = colotracker.ColorTracker()

ok, image=camera.read()
if not ok:
    print('Failed to read video')
    exit()

bbox1 = cv2.selectROI('tracking', image,0,0)

while camera.isOpened():
    ok, image=camera.read()
    if not ok:
        print 'no image to read'
        break
    Mat = colotracker.Mat.from_array(image)
    if not init_once:
        my_tracker.init(colotracker.Mat.from_array(image), int(bbox1[0]),int(bbox1[1]),int(bbox1[0]+bbox1[2]),int(bbox1[1]+bbox1[3]))
        init_once = True
    my_tracker.track(colotracker.Mat.from_array(image))
    bbox = my_tracker.getinfo()
    bbox = bbox.split(',')
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0]) +int( bbox[2]), int(bbox[1]) +int(bbox[3]))
    cv2.rectangle(image, p1,p2, (200,0,0))

    cv2.imshow('tracking', image)
    k = cv2.waitKey(1)
    if k == 27 : break 
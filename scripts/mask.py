#!/usr/bin/python
# coding: utf-8

import cv2 
import time
import numpy as np
import RPi.GPIO as gpio



# Minimum area to detect
minArea = 40


cv2.namedWindow("Normal")
cv2.namedWindow("HSV")
cv2.namedWindow("Mask")
cv2.namedWindow("Erode")


cap = cv2.VideoCapture(0)

width = 320
height = 240

if cap.isOpened():
  cap.set(3, width)
  cap.set(4, height)

  
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,(90,50,20),(123,255,255))
    erode = cv2.erode(mask, None, iterations = 3)
    moments = cv2.moments(erode,True)
    if moments['m00'] >= minArea:
       x = moments['m10'] / moments['m00']
       y = moments['m01'] / moments['m00']
       print(x, ", ", y)
       cv2.circle(frame, (int(x), int(y)), 5, (0, 255,0), -1)

    cv2.imshow("Normal",frame)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Mask", mask)
    cv2.imshow("Erode", erode)


    
	
	
    if cv2.waitKey(10) == 27:
        break
cv.destroyAllWindows()


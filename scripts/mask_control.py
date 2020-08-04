#!/usr/bin/python
# coding: utf-8

import cv2 
import time
from gpiozero import PWMLED, LED

lb1 = LED(17, initial_value=True)
lb2 = LED(27, initial_value=True)
lf1 = LED(22, initial_value=True)
lf2 = LED(23, initial_value=True)
rf1 = LED(9, initial_value=True)
rf2 = LED(10, initial_value=True)
rb1 = LED(24, initial_value=True)
rb2 = LED(25, initial_value=True)

speed = PWMLED(11)
speed.value = 0.16

def forward():
  lf1.off()
  rf1.off()
  rf2.off()
  lf2.off()

def backward():
  lb1.off()
  lb2.off()
  rb1.off()
  rb2.off()

def left():
  rf1.off()
  rf2.off()

def right():
  lf1.off()
  lf2.off()

def stop():
  lf1.on()
  lf2.on()
  rf1.on()
  rf2.on()
  lb1.on()
  lb2.on()
  rb1.on()
  rb2.on()
  
def zArea(area):
  if (area<=120):
    forward()
  elif (area>=600):
    backward()
  else:
    stop()

# Minimum area to detect
minArea = 60
cap = cv2.VideoCapture(0)

width = 160
height = 120

if cap.isOpened():
  print("test")
  cap.set(3, width)
  cap.set(4, height)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,(90,50,20),(123,255,255))
    erode = cv2.erode(mask, None, iterations = 3)
    moments = cv2.moments(erode,True)
    print(moments)
    if moments['m00'] >= minArea:
       print(moments['m00'])
       zArea(moments['m00'])
    else:
       stop()
    #cv2.imshow("Normal",frame)
    #cv2.imshow("HSV", hsv)
    #cv2.imshow("Mask", mask)
    #cv2.imshow("Erode", erode)

    if cv2.waitKey(10) == 27:
        break
cv.destroyAllWindows()


# trashket-robot/scripts/circle.py
# by Luke Smalley

from gpiozero import PWMLED
from time import sleep

left = PWMLED(17)
right = PWMLED(22)

try:
  left.value = 0.1
  while True:
    right.value = 0.1
    sleep(2)
    right.value = 0
    sleep(2)
except: # Ctrl-C is used to interrupt the loop and end the program.
  left.value = 0
  right.value = 0

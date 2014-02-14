# polygon.py
# - Draw a polygon with the number of sides specified by an argument
import sys

from turtle import *

try:
	sides = int(sys.argv[1])
except:
	sides = 4

def polygon(sides,step):
    for i in range(sides):
     forward(step)
     right(360/sides)

polygon(sides,50)


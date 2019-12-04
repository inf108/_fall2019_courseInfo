from graphics import *
import random

def rand255():
  return 

def randomColor():
  return (color_rgb(rand255(), rand255(), rand255()))


def createGround(win, x, y, height):
  groundColor = randomColor()
  ground = Rectangle(Point(0, y*height), Point(x, y))
  ground.setFill(groundColor)
  ground.setOutline(groundColor)
  ground.draw(win)

  return [ground]


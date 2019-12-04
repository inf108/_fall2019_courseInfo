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

def createHills(win, winX, winY, height):
  x = 0
  hills = []
  hills.append(Point(0, winY))
  while (x < winX):
    hills.append(Point(x, random.randint(int(height*winY), winY)))
    x += random.randint(int(winX*0.05), int(winX*0.3))
  hills.append(Point(winX, winY))

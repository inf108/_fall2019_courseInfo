from graphics import *
import random

def rand255():
  return random.randint(0, 255)

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

  hill = Polygon(hills)
  hillColor = randomColor()
  hill.setOutline(hillColor)
  hill.setFill(hillColor)
  hill.draw(win)

  return [hill]

def createStars(win, winX, winY, number):
  stars = []
  for i in range(number):
    stars.append(Point(random.randint(0, winX), random.randint(0, winY)))
    stars[i].setOutline(color_rgb(random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)))
    stars[i].draw(win)
  return stars

def createSky(win, winX, winY):
  color = color_rgb(random.randint(0, 10), random.randint(0, 10), random.randint(20, 50))
  sky = Rectangle(Point(0,0), Point(winX, winY))
  sky.setFill(color)
  sky.draw(win)
  return sky

def createLandscape(win, x, y):
  sky = createSky(win, x, y)
  stars = createStars(win, x, y, 100)
  hills = createHills(win, x, y, 0.6)
  ground = createGround(win, x, y, 0.8)

  

'''
win = GraphWin("Landscape", 640, 480)
createLandscape(win, 640, 480)
win.getMouse() # Pause to view result
win.close()    # Close window when done
'''

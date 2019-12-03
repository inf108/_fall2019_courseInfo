from graphics import *
from tardis import *

def createCircle(win, x, y, size, color):
  c = Circle(Point(x,y), size)
  c.setFill(color)
  c.draw(win)
  return c



def createRectangle(win, x, y, size, width, height, color):
  r = Rectangle(Point(x, y), Point(x + size*width, y + size*height))
  r.setFill(color)
  r.draw(win)
  return r

  
def createDalekTorso(win, x, y, size, bodyColor):
  r = createRectangle(win, x, y, size, 2, 1, bodyColor)
  return r



def createDalekTop(win, x, y, size):
  domeColor = "grey"
  bodyColor = "grey"
  
  c = createCircle(win, x, y, size, domeColor)
  r = createDalekTorso(win, x - size, y, size, bodyColor)

  return [c, r]



def createDalekBottomBackdrop(win, x, y, size, color):
  bottom = y + size*3
  topL = x - size
  topR = x + size
  bottomL = x - 1.55 * size
  bottomR = x + 2 * size

  p = Polygon(Point(topL, y), Point(topR, y), Point(bottomR, bottom), Point(bottomL, bottom))
  p.setFill(color)
  p.draw(win)

  return p



def createDalekBase(win, x, y, size, color):
  bezel = 0.05
  bottom = y + size*3
  bottomL = x - 1.55*size
  bottomR = x + 2*size

  top = bottom-size*0.2
  topLeftX = bottomL + size*bezel
  topRightX = bottomR - size*bezel
  bezelHeight = top+size*bezel

  points = []
  points.append(Point(bottomL, bottom))
  points.append(Point(bottomL, bezelHeight))
  points.append(Point(topLeftX, top))
  points.append(Point(topRightX, top))
  points.append(Point(bottomR, bezelHeight))
  points.append(Point(bottomR, bottom))
  
  p = Polygon(points)
  p.setFill(color)
  p.draw(win)

  return [p]



def isDalekAtEdge(winX, size, dalek):
  rightX = winX - size - 0.1 * winX
  leftX = size + winX*0.1
  dalekX = dalek[0].getCenter().getX()
  return (dalekX > rightX) or (dalekX < leftX )



def createDalek(win, x, y, size):
  top = createDalekTop(win, x, y, size)
  bottom = createDalekBottom(win, x, y + size, size)

  return top + bottom



def main():
  winX = 1440
  winY = 900

  dalekSize = 75
  dalekSpeed = 1
  dalekX = 250
  dalekY = 500
  timeBetweenFrames = 0.01

  tardisX = 280
  tardisY = 180
  tardisSize = 300

  win = GraphWin("Dalek", winX, winY)

  # for easy bug, swap these
  tardis = createTardis(win, tardisX, tardisY, tardisSize)
  dalek = createDalek(win, dalekX, dalekY, dalekSize)

  while (True):
    
    for part in dalek:
      part.move(dalekSpeed, 0)
    
    if isDalekAtEdge(winX, dalekSize, dalek):
      dalekSpeed *= -1

    # to make testing easier, quit any time the screen is clicked
    if (win.checkMouse()):
      quit()

    time.sleep(timeBetweenFrames)

main()

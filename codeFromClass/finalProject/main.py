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



def createDalekBottomBackdrop(win, points, color):

  p = Polygon(Point(points["topLeft"], points["top"]), Point(points["topRight"], points["top"]), Point(points["bottomRight"], points["bottom"]), Point(points["bottomLeft"], points["bottom"]))
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

  return p



def createDalekPanels(win, backdrop, size):
  topLeftX = backdrop.getPoints()[0].getX()
  topRightX = backdrop.getPoints()[1].getX()
  bottomRighX = backdrop.getPoints()[2].getX()
  bottomLeftX = backdrop.getPoints()[3].getX()

  top = backdrop.getPoints()[0].getY()
  bottom = backdrop.getPoints()[2].getY()

  topWidth = topRightX - topLeftX
  bottomWidth = bottomRighX - bottomLeftX

  panels = 4

  topIncrement = topWidth/panels
  bottomIncrement = bottomWidth/panels

  lines = []
  for i in range(panels):
    lines.append(Line(Point(topLeftX + topIncrement*(i+1), top), Point(bottomLeftX + bottomIncrement*(i+1), bottom)))
    lines[i].draw(win)
  
  return lines


def createDalekBottom(win, x, y, size):
  backdropColor = color_rgb(150, 150, 100)
  baseColor = color_rgb(100, 100, 50)

  points = {}
  points["topLeft"] = x - size
  points["topRight"] = x + size
  points["bottomLeft"] = x - 1.55 * size
  points["bottomRight"] = x + 2 * size
  points["top"] = y
  points["bottom"] = y + size*3

  backdrop = createDalekBottomBackdrop(win, points, backdropColor)  
  panels = createDalekPanels(win, backdrop, size)
  base = createDalekBase(win, x, y, size, baseColor)

  parts = [backdrop] + panels + [base]

  return parts



def createDalek(win, x, y, size):
  top = createDalekTop(win, x, y, size)
  bottom = createDalekBottom(win, x, y + size, size)

  return top + bottom



def isDalekAtEdge(winX, size, dalek):
  rightX = winX + size*2
  dalekX = dalek[0].getCenter().getX()
  return (dalekX > rightX) 


def main():
  winX = 1440
  winY = 900

  dalekSize = 75
  dalekSpeed = 1
  dalekX = 0 - dalekSize
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
      for part in dalek:
        part.move(dalekX-winX, 0)

    # to make testing easier, quit any time the screen is clicked
    if (win.checkMouse()):
      quit()

    time.sleep(timeBetweenFrames)

main()

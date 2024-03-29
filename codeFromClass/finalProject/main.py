from graphics import *
from tardis import *
from landscape import *

def createCircleOutline(win, x, y, size):
  c = Circle(Point(x,y), size)
  c.draw(win)
  return [c]

def createCircle(win, x, y, size, color):
  c = Circle(Point(x,y), size)
  c.setFill(color)
  c.draw(win)
  return [c]

def createRectangle(win, x, y, size, width, height, color):
  r = Rectangle(Point(x, y), Point(x + size*width, y + size*height))
  r.setFill(color)
  r.draw(win)
  return [r]



def createDalekTorsoStripes(win, x, y, size, color):
  numberOfStripes = 5
  width = 12
  spaceBetweenStripes = size/(numberOfStripes-1)

  stripes = []
  left = x - size*0.05
  right = x + size*2.05

  for i in range(numberOfStripes):
    height = y + spaceBetweenStripes*i - width/2 + 1 # one pixel offset required to align with bottom
    stripes.append(Line(Point(left, height), Point(right, height)))
    stripes[i].setOutline(color)
    stripes[i].setWidth(width)
    stripes[i].draw(win)

  return stripes



def createDalekWhisk(win, x, y, size):
  left = x + size*2
  right = left + size * 1.5
  y += size

  stalk = Line(Point(left, y ), Point(right, y ))
  stalk.setOutline("grey")
  stalk.setWidth(3)
  stalk.draw(win)

  left += size*0.3

  whisk = []
  whisk.append(Oval(Point(left, y+size*0.1), Point(right, y-size*0.1)))
  whisk.append(Oval(Point(left, y+size*0.05), Point(right, y-size*0.05)))
  whisk.append(Oval(Point(left, y+size*0.15), Point(right, y-size*0.15)))

  for wire in whisk:
    wire.setOutline("grey")
    wire.draw(win)

  return whisk + [stalk]



def createDalekTorso(win, x, y, size, color, darkColor):
  r = createRectangle(win, x, y, size, 2, 1, color)
  stripes = createDalekTorsoStripes(win, x, y, size, darkColor)
  whisk = createDalekWhisk(win, x, y, size)

  return r + stripes + whisk



def createDalekEyeStalk(win, x, y, size, color, darkColor):
  eyePoints = []
  eyePoints.append(Point(x+size*1.9, y-size*0.45))
  eyePoints.append(Point(x+size*2.2, y-size*0.65))
  eyePoints.append(Point(x+size*2.2, y-size*0.25))
  eye = Polygon(eyePoints)
  eye.setFill("black")
  eye.draw(win)

  stalk = createRectangle(win, x+size*0.5, y-size*0.5, size, 1.5, 0.1, "grey")
  ball = createCircle(win, x+size*1.5, y-size*0.45, size*0.15, "lightGrey")

  return stalk + ball + [eye]



def createDalekTop(win, x, y, size):
  color = color_rgb(150, 150, 100)
  darkColor = color_rgb(100, 100, 50)
  
  eyeStalk = createDalekEyeStalk(win, x, y, size, color, darkColor)
  dome = createCircle(win, x, y, size, color)
  torso = createDalekTorso(win, x - size, y, size, color, darkColor)
  

  return dome + torso + eyeStalk



def createDalekBottomBackdrop(win, points, color):

  p = Polygon(Point(points["topLeft"], points["top"]), Point(points["topRight"], points["top"]), Point(points["bottomRight"], points["bottom"]), Point(points["bottomLeft"], points["bottom"]))
  p.setFill(color)
  p.draw(win)

  return [p]



def createDalekBase(win, basePoints, size, color):
  bezel = 0.05

  top = basePoints["bottom"] - size*0.2
  topLeftX = basePoints["bottomLeft"] + size*bezel
  topRightX = basePoints["bottomRight"] - size*bezel
  bezelHeight = top + size*bezel

  points = []
  points.append(Point(basePoints["bottomLeft"], basePoints["bottom"]))
  points.append(Point(basePoints["bottomLeft"], bezelHeight))
  points.append(Point(topLeftX, top))
  points.append(Point(topRightX, top))
  points.append(Point(basePoints["bottomRight"], bezelHeight))
  points.append(Point(basePoints["bottomRight"], basePoints["bottom"]))
  
  p = Polygon(points)
  p.setFill(color)
  p.draw(win)

  return [p]



def createDalekPanels(win, points, size, numberOfPanels):
  topWidth = points["topRight"] - points["topLeft"]
  bottomWidth = points["bottomRight"] - points["bottomLeft"]

  topIncrement = topWidth/numberOfPanels
  bottomIncrement = bottomWidth/numberOfPanels

  lines = []
  for i in range(numberOfPanels):
    lines.append(Line(Point(points["topLeft"] + topIncrement*(i+1), points["top"]), Point(points["bottomLeft"] + bottomIncrement*(i+1), points["bottom"])))
    lines[i].draw(win)
  
  return lines



def createDalekCircles(win, points, size, color):
  # TODO: come up with model that doesn't require fudge factors
  numberOfPanels = 4
  circlesPerPanel = 5
  topPanelWidth = (points["topRight"] - points["topLeft"])/numberOfPanels
  dy = (points["bottom"]-points["top"])/(circlesPerPanel+1)
  dx = (points["topRight"] - points["topLeft"])/(numberOfPanels*2+1)*2.18
  dxBottom = (points["bottomRight"] - points["bottomLeft"])/(numberOfPanels*2+1)
  ddx = (dx + dxBottom)/(numberOfPanels+1)*0.35
  dLeftX = (points["bottomLeft"] - points["topLeft"])/2/(circlesPerPanel+1)
  print(dLeftX)
  
  radiusIncrement = size*0.013

  circles = []
  y = points["top"] - dy*0.33
  r = topPanelWidth/3
  #print(ddx)
  for i in range(circlesPerPanel):
    y += dy
    r += radiusIncrement
    dx += ddx
    x = points["topLeft"] + dLeftX*(i + 2) + topPanelWidth/2
    
    for j in range(numberOfPanels):
      circles += createCircleOutline(win, x, y, r)
      x += dx

  for circle in circles:
    circle.setOutline(color)
  
  return circles


def createDalekBottom(win, x, y, size):
  color = color_rgb(150, 150, 100)
  darkColor = color_rgb(100, 100, 50)
  numberOfPanels = 4
  circlesPerPanel = 5

  points = {}
  points["topLeft"] = x - size
  points["topRight"] = x + size
  points["bottomLeft"] = x - 1.55 * size
  points["bottomRight"] = x + 2 * size
  points["top"] = y
  points["bottom"] = y + size*3

  backdrop = createDalekBottomBackdrop(win, points, color)  
  panels = createDalekPanels(win, points, size, numberOfPanels)
  base = createDalekBase(win, points, size, darkColor)
  circles = createDalekCircles(win, points, size, darkColor)

  return backdrop + panels + base + circles



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

  landscape = createLandscape(win, winX, winY)
  tardis = createTardis(win, tardisX, tardisY, tardisSize)
  dalek = createDalek(win, dalekX, dalekY, dalekSize)

  #testDalek = createDalek(win, 500, 200, 100)

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

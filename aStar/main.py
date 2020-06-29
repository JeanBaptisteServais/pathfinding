import cv2
import numpy as np
import random

#define variables for the picture
WIDTH  = 1000
HEIGHT = 500
ROUND_NUMBER = 1000

#Variable for a* pathfinding
OPEN_LIST       = {} #neigtbhoors
SAUVEGARDE_LIST = {} #Historic
CLOSE_LIST      = [] #To not analysis
CURRENT_NODE    = [] #Current node


def addNodeInOpenList(initalPts, gValue, points):
    global OPEN_LIST
    OPEN_LIST[(initalPts, gValue)] = list(points)


def addNodeInClosedList(points):
    global CLOSE_LIST
    CLOSE_LIST.append(points)


def recuperateNeightboorsPoints(gValue, initalPts, img):

    x = initalPts[0]
    y = initalPts[1]

    points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
              (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1),
              (x + 1, y + 1)]

    validPoints = []

    for pts in points:

        isNotBlack = verifyPïxel(pts, img, 0, 0, 0)
        isRed      = verifyPïxel(pts, img, 0, 0, 255)
        isInClosed = verifyPixelIsntInClosed(pts)

        if isNotBlack is True and isInClosed is True:
            validPoints.append(pts)

        elif isRed is False:
            return False

    addNodeInOpenList(initalPts, gValue, validPoints)

    return True


def verifyPïxel(pts, img, px1, px2, px3):
    if img[pts[1], pts[0]][0] == px1 and\
       img[pts[1], pts[0]][1] == px2 and\
       img[pts[1], pts[0]][2] == px3:
        return False
    return True


def verifyPixelIsntInClosed(pts):
    for i in CLOSE_LIST:
        if i == pts:
            return False
    return True


def calculG():
    """{((83, 357), 0): [coord1, coord2 ...]"""

    dicoCost = {0: 10, 1: 10, 2: 10, 3: 10, 4: 14, 5: 14, 6: 14, 7: 14}

    gValueList = [coord[1] + dicoCost[nb] for coord, neightboorsCoord in OPEN_LIST.items()
                  for nb, i in enumerate(neightboorsCoord)]
    return gValueList


def calculH(pointsArrivé):

    hValueList = []
    for k, v in OPEN_LIST.items():
        for points in v:

            x1, y1 = points
            x2, y2 = pointsArrivé

            caseTotal = (abs(x2 - x1) + abs(y2 - y1)) * 10
            hValueList.append(caseTotal)

    return hValueList



def calculF(gValueList, hValueList):
    return [gValue + hValue for gValue, hValue in zip(gValueList, hValueList)]
     

def searchMinF(fValueList, gValueList, hValueList):

    global CURRENT_NODE

    minus = fValueList.index(min(fValueList))
    for k, neightboorsCoord in OPEN_LIST.items():
        CURRENT_NODE = [neightboorsCoord[minus], gValueList[minus], hValueList[minus]]



generateCoordinate = lambda width, height: (random.randrange(width), random.randrange(height))
generateRandomCircle = lambda image, points, maxRadius, color: cv2.rectangle(image, points,
                                                  (points[0] + random.randrange(maxRadius),
                                                   points[1] + random.randrange(maxRadius)), color, -1)
generateCircle = lambda image, points, radius, color:\
                        cv2.circle(image, points, radius, color, -1)
drawPoints = lambda image, points, color: cv2.circle(image, points, 1, color, 1)




#Create picture
img = np.ones((HEIGHT, WIDTH, 3), np.uint8) * 255

pointDépart = generateCoordinate(WIDTH, HEIGHT)
pointArrivé = generateCoordinate(WIDTH, HEIGHT)


[generateRandomCircle(img, generateCoordinate(WIDTH, HEIGHT), 20, (0, 0, 0))
 for i in range(ROUND_NUMBER)]
generateCircle(img, pointDépart, 10, (255, 0, 0))
generateCircle(img, pointArrivé, 10, (0, 0, 255))
copy = img.copy()







iteration  = 0 
nodeInList = True
while nodeInList:


    if iteration == 0:
        addNodeInClosedList(pointDépart)
        nodeInList = recuperateNeightboorsPoints(0, pointDépart, img)
        gValueList = calculG()
        hValueList = calculH(pointArrivé)
        fValueList = calculF(gValueList, hValueList)
        searchMinF(fValueList, gValueList, hValueList)
        


    else:
        nodeInList = recuperateNeightboorsPoints(CURRENT_NODE[1], CURRENT_NODE[0], img)
        gValueList = calculG()
        hValueList = calculH(pointArrivé)
        fValueList = calculF(gValueList, hValueList)
        searchMinF(fValueList, gValueList, hValueList)



    #CURRENT_NODE = coord, gValue, hValue

    addNodeInClosedList(CURRENT_NODE[0])
    drawPoints(copy, CURRENT_NODE[0], (0, 0, 255))

    SAUVEGARDE_LIST[iteration] = OPEN_LIST

    iteration += 1

    cv2.imshow('image', copy)
    cv2.waitKey(1)
    
    OPEN_LIST = {}

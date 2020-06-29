import cv2
import random


class constructionCarte:
    

    def __init__(self, img, width, height, square, numberObstacle, sizeObstacle):
   
        self.square = square
        self.width = width
        self.height = height
        self.img = img
        self.numberObstacle = numberObstacle
        self.sizeObstacle = sizeObstacle

    def generateCoords(self):

        generateCoordinate = lambda width, height:\
                             (random.randrange(width), random.randrange(height))
  
        pointDépart = generateCoordinate(self.width, self.height)
        pointArrivé = generateCoordinate(self.width, self.height)

        generateCircle = lambda image, points, radius, color:\
                                cv2.circle(image, points, radius, color, -1)

        generateCircle(self.img, pointDépart, 2, (255, 0, 0))
        #generateCircle(self.img, pointArrivé, 2, (255, 255, 0))


        return pointDépart, pointArrivé


    def generateObstacle(self):

        color = (0, 0, 0)

        for i in range(self.numberObstacle):

            coordX = random.randrange(self.width)
            coordY = random.randrange(self.height)

            size = random.randrange(self.sizeObstacle)

            cv2.rectangle(self.img, (coordX, coordY),
                          (coordX + size, coordY + size), color, -1)


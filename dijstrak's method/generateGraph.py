import cv2
import random
from scipy.spatial import distance


class Graph:

    def __init__(self, image, height, width, numberPts):
        self.image     = image
        self.height    = height
        self.width     = width
        self.numberPts = numberPts


        self.depart = 0
        self.arrivé = 0
        self.coordinates = []
        self.score = []

        self.departToPts = 0
        self.arrivaToPts = 0
        self.scoreDepAr  = []


    def generatePoints(self):

        self.coordinates = [(random.randrange(self.width),
                             random.randrange(self.height))
                            for i in range(self.numberPts)]

        self.depart = (random.randrange(self.width),
                       random.randrange(self.height))

        self.arrivé = (random.randrange(self.width),
                       random.randrange(self.height))


    def drawPoints(self):

        black = (0, 0, 0)
        red   = (0, 0, 255)
        size  = 10
        remplissage = 1


        [cv2.circle(self.image, (x, y), size, black, remplissage)
         for (x, y) in self.coordinates]

        cv2.circle(self.image, self.depart, size, red, -remplissage)
        cv2.circle(self.image, self.arrivé, size, (0, 255, 0), -remplissage)



    def makeLiaisonScore(self):


        [cv2.line(self.image, (x1, y1), (x2, y2),(130, 130, 130), 2)
         for (x1, y1) in self.coordinates
         for (x2, y2) in self.coordinates
         if (x1, y1) != (x2, y2)]

        self.score = [int(distance.euclidean((x1, y1), (x2, y2)))
                      for (x1, y1) in self.coordinates
                      for (x2, y2) in self.coordinates
                      if (x1, y1) != (x2, y2)]


    def makeLiaisonDepartureArrival(self):
        
        #Choice randomly an other point to attach to arrival and
        #departure
        departToRandom  = random.randrange(self.numberPts)
        arrivalToRandom = departToRandom
        while arrivalToRandom == departToRandom:
            arrivalToRandom = random.randrange(self.numberPts)

        self.departToPts = self.coordinates[departToRandom]
        self.arrivaToPts = self.coordinates[arrivalToRandom]

        cv2.line(self.image, self.arrivé, self.arrivaToPts,(130, 130, 130), 2)
        cv2.line(self.image, self.depart, self.departToPts,(130, 130, 130), 2)

        self.scoreDepAr.append(int(distance.euclidean(self.departToPts, self.depart)))
        self.scoreDepAr.append(int(distance.euclidean(self.arrivaToPts, self.arrivé)))



    def putText(self):

        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 0, 0)

        [cv2.putText(self.image, str(i), i, font, 0.4, color, 1, cv2.LINE_AA)
         for i in self.coordinates]


        findMid = lambda i, i2: (abs(int((i[0] + i2[0]) / 2)),
                                 abs(int((i[1] + i2[1]) / 2)))

        counter = 0
        for i in self.coordinates:
            for i2 in self.coordinates:
                if i != i2:
                    cv2.putText(self.image, str(self.score[counter]),
                                findMid(i, i2), font, 0.3,
                                color, 1, cv2.LINE_AA)
  
                    counter += 1



    def putTextDepartureArrival(self):

        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 0, 0)


        findMid = lambda i, i2: (abs(int((i[0] + i2[0]) / 2)),
                                 abs(int((i[1] + i2[1]) / 2)))

        [cv2.putText(self.image, str(i), i, font, 0.4, color, 1, cv2.LINE_AA)
         for i in [self.arrivé, self.depart]]

        midArr = findMid(self.arrivé, self.arrivaToPts)
        midDep = findMid(self.depart, self.departToPts)
        

        [cv2.putText(self.image, str(self.scoreDepAr[nb]), i, font, 0.3,
                    color, 1, cv2.LINE_AA) for nb, i in enumerate([midDep, midArr])]
        


    def scoreDepartArrivé(self):
        return self.scoreDepAr

    def liaisonArrivalDep(self):
        return self.arrivaToPts, self.departToPts

    def recuperateArrivalDepCoord(self):
        return self.arrivé, self.depart

    def recuperateScore(self):
        return self.score

    def recuperateCoordinate(self):
        return self.coordinates

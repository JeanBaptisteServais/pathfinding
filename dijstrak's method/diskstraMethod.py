import cv2
from scipy.spatial import distance

class dikstra:

    def __init__(self, arrivé, départ, image, arrivaToPts, departToPts, coordinates, score, scoreDepAr):

        self.image = image

        self.arrivé = arrivé
        self.départ = départ

        self.arrivaToPts = arrivaToPts
        self.departToPts = departToPts
        self.scoreDepAr  = scoreDepAr

        self.coordinates = coordinates
        self.score = score

        self.roadScore = []
        self.coordinatesRoad = []
        self.closeList = []

    def searchingRoad(self):


        dikstra.departureScore(self, self.départ, self.departToPts, self.scoreDepAr[0])
        iteration = 1
        isNotArrival = True
        while isNotArrival:


            dikstra.searchingOtHerPoints(self)
                
            if self.coordinatesRoad[-1] == self.arrivaToPts:
                isNotArrival = False


            cv2.imshow("image", self.image)
            cv2.imwrite(str(iteration) + ".png", self.image)
            cv2.waitKey(1000)


        dikstra.departureScore(self, self.arrivé, self.arrivaToPts, self.scoreDepAr[1])

        cv2.imshow("image", self.image)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()







    def searchingOtHerPoints(self):

        currentPoint = self.coordinatesRoad[-1]

        listeScore = []
        listeCoord = []


        copy = self.image.copy()

        for coord1 in self.coordinates:
            for coord2 in self.coordinates:

                isntInClosed = dikstra.isntInListe(self, self.closeList, coord2)

                if coord1 == currentPoint and coord2 != currentPoint and isntInClosed is True:
                    dikstra.makeLine(self, coord1, coord2, (255, 0, 0), copy)

                    dist = int(distance.euclidean(currentPoint, coord2))
                    listeScore.append(dist + self.roadScore[-1])
                    listeCoord.append(coord2)

                    cv2.imshow("image", copy)
                    cv2.waitKey(100)


        minScoreIndex = listeScore.index(min(listeScore))
        coord = listeCoord[minScoreIndex]


        self.roadScore.append(min(listeScore))
        self.coordinatesRoad.append(coord)
        self.closeList.append(coord)


        dikstra.makeLine(self, self.coordinatesRoad[-1], self.coordinatesRoad[-2], (0, 0, 255), self.image)
        cv2.imshow("image", self.image)
        cv2.waitKey(1000)



    def departureScore(self, pts1, pts2, score):

        
        dikstra.makeLine(self, pts1, pts2, (255, 0, 0), self.image)

        cv2.imshow("image", self.image)
        cv2.waitKey(1000)

        dikstra.makeLine(self, pts1, pts2, (0, 0, 255), self.image)


        self.roadScore.append(score)
        self.coordinatesRoad.append(pts2)
        self.closeList.append(pts2)













    def isntInListe(self, liste, coord):
        for i in liste:
            if i == coord:
                return False

        return True


    def makeLine(self, pts1, pts2, color, image):
        cv2.line(image, pts1, pts2, color, 3)
        









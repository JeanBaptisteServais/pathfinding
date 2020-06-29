import cv2
from scipy.spatial import distance
from displayingSearching import displayingSearching



class searchingArrivé:

    def __init__(self, img, departCoord, coordArrive, width, height):

        self.img = img
        self.departCoord = departCoord
        self.coordArrive = coordArrive
        self.width = width
        self.height = height
        self.roads = [ [(departCoord, 0)] ]

        
        self.coordx, self.coordy = departCoord 


    def searching(self, iteration):

        displaying = displayingSearching(self.img, self.coordArrive, self.departCoord)

        x, y = self.departCoord 

        listeDistance  = []
        listeCoordonée = []

        for i in range(y - iteration, y + (iteration + 1)):
            for j in range(x - iteration, x + (iteration + 1)):

                if 0 <= i <= self.height - 1 and 0 <= j <= self.width - 1:

                    isBlack = searchingArrivé.verifyPixels(self, i, j, 0, 0, 0)
                    isBlue  = searchingArrivé.verifyPixels(self, i, j, 255, 255, 0)

                    if isBlue is True:
                        for road in self.roads[-1]:
                            if road[0][0] == j and road[0][1] == i:
                                searchingArrivé.fromArrival(self, j, i)
                                return False, (j, i), self.roads

                    if isBlack is False:

                        noVisited = searchingArrivé.isAlreadyVisited(self, (j, i))
                        if noVisited is True:

                            distance = searchingArrivé.calculDistance(self, (j, i))
                            listeDistance.append(distance)
                            listeCoordonée.append((j, i))
 

        searchingArrivé.saveGardeNewRoad(self, listeDistance, listeCoordonée)
        displaying.displaying(iteration, self.roads)
        self.img[self.departCoord[1], self.departCoord[0]] = 255, 0, 0

        return True, None, None



    def fromArrival(self, x, y):

        listeCoord = [(x, y)]
        iteration = 1
        listeCoord2 = [self.departCoord]

        while True:

            for i in self.roads[::-1]:
                for j in i:
                    dst = distance.euclidean(listeCoord[-1], j[0])

                    notBlack = searchingArrivé.verifyPixels(self, j[0][1], j[0][0], 0, 0, 0)

                    if iteration < 5 :
                        notIn = j[0] not in listeCoord
                        if dst <= 1.4142135623730951 and notBlack is False and notIn is True:
                            listeCoord.append(j[0])
                            self.img[j[0][1], j[0][0]] = 0, 255, 255
                            if self.departCoord == listeCoord[-1]:
                                return True

                    else:
                        if dst <= 2 and notBlack is False and notIn is True:
                            listeCoord.append(j[0])
                            self.img[j[0][1], j[0][0]] = 0, 255, 255
                            if self.departCoord == listeCoord[-1]:
                                return True

                    showing1 = cv2.resize(self.img, (500, 500))
                    cv2.imshow("image", showing1)
                    cv2.waitKey(1)

            iteration += 1




    def saveGardeNewRoad(self, listeDistance, listeCoordonée):

        newValue = []
        minimum = min(listeDistance)

        for nb, distance in enumerate(listeDistance):
            if distance == minimum:
                newValue.append((listeCoordonée[nb], minimum))
        self.roads.append(newValue)



    def isAlreadyVisited(self, pts):
        verifyCoord = [r[0] for road in self.roads for r in road]
        if pts not in verifyCoord:
            return True
        return False



    def calculDistance(self, pts):
        dst = distance.euclidean(self.departCoord, pts)
        return dst


    def verifyPixels(self, i, j, px1, px2, px3):

        if self.img[i, j][0] == px1 and\
           self.img[i, j][1] == px2 and\
           self.img[i, j][2] == px3:
            return True


        return False

        
        

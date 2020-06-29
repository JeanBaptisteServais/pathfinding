import cv2

class displayingSearching:

    def __init__(self, img, coordArrive, pointDépart):

        self.img = img
        self.coordArrive = coordArrive
        self.pointDépart = pointDépart


    def displaying(self, iteration, roads):

        nbDisplay = len(roads) - 5

        if iteration > 10: nbDisplay = len(roads) - 10

        for nb, i in enumerate(roads):

            if nb < nbDisplay:
                for j in i:
                    self.img[j[0][1], j[0][0]] = 150, 255, 125
            else:
                for i in roads[nbDisplay:]:
                    for j in i:
                        self.img[j[0][1], j[0][0]] = 0, 0, 255


        self.img[self.coordArrive[1], self.coordArrive[0]] = 255, 255, 0























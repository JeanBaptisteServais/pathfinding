import cv2
import numpy as np

from constructionCarte import constructionCarte
from displayingSearching import displayingSearching
from searchingArrivé import searchingArrivé

height = 25
width  = 25
square = 10

img = np.ones((height, width, 3), np.uint8) * 255

#Construct map
carte = constructionCarte(img, width, height, square, 60, 2)
carte.generateObstacle()
pointDépart, pointArrivé = carte.generateCoords()

copy = img.copy()


searching = searchingArrivé(copy, pointDépart, pointArrivé, width, height)


iteration = 1
oContinuer = True
print(pointDépart, pointArrivé, iteration - 1)


while oContinuer:

    oContinuer, _, _ = searching.searching(iteration)


    showing = cv2.resize(copy, (500, 500))
    cv2.imshow("image", showing)
    cv2.waitKey(1)

    iteration += 1








    

print("")
print(pointDépart, pointArrivé, iteration - 1)




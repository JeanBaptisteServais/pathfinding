import cv2
import numpy as np


from generateGraph import Graph
from diskstraMethod import dikstra

def generateGraphique(image, height, width, numberPts):

    graphique = Graph(image, height, width, numberPts)
    graphique.generatePoints()
    graphique.makeLiaisonScore()
    graphique.makeLiaisonDepartureArrival()
    graphique.drawPoints()
    graphique.putText()
    graphique.putTextDepartureArrival()


    score = graphique.recuperateScore()
    coordinates = graphique.recuperateCoordinate()
    arrivé, depart = graphique.recuperateArrivalDepCoord()
    arrivaToPts, departToPts = graphique.liaisonArrivalDep()
    scoreDepAr = graphique.scoreDepartArrivé()

    searching = dikstra(arrivé, depart, image, arrivaToPts,
                        departToPts, coordinates, score, scoreDepAr)


    searching.searchingRoad()





    return score, coordinates


height    = 500
width     = 1200
numberPts = 20

image = np.ones((height, width, 3), np.uint8) * 255


score, coordinates = generateGraphique(image, height, width, numberPts)














cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

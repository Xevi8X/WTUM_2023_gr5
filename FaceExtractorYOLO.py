class FaceExtractorYOLO():

    def __initNN(self):
        # inicjalizacja sieci, wczytanie pliku z modelem
        pass


    def recognize(self,img):
        # img - obraz wejsciowy, bodajże ndarray (X,Y,3) uint8 
        img_with_box = img.copy()
        faces = []
        # img_with_box - obraz wejsciowy z narysowanymi boxami
        # faces - lista wycietych twarzy
        return (img_with_box,faces)
    
    def __init__(self):
        self.__initNN()
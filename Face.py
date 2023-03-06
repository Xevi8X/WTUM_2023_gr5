class Face():
    def __init__(self, img):
        self.img = img
        self.rec_emotion = []

    def setEmotion(self,rec_emotion):
        self.rec_emotion = rec_emotion
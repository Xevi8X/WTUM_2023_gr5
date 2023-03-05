class Face():
    def __init__(self, img):
        self.img = img
        self.emotion = ""
        self.precision = -1
    
    def setEmotion(self,emotion, prescision):
        self.emotion = emotion
        self.precision = prescision
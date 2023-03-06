from Face import Face
import tensorflow as tf
import cv2 as cv
import numpy as np

class EmotionRecognizer():

    def __init__(self):
        self.model : tf.keras.Model
        self.model = tf.keras.models.load_model("best_model.h5") # type: ignore
        self.emotions = {0: 'Angry', 1:'Disgust', 2:'Fear',3: 'Happy', 4:'Sad', 5:'Surprise', 6:'Neutral'}
        
    def recognize(self, face: Face):
        img = cv.resize(face.img, (48,48))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = img / 255.0
        predictions = self.model.predict(tf.expand_dims(img,0))
        #print(predictions)
        rec_emotions = []
        for i,prediction in enumerate(predictions[0]):
            #print(prediction)
            if prediction > 0.05:
                rec_emotions.append((self.emotions[i],prediction*100))
        rec_emotions.sort(key=lambda a: a[1],reverse=True)
        return rec_emotions
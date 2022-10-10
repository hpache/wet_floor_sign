'''
Henry Pacheco Cachon
7 October 2022

Class represents an object that detects spills through a webcam stream
'''

import cv2
import tensorflow as tf
import numpy as np

class WetFloorSign:

    def __init__(self, uri=0):
        '''
        Parameters:
        -------------
        uri: String or int. Default to 0 to use a webcam as a stream, can input
        IP Camera URI in order to use that source as a stream
        '''
        
        self.capture = cv2.VideoCapture(uri)
        self.capture.set(3,200)
        self.capture.set(4,200)
        self.model = tf.keras.models.load_model('./models/version2/')
        self.categories = ['dry', 'wet']
        self.notified = False
    

    def survey(self, image):
        '''
        Method responsible for running stream through NN

        Parameters:
        -------------
        image: numpy.ndarray returned from cv2.VideoCapture.read()
        '''

        image_input = cv2.resize(image, (200,200))
        image_arr = np.asarray(image_input)
        model_estimate = self.model.predict(np.array([image_arr]))
        prediction = self.categories[model_estimate.argmax()]

        if self.notified == False and prediction == 'wet':
            self.notify()
    

    def notify(self):
        '''
        Method responsible for notifying admin
        '''

        self.notified = True
        print("The floor is wet!")
    

    def respond(self):
        '''
        Method responsible for resetting the notification
        '''

        self.notified = False
    

    def survey_stream(self):
        '''
        Method responsible for surveying the window stream. More usefull for testing 
        that the class works as intended. 
        '''

        while True:
            _, image = self.capture.read()
            self.survey(image)
            cv2.imshow("Webcam", image)
    
            if cv2.waitKey(1) & 0xFF==ord('q'):
                self.capture.release()
                break
        
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    

if __name__ == "__main__":

    test = WetFloorSign()
    test.survey_stream()
'''
Henry Pacheco Cachon
25 October 2022

Updated 31 October 2022
Class only responsible for taking in an image and spitting out a classification
'''

import cv2
import tensorflow as tf
import numpy as np

class WetFloorSign:

    def __init__(self, model_path = './models/version3/'):
        '''
        Parameters:
        -------------
        uri: String or int. Default to 0 to use a webcam as a stream, can input
        IP Camera URI in order to use that source as a stream
        '''
        self.model = tf.keras.models.load_model(model_path)
        self.categories = ['dry', 'wet']

    

    def classify(self, image):
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

        return prediction

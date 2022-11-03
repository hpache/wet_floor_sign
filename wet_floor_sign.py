'''
Henry Pacheco Cachon
25 October 2022

Updated 31 October 2022
Class only responsible for taking in an image and spitting out a classification
'''

import cv2
import tensorflow as tf
import numpy as np
from datetime import datetime
import pytz
import os


class WetFloorSign:

    def __init__(self, model_path = './models/version5/'):
        '''
        Parameters:
        -------------
        uri: String or int. Default to 0 to use a webcam as a stream, can input
        IP Camera URI in order to use that source as a stream
        '''
        self.model = tf.keras.models.load_model(model_path)
        self.categories = ['dry', 'wet']
        self.photo_point = 0
        self.photo_paths = []

    
    def update(self, response):
        updated_paths = {}

        for old_path in response:
            
            new_status = response[old_path]

            if new_status == "False Positive":
                os.rename(old_path, f'./static/photos/retrain_data/dry/{old_path.split("/")[-1]}')
                updated_paths[old_path] = f'./static/photos/retrain_data/dry/{old_path.split("/")[-1]}'
            else:
                os.rename(old_path, f'./static/photos/retrain_data/wet/{old_path.split("/")[-1]}')
                updated_paths[old_path] = f'./static/photos/retrain_data/wet/{old_path.split("/")[-1]}'
        
        return updated_paths


    def classify(self, image, camera_num):
        '''
        Method responsible for running stream through NN

        Parameters:
        -------------
        image: numpy.ndarray returned from cv2.VideoCapture.read()
        '''
        if image.any() != None:
            image_input = cv2.resize(image, (300,300))
            image_arr = np.asarray(image_input)
            model_estimate = self.model.predict(np.array([image_arr]))
            prediction = self.categories[model_estimate.argmax()]

            if prediction == "wet":
                time_capt = datetime.now(pytz.utc)
                file_path = f'./static/photos/retrain_data/tmp/{self.photo_point}.jpg'
                cv2.imwrite(file_path, image)
                self.photo_paths.append(file_path)
                self.photo_point += 1
                
                return {"wet":True,  
                        "timestamp": f'{time_capt.hour}:{time_capt.minute:02d} GMT',
                        "camera": camera_num,
                        "hash": f'{self.photo_point - 1}',
                        "path": file_path}
            else:

                return {"wet": False}
        else:
            return {"error": "Camera footage not found!"}

'''
Henry Pacheco Cachon
31 October 2022

This class is responsible for handling camera streams from opencv2
'''
import cv2

class Camera:

    def __init__(self, camera_urls = None):
        
        if camera_urls == None:
            self.capture = cv2.VideoCapture(0)
            self.cameras = None
        else:
            self.cameras = camera_urls
            self.capture = cv2.VideoCapture(camera_urls[0])
            self.current_camera = 0
    

    def stream(self):
        '''
        Returns
        ---------
        Encoded image for flask template
        '''

        while True:
        
            success,frame = self.capture.read()

            if success:

                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type image/jpeg\r\n\r\n' + frame + b'\r\n')
    
            else:
                break
    

    def get_current_cam(self):
        '''
        Returns
        ------------
        String: Camera string 
        Int: If using a webcam, the method returns 0
        '''


        if self.cameras != None:
            return self.cameras[self.current_camera]
        else:
            return 0
    
    def next(self):
        '''
        Method handles the next button operation
        '''

        if self.cameras != None:

            self.current_camera = (self.current_camera + 1) % (len(self.cameras))
            self.capture = cv2.VideoCapture(self.cameras[self.current_camera])


    def prev(self):
        '''
        Method handles the previous button operation
        '''
        
        if self.cameras != None:
            self.current_camera = (self.current_camera - 1) % (len(self.cameras))
            self.capture = cv2.VideoCapture(self.cameras[self.current_camera])
    

    def getPhoto(self):
        '''
        Returns
        ----------
        img: ndarray
        '''

        success, img = self.capture.read()

        return img
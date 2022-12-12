'''
Henry Pacheco Cachon
31 October 2022

This class is responsible for handling camera streams from opencv2
'''
import cv2

class Camera:

    def __init__(self, camera_urls = None):
        
        if camera_urls == None:
            self.capture = None
            self.cameras = [0]
            self.num_cams = 1
            self.current_camera = 0
            self.local = True
        else:
            self.cameras = camera_urls
            self.capture = None
            self.current_camera = 0
            self.num_cams = len(self.cameras)
            self.survey = False
        
    

    def stream(self):
        '''
        Returns
        ---------
        Encoded image for flask template
        '''
        self.capture = cv2.VideoCapture(self.cameras[self.current_camera])
        while self.survey:
        
            success,frame = self.capture.read()
            self.frame = frame

            if success:

                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

                if self.local:
                    yield (b'--frame\r\n'
                        b'Content-Type image/jpeg\r\n\r\n' + frame + b'\r\n')
                else:
                    yield (b'--frame\r\n'
                        b'Content-Type:image/jpeg\r\n'
                        b'Content-Length: ' + f"{len(frame)}".encode() + b'\r\n'
                        b'\r\n' + frame + b'\r\n')
    
            else:
                break
        
        self.capture.release()
    
    
    def setNumberCameras(self, num_cams):
        '''
        Parameters
        --------------
        num_cams: int -> The number of cameras 
        '''
        self.num_cams = num_cams
    

    def setCameraUrls(self, camera_urls):
        '''
        Parameters
        -------------
        camera_uris: List[Str] -> A list of all the camera url strings
        '''
        self.cameras = camera_urls

    
    def switchState(self, switch):
        
        if switch == 1:
            self.survey = False
        else:
            self.survey = True



    def getCurrentCamera(self):
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
    

    def getNumberCameras(self):
        '''
        Returns
        ----------
        int -> Number of cameras
        '''
        return self.num_cams
    
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
        print(img)
        return self.frame
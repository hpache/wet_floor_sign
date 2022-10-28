# Model Mk2

**Created:** 30 September 2022

**Input** (200,200,3) rgb photo from webcam scaled down to 200x200 pixels.
Max accuracy was roughly 95% (rounding up).

# Layout

Input layer
Rescaling layer (normalizing)
Conv2D
Max Pooling 2D 
Conv2D
Max Pooling 2D
Conv2D
Max Pooling 2D
Flatten (down to vector)
Dense Layer

# Notes 

Works best at an angle and also from afar. The use case would be from cctv cameras. Scaling down to (200,200) on a 1080p webcam is a good sign that it might work on cctv cameras? Right now the only thing we need to improve accuracy is better data collection. The next step would be to put it on a webserver. It would be best to start testing it within a docker container...
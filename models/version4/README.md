# Model MK4

**Created:** 2 November 2022
**Input** (300,300,3) rgb photo from webcam scaled down to 200x200 pixels.
**Dataset** Augmented dataset 5000 wet and 5000 dry

 Layout

Input layer
Rescaling layer (normalizing)
Conv2D
Max Pooling 2D 
Conv2D
Max Pooling 2D
Conv2D
Max Pooling 2D
Conv2D
Max Pooling 2D
Flatten (down to vector)
Dense Layer

# Notes

Looks like the overfitting is pretty much gone, along with the noise within the learning curve.
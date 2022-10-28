# Model MK3

**Created:** 28 October 2022
**Input** (200,200,3) rgb photo from webcam scaled down to 200x200 pixels.
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

Some overfitting was present, so I increased the dataset from 1600 to 10000 photos with augmentation. This improved the overfitting, and the accuracy is at around 96%. I also increased the batch size to 250, training took longer, but it looks like it also helped with the overfitting. Maybe playing around with learning rates will help out as well. 

I added an extra layer to help with the overfitting and that seemed to resolve it. Brought down the parameters to half a million and we're within range in terms of the dataset size. Training loss and validation loss are close enough as well.
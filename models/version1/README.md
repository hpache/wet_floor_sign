# Model Mk1

**Created:** 27 September 2022

**Input:** (100,100,3) RGB photo scaled down to 100x100 pixels
Max accuracy was roughly 98% (Potential overfitting)

# Layout

Input layer
Rescaling layer (normalizing)
Conv2D
Max Pooling 2D 
Conv2D
Max Pooling 2D
Flatten (down to vector)
Dense Layer

# Notes

Works fine with camera stream, but the accuracy is terrible in real world application. I think adding another Conv2D and Max Pooling 2D layer along with increasing the parameter space will improve the accuracy. Performance will be shot, so maybe another model might be in order?
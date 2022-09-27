# Wet Floor Sign

This repo contains a tensorflow model that is able to classify a wet floor and a dry floor from a (100,100) image.


## Dataset

Photos were gathered by looking through common access photos and augmenting them. The augmentation process brought the dataset size from 29 photos to 1600 photos. 1280 photos were used for training and 320 photos were used for validation.

The test directory has one unseen photo (will increase later)

## Model

Currently, the model is on its first iteration. Improvements can be made by modifying the CNN, adding more data for training/validating, and improving the parameter space. Fitting and predicting run-time is provided by the tensorflow methods as output in their respective cells.


## How to run

**JUPYTER REQUIRED**

Make sure you have installed the necessary packages! If you are on MacOS run the following commands

```
pip install -r requirements.txt
```

If you are not on MacOS. Be sure to install 

- numpy
- augmentor
- matplotlib
- tensorflow
- pillow (optional)

i.e. run the following command

```
pip install numpy augmentor matplotlib tensorflow
```


## View 

If you wish to just view the code, just click on the ipynb files through GitHub. Fortunately, GitHub renders jupyter notebooks on their site.
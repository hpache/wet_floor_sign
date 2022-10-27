# Wet Floor Sign

This repo contains a tensorflow model that is able to classify a wet floor and a dry floor from a (100,100) image.


## Dataset

Photos were gathered by looking through common access photos and augmenting them. The augmentation process brought the dataset size from 29 photos to 1600 photos. 1280 photos were used for training and 320 photos were used for validation.

The test directory has one unseen photo (will increase later)

## Model

Currently, the model is on its first iteration. Improvements can be made by modifying the CNN, adding more data for training/validating, and improving the parameter space. Fitting and predicting run-time is provided by the tensorflow methods as output in their respective cells.


## How to run

### Jupyter Notebooks

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



#### View Notebooks

If you wish to just view the code, just click on the ipynb files through GitHub. Fortunately, GitHub renders jupyter notebooks on their site.

### Flask Application

#### Requirements

In order to run the flask application, please be sure to install flask on python:

``` pip install flask ```

You will also need to install the libraries referenced in the **Jupyter Notebooks** section.

#### Running

In order to run the application, you would need to open a terminal (or powershell for windows users). CD into the github repo and run one of the following commands:


1. ``` flask run -h localhost -p 8080 ```
2. ``` python3.x app.py ```

Note, the x should be replaced by the version of Python3 that you are running. For example, if you have Python 3.9 then you should run ``` python3.9 app.py ```

Navigate to ``` localhost:8080 ``` on a web browser to see the webpage
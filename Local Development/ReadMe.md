
# MSDS 434 Project Local Development- Spencer Puterbaugh

- This document has been assembled in order to show the actions taken to work on the final project for this course in my local development environment


## Final Project

- The Model Development folder contains source code, as jupyter notebooks, that were created for the following items:
    - Fetch the data set
    - Preprocess the data set
        - Convert sound files to features using librosa libary
        - Create csv file (called 'data.csv')
        - Write each sound file feature extraction as a row to data.csv, with label
    - Train a TensorFlow based neural network
    - Generate predictions on test data
    - Save the TF model for use in the front-end
- The Front End folder contains source code and other items that were created to serve as the interface for generating predictions from user input:
    - app.py contains the flask UI/API code that is accessible from localhost in a browser (access via 127.0.0.1/5000)
    - templates folder contains the html code for the front end (very basic but functional)
    - static folder will save the user input and allow the app.py to reference it as needed for serving predictions


## Sound Features

- During development, the librosa library for python was used to convert sound files into a number of features that are required in order to generate a prediction from the model. The required features for generating a prediction are as follows:
    - length
    - chroma_stft_mean
    - chroma_stft_var
    - rms_mean
    - rms_var
    - spectral_centroid_mean
    - spectral_centroid_var
    - spectral_bandwidth_mean
    - spectral_bandwidth_var
    - rolloff_mean
    - rolloff_var
    - zero_crossing_rate_mean
    - zero_crossing_rate_var
    - harmony_mean
    - harmony_var
    - perceptr_mean
    - perceptr_var
    - tempo
    - mfcc1_mean
    - mfcc1_var
    - mfcc2_mean
    - mfcc2_var
    - mfcc3_mean
    - mfcc3_var
    - mfcc4_mean
    - mfcc4_var

- In the Model Development folder, the 'Testing_Notebook' contains python code that will indicate how to use this library to extract all of these features from a sound file.
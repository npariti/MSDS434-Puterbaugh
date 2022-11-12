
# MSDS 434 Final Project- Spencer Puterbaugh

This is a repository for the coursework and all associated files that led up to the creation of the final project for MSDS 434, Fall 2022. Work is still in progress and as new items are added this repository will be updated as necessary until the project has been completed and submitted for grading.


## Description

- This project was designed to meet the requirements outlined in the course objectives for MSDS 434.

- The overall idea is to implement a marine mammal classification application, wherein users can submit a sound file (in .wav format for the moment but that may be extended if time allows) of an unknown marine mammal and receive a prediction from the interface that attempts to identify the marine mammal in question.
- Google Cloud Platform will be utilized as a means of serving the application to end users.
    - This will include ingesting and storing the data, using BigQueryML or AutoML to train and serve a classification model, as well as using AppEngine to deploy a publicly accessible interface that users can access.
- At this time, the interface will accept a sound file, a sound file that has been converted to csv format with appropriate features (documentation to come), or accept an API call that contains the sound file features.
- Local development has been done to establish the necessary items that will be required to complete this process.
    - Python to scrape the training data (sound files) from the Watkins Marine Mammal Sound database.
    - Python to convert the sound files into a dataframe/csv that contains extracted features and labels.
    - Python to train a TensorFlow based CNN that was used for local development and testing.
    - Python to serve a Flask based web interface to accept user input and serve the saved TF model to generate predictions.
- A Google Cloud Platform based project has been instantiated, and development has commenced/is progressing for translating the local implementation into a cloud based deployment.
    - Data Ingest to Cloud Storage - Complete
    - Data Transfer to BigQuery Dataset/Table - Complete
    - BigQuery ML Model Trained - Complete
    - BigQuery ML Model Exported - Complete
    - BigQuery ML Model Deployed/Served - In Progress
    - AutoML Model - Not Needed for this Implementation, BigQuery ML Custom Model is Being Utilized
    - AppEngine Based Pyton Web UI - In Progress
    - Deployment of WebUI for Public Consupmption - In Progress
    - Continuous Deployment - In Progress, will trigger changes from GitHub Repository for WebUI
    - Multiple Environments - In Progress

## Accessing the Cloud Deployment

- to be added

# MSDS 434 Project Predictive App Set Up- Spencer Puterbaugh

- This directory contains a copy of the same files used in the repository that was set up to leverage CI/CD to push changes to the GCP project automatically.
    - https://github.com/saputerb/MSDS434-App

- The app uses a simple html template to display a front end that will accept the sound files as uploads and return a prediction.
    - Accepts .wav files, as well as csv and json files that contain the required features
    - Below is the url for the application hosted on GCP
        - https://front-end-microservice-snovrulsya-uc.a.run.app
    - There is also a development environment that can be used for testing purposes prior to pushing changes into production.
        - https://front-end-microservice-dev-snovrulsya-uc.a.run.app

- The app also has an endpoint that accepts POST requests from a curl command (or Postman or any method to interact with an https endpoint).
    - https://front-end-microservice-snovrulsya-uc.a.run.app/returnJSON











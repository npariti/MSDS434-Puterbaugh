
# MSDS 434 Project Week 1 Project Idea and Design - Spencer Puterbaugh

- This document has been assembled in order to show the actions taken to work on the final project for this course
- This documents details the actions taken to create a machine learning model (deep neural network) that will serve as the basis of the predictions served by the application.
- A sql query was developed that was executed within BigQuery in order to train the model based on the dataset created in alignment with week 4's content
    - This function needed to have more than the default memory of 256 MiB allocated in order to successfully complete its work.




## Final Project

- The final project will use a database of marine mammal sounds, sourced from the Watkins Marine Mammal Sound Database (get link), to train a multi-classification model that will allow users to upload a sound file and receive a predicted mammal from the application.
- Python will be the primary methodology, utilizing Flask as a means of hosting a simple web-based interface that allows users to interact with the model.
- Predictions will be served from the Flask based application after it has been deployed within GCP.
    - Front end interface will allow users to recieve predictions directly to their screen.
    - Predictions can also be requested from the application's API via a curl command, Postman request, or other methodology that the user would prefer to interact with the API.
- The model will be trained using a deep neural network and deployed within GCP, and served up as an endpoint that the flask application will send request to in order to generate predictions.
- Initial development and testing will be done locally on the developer's primary computing device. 
    - Once a local MVP has been developed, tested, and is working as intended, the local implemlentation will be translated into a format that will be deployed via GCP in order to take advantage of the cloud provider's added capabilities, scalability, and allow for public hosting and serving of the application.
- The model will be trained using Tensorflow, which should translate well into GCP's ecosystem as Tensorflow was initially developed by Google.
    - BigQuery ML and AutoML, GCP offerings, will be evaluated for their utility in the pipeline in order to meet the assignment requirements.
    - The locally trained model could also be saved and deployed within AppEngine, however this may not be in line with the assignment requirements and will only be leveraged as a last resort.
- The application will enable users to interact with it from a publicly hosted website, and will afford the following capabilities (subject to change):
    - Users can upload a sound file, in .wav format, and receive a predicted marine mammal classification from the model endpoint, returned to their primary screen via the web interface.
    - Users can interact with the application's API via curl or some other format to request predictions and receive them in the form of a JSON response
    - Users can upload a csv file that contains the appropriate fields (need to identify/document) of a processed sound file and receive a predicted marine mammal classification.

# MSDS 434 Project Week 3 GCP Set Up Cloud Bucket to Store Data Set - Spencer Puterbaugh

- This document has been assembled in order to show the actions taken to work on the final project for this course
- This documents details the actions taken to create a data ingestion to store the necessary data for this project in a Google Cloud Platform storage bucket
- A cloud function, based in python 3.9 was used to retrieve the data from one of my github repos that houses the data in a csv format.




## Triggering the function

1. Run the command below within the cloud shell in order to execute the function and load the data to a cloud bucket.
curl -m 70 -X POST https://us-central1-msds434-puterbaugh.cloudfunctions.net/marine-mammal-ingest \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{}'


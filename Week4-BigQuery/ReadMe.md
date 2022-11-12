
# MSDS 434 Project Week 4 GCP Set Up BigQuery Dataset and Table - Spencer Puterbaugh

- This document has been assembled in order to show the actions taken to work on the final project for this course
- This documents details the actions taken to create a data ingestion to store the necessary data for this project in a BigQuery dataset and table
- A cloud function, based in python 3.9 was used to retrieve the data from the cloud bucket set up in week 3 and load it into a BigQuery data set
    - This function needed to have more than the default memory of 256 MiB allocated in order to successfully complete its work.




## Triggering the function

1. Run the command below within the cloud shell in order to execute the function and load the data from a cloud bucket to BigQuery dataset.
curl -m 70 -X POST https://us-central1-msds434-puterbaugh.cloudfunctions.net/marine-mammal-bigquery-load \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{}'

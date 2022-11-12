
# MSDS 434 Project Week 8 GCP Set Cost Management Tools - Spencer Puterbaugh

- This document has been assembled in order to show the actions taken to work on the final project for this course
- This documents details the actions taken to create a bigquery data set that will help manage costs for a cloud based deployment
- A cloud function, based in python 3.9 was used to retrieve the data from one of my github repos that houses the data in a csv format.




## Setting Up Cost Managment

- Follow the instructions from Dr. Ostrowski's lecture, GCP documentation is [here](https://cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)

1. Link to a project
2. Verify billing is enabled
3. Enable BigQuery Data Transfer Service API [here](https://console.cloud.google.com/apis/api/bigquerydatatransfer.googleapis.com/metrics?_ga=2.64646447.1629872624.1668257441-1316210069.1656539093&project=msds434-puterbaugh)
    - Ensure you select an appropriate project for this
4. Create a BigQuery data set to house your billing data
    - I named mine billing_data_puterbaugh
5. Go to Billing Export page [here](https://console.cloud.google.com/billing/018AD1-904D4F-E20028/export/bigquery?organizationId=0)
    - Enable the sections that you would like to see the data for
    - Ensure you link to the appropriate project and the dataset that you have created to house this data
    - Enabling these actually starts the process

- It takes some time for the data load to kick off, so be prepared to wait if this is the first time you have enabled this.

## Create a Time Series Model to Forecast Cloud Costs

- Below is the code I used to created a time series forecasting model
```
CREATE OR REPLACE MODEL billing_data_puterbaugh.ga_arima_model
OPTIONS
  (model_type = 'ARIMA_PLUS',
   time_series_timestamp_col = 'usage_start_time',
   time_series_data_col = 'cost',
   auto_arima = TRUE,
   data_frequency = 'AUTO_FREQUENCY',
   decompose_time_series = TRUE
  ) AS
SELECT
  usage_start_time,
  SUM(cost) AS cost
FROM
  `msds434-puterbaugh.billing_data_puterbaugh.gcp_billing_export_resource_v1_018AD1_904D4F_E20028`
GROUP BY usage_start_time
```

- Below is a query that generates a prediction of the cost for the next 30 days, with an 80% confidence, for the project.
```
SELECT
 *
FROM
 ML.FORECAST(MODEL billing_data_puterbaugh.ga_arima_model,
             STRUCT(30 AS horizon, 0.8 AS confidence_level))
```

## Billing and Budget APIs

- You can find documentation about interacting with Google's API's for cost management and exploration [here](https://cloud.google.com/billing/docs/apis)
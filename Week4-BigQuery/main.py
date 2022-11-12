import io
from google.cloud import storage, bigquery
import pandas as pd


def bigquery_load(target):

    bucket_name = 'msds434-puterbaugh-bucket'
    source_blob = 'marine_mammal_sounds_data.csv'

    storage_client = storage.Client()

    gcp_bucket = storage_client.get_bucket(bucket_name)
    gcp_blob = gcp_bucket.blob(source_blob)

    data = gcp_blob.download_as_string()


    marine_mammal_sound_data = pd.read_csv(io.StringIO(data.decode('utf-8'))).iloc[:, 1:]

    bq_client = bigquery.Client()

    identifier = "marine_mammal_sound_data"
    full_identifier = f"{bq_client.project}.{identifier}"
    schema = bigquery.Dataset(full_identifier)

    try:
        schema = bq_client.create_dataset(schema)
    except:
        pass


    try:
        table = bq_client.create_table(f"{full_identifier}.sound_data")
    except:
        table = bq_client.get_table(f"{full_identifier}.sound_data")

    job_config = bigquery.LoadJobConfig()

    job = bq_client.load_table_from_dataframe(
        marine_mammal_sound_data,
        destination=table,
        job_config=job_config
    )  # Make an API request.

    job.result()  # Wait for the job to complete.

    table = bq_client.get_table(table)  # Make an API request.

    return "CSV Data Loaded to Bigquery Dataset"
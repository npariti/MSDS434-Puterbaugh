import requests
import io
from google.cloud import storage
import pandas as pd


def data_ingest(request):
  user='saputerb'
  pao='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'

  github_session = requests.Session()
  github_session.auth = (user, pao)

  # providing raw url to download csv from github
  csv_url = 'https://raw.githubusercontent.com/saputerb/testing-repo/main/data.csv'

  download = github_session.get(csv_url).content
  #downloaded_csv = pandas.read_csv(io.StringIO(download.decode('utf-8')), error_bad_lines=False)

  df = pd.read_csv(io.StringIO(download.decode('utf-8')), error_bad_lines=False)
  #print(df.head())

  bucket_name = 'msds434-puterbaugh-bucket'

  storage_client = storage.Client()
  gcp_bucket = storage_client.get_bucket(bucket_name)

  dest_blob = gcp_bucket.blob('marine_mammal_sounds_data.csv')

  dest_blob.upload_from_string(df.to_csv(), 'text/csv')

  return 'File written to GCP Cloud Storage'
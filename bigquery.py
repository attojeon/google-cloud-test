'''
# 1.library install
$ pip install google-cloud-bigquery

'''

import os
import google.cloud.bigquery

# Set google application credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./credential/vision-api-exit-89121177417b.json"                

# Create a BigQuery client.
bigquery_client = google.cloud.bigquery.Client()

# Query a public dataset.
query = bigquery_client.query("""
#standardSQL
SELECT * FROM publicdata.samples.natality LIMIT 5;
""")

# Print out the results.
for row in query.result():
    print(row)
                
            
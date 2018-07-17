'''
# 1.install library
# $ pip install google-cloud-storage
'''
import io
import os
import google.cloud.datastore as ds

# Set google application credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./credential/vision-api-exit-89121177417b.json"

# Instantiates a client
ds_client = ds.Client()

# The kind for the new entity
kind = 'Users'
# The name/ID for the new entity
user_firstname = 'User'

query = ds_client.query()
results = list(query.fetch())

print(results)
# code for accessing BigQuery locally

import os
def main():
    from google.cloud import bigquery
    from google.oauth2 import service_account

    # follow the steps here to download a JSON file that contains your key
    # https://cloud.google.com/docs/authentication/production#create_service_account
    path = "LOCALPATH/TO/YOUR_KEY.JSON"

    credentials = service_account.Credentials.from_service_account_file(path,
        scopes=["https://www.googleapis.com/auth/cloud-platform"], )
    client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
    return client

if __name__ == "__main__":
    client = main()


# run a query and save the output as a data frame
import pandas as pd
df = client.query(
    """
    YOUR-BigQuery-QUERY-GOES-HERE
    """
    ).to_dataframe()
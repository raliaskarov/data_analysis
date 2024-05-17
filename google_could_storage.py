# scripts to interact with google cloud storage

# @title push to google cloud storage

from google.colab import auth
from google.auth import default
from google.cloud import storage
from io import BytesIO

# authenticate
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)


def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")


# Function to upload DataFrame to Google Cloud Storage
def upload_df_to_gcs(bucket_name, df, destination_blob_name):
    """Uploads a DataFrame to the bucket as a CSV."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Create a bytes buffer for the DataFrame and write to GCS
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)  # Rewind the buffer to the beginning after writing
    blob.upload_from_file(buffer, content_type='text/csv')

    print(f"DataFrame uploaded to {destination_blob_name}.")


# Upload DataFrame to GCS
bucket_name = 'YOUR_BUCKET_NAME'
destination_blob_name = 'path/to/your/data.csv'
upload_df_to_gcs(bucket_name, df_merged, destination_blob_name)

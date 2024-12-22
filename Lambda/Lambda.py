import awswrangler as wr
import pandas as pd
import urllib.parse
import os


os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = "project-youtube-raw"  #database name
os_input_glue_catalog_table_name = "raw_statistics_reference_data"  # table name
os_input_write_data_operation = os.environ['write_data_operation']

def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        # Create DataFrame from the JSON content in S3
        df_raw = wr.s3.read_json(f's3://{bucket}/{key}')

        # Extract required columns
        df_step_1 = pd.json_normalize(df_raw['items'])

        # Write DataFrame to S3 in Parquet format
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation
        )

        return wr_response
    except Exception as e:
        print(e)
        print(f"Error processing object {key} from bucket {bucket}. Ensure they exist and the bucket is in the correct region.")
        raise e

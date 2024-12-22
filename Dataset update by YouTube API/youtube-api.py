import pandas as pd
from googleapiclient.discovery import build
import boto3
import io
import traceback

# YouTube API key and bucket details
API_KEY = ""
BUCKET_NAME = "youtube-analytics-dataset1"
REGION = "us-east-1"

# Set up YouTube API client and boto3 session
youtube = build('youtube', 'v3', developerKey=API_KEY)
session = boto3.Session(region_name=REGION)
s3_client = session.client("s3")

def update_video_stats(video_ids):
    """Fetch updated stats for a list of video IDs from YouTube API."""
    if not video_ids:
        print("No video IDs to update.")
        return {}

    try:  # Make sure video IDs are formatted as a comma-separated string
        request = youtube.videos().list(
            part="statistics",
            id=",".join(video_ids)
        )
        response = request.execute()
        stats = {item['id']: item['statistics'] for item in response['items']}
        print(f"Fetched updated stats for {len(video_ids)} videos.")
        return stats

    except Exception as e:
        print(f"Error fetching video stats: {e}")
        traceback.print_exc()
        return {}

def process_csv(file_key):
    """Download CSV from S3 with boto3, update video stats, and re-upload to S3."""
    print(f"Starting processing for {file_key}...")

    # Download the file from S3 into memory
    try:
        csv_obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_key)
        print(f"Successfully downloaded {file_key} from S3.")
        csv_content = csv_obj["Body"].read().decode("utf-8")

        # Load the CSV content into a pandas DataFrame
        df = pd.read_csv(io.StringIO(csv_content))

    except Exception as e:
        print(f"Error downloading {file_key}: {e}")
        traceback.print_exc()
        return

    # Take the top 500 rows for updating
    df = df.head(50)

    video_ids = df['video_id'].unique().tolist()

    # Debugging output for video IDs
    print(f"Processing video IDs: {video_ids}")

    # Fetch updated statistics from YouTube API
    video_stats = update_video_stats(video_ids)

    # Update DataFrame with the latest stats
    for idx, row in df.iterrows():
        video_id = row['video_id']
        if video_id in video_stats:
            stats = video_stats[video_id]
            df.at[idx, 'views'] = stats.get('viewCount', row['views'])
            df.at[idx, 'likes'] = stats.get('likeCount', row['likes'])
            df.at[idx, 'comment_count'] = stats.get('commentCount', row['comment_count'])

    # Write the updated DataFrame to a CSV in memory
    updated_csv = io.StringIO()
    df.to_csv(updated_csv, index=False)
    updated_csv.seek(0)

    # Re-upload the updated CSV to S3
    updated_file_path = f"updated/{file_key}"
    try:
        s3_client.put_object(Bucket=BUCKET_NAME, Key=updated_file_path, Body=updated_csv.getvalue())
        print(f"Updated file saved as {updated_file_path} in S3.")
    except Exception as e:
        print(f"Error uploading {file_key} to S3: {e}")
        traceback.print_exc()

def update_all_files():
    """Process all CSV files in the specified folder."""
    files_to_update = [
        "archive-1/CAvideos.csv", "archive-1/DEvideos.csv",
        "archive-1/FRvideos.csv", "archive-1/GBvideos.csv",
        "archive-1/INvideos.csv", "archive-1/JPvideos.csv",
        "archive-1/KRvideos.csv", "archive-1/MXvideos.csv",
        "archive-1/RUvideos.csv", "archive-1/USvideos.csv"
    ]
    for file_key in files_to_update:
        process_csv(file_key)

# Start the update process
print("Starting the YouTube stats update process for S3 files...")
update_all_files()
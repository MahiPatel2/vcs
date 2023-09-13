import boto3
def get_file_from_s3(bucket_name,s3_key,file_name):
    s3=boto3.client('s3')
    try:
        s3.download_file(bucket_name,s3_key,file_name)
        print("this is exam")
    except Exception as e:
        print("Error downloading",str(e))
bucket_name="data5exam31-918"
file_name="get.py"#here download file name
s3_key="move.py"#s3 bucket name

get_file_from_s3(bucket_name,s3_key,file_name)
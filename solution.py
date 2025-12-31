import boto3
import random
import string
from botocore.client import Config

# connection settings
# Using the credentials you used for the MinIO console
ACCESS_KEY = "admin"
SECRET_KEY = "password123"
BUCKET_NAME = "test-bucket"
ENDPOINT = "http://localhost:9000" # API port is 9000

# Initialize the S3 resource to interact with MinIO
s3 = boto3.resource('s3',
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version='s3v4'),
    region_name='us-east-1' # Required for S3 API compatibility
)

bucket = s3.Bucket(BUCKET_NAME)

# 1. Create a new object with random name and random data
def create_random_object():
    random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".txt"
    random_content = f"Hello! This is random data: {random.randint(1, 1000)}"
    s3.Object(BUCKET_NAME, random_name).put(Body=random_content)
    print(f"[CREATE] Created random object: {random_name}")
    return random_name

# 2. List all existing objects in the bucket
def list_objects():
    print("\n[LIST] Current objects in bucket:")
    for obj in bucket.objects.all():
        print(f" - {obj.key}")

# 3. Read the data of an existing object
def read_object(object_name):
    obj = s3.Object(BUCKET_NAME, object_name)
    content = obj.get()['Body'].read().decode('utf-8')
    print(f"\n[READ] Content of {object_name}: {content}")

# 4. Update an existing object
def update_object(object_name):
    new_content = "This is UPDATED content!"
    s3.Object(BUCKET_NAME, object_name).put(Body=new_content)
    print(f"\n[UPDATE] Object '{object_name}' has been updated.")

# 5. Remove an existing object
def delete_object(object_name):
    s3.Object(BUCKET_NAME, object_name).delete()
    print(f"\n[DELETE] Object '{object_name}' was removed.")

#Execution Flow
if __name__ == "__main__":
    try:
        obj_name = create_random_object()
        list_objects()
        read_object(obj_name)
        update_object(obj_name)
        read_object(obj_name)
        delete_object(obj_name)
        list_objects()

    except Exception as e:
        print(f"Error occurred: {e}. Please ensure MinIO is running.")
import boto3
#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='Your Access Key ID',
aws_secret_access_key='You Secret access key'
)
#Creating S3 Resource From the Session.

ACCESS_KEY_ID = ''
SECRET_ACCESS_KEY = ''
s3 = session.resource('s3', aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY)
#Create a Source Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
copy_source = {
'Bucket': 'your_source_bucket_name',
'Key': 'Object_Key_with_file_extension'
}
bucket = s3.Bucket('target_bucket_name')
bucket.copy(copy_source, 'target_object_name_with_extension')
# Printing the Information That the File Is Copied.
print('Single File is copied')
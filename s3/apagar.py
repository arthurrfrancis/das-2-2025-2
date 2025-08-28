import boto3

s3_client = boto3.resource('s3', region_name='us-east-1')

bucket = s3_client.Bucket('arthurfrancisco2003')

obj = bucket.Object('exemplo.txt')

obj.delete()
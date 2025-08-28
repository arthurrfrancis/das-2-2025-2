import boto3

s3_client = boto3.client('s3', region_name='us-east-1')

s3_client.create_bucket(Bucket='arthurfrancisco2003')

print("Bucket criado com sucesso!")
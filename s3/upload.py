import boto3

s3_client = boto3.client('s3', region_name='us-east-1')
s3_client.upload_file('./s3/exemplo.txt', 'arthurfrancisco2003', 'exemplo.txt')

print("Arquivo enviado com sucesso!")
import json
import boto3

def get_volume_id_from_arn(volume_arn):
    arn_parts = volume_arn.split(":")
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id
    

def lambda_handler(event, context):
    
    client = boto3.client('ec2')
    
    
    volume_arn = event["resources"][0]
    volume_id = get_volume_id_from_arn(volume_arn)
    
    print("Extracted volume ID:", volume_id)
    
    try:
        response = client.modify_volume(
            VolumeId=volume_id,
            VolumeType='gp3'
        )
        print("Volume modification successful:", response)
    except Exception as e:
        print("Error modifying volume:", e)
    
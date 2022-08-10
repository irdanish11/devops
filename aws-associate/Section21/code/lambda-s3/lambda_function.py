import json

def lambda_handler(event, context):
    print('S3 Event: ', event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
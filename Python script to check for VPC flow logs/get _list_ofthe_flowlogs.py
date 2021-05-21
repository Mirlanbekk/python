import boto3, json
from botocore.exceptions import ClientError

ec2 = boto3.resource("ec2")
ec2_client = boto3.client("ec2")

FlowLogId = ['fl-00c4625e4537f55af']

def get_flow_logs ():
    try:
        response=ec2_client.describe_flow_logs()
        for i in response['FlowLogs']:
            FlowLogId.append(i['FlowLogId'])
    except Exception as error:
        print(error)
    print("FlowLogId:", FlowLogId)
get_flow_logs()
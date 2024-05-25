import boto3

def handler(event, context):
    ec2 = boto3.resource('ec2')

    instance = ec2.create_instances(
        ImageId='ami-0e001c9271cf7f3b9',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    );
    instance_id = instance[0].id
    print(f"Instance {instance_id} is creating.")

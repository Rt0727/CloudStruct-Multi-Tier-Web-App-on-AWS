import boto3

def create_ec2_instance():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-xxxxxxxxxxxxxxxxx',  # Replace with a valid AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='your-key-pair',
    )[0]
    print(f"EC2 instance {instance.id} created.")
    return instance

def stop_ec2_instance(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    instance.stop()
    print(f"EC2 instance {instance_id} stopped.")

if __name__ == '__main__':
    # Example usage
    create_ec2_instance()
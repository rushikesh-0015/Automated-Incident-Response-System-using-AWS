import boto3

asg = boto3.client('autoscaling')

def lambda_handler(event, context):
    response = asg.set_desired_capacity(
        AutoScalingGroupName='My-ASG',
        DesiredCapacity=2,
        HonorCooldown=False
    )

    print("Scaled ASG to 2 instances")

    return response

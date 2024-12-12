import boto3

def create_iam_role():
    iam = boto3.client('iam')
    role = iam.create_role(
        RoleName='YourRoleName',
        AssumeRolePolicyDocument='{}',  # Add appropriate policy document
    )
    print(f"IAM Role {role['Role']['RoleName']} created.")

def attach_policy_to_role(role_name):
    iam = boto3.client('iam')
    iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
    )
    print(f"Policy attached to role {role_name}.")

if __name__ == '__main__':
    create_iam_role()
    attach_policy_to_role('YourRoleName')
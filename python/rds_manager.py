import boto3

def create_rds_instance():
    rds = boto3.client('rds')
    response = rds.create_db_instance(
        DBName='yourdb',
        DBInstanceIdentifier='yourdbinstance',
        AllocatedStorage=20,
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        MasterUsername='admin',
        MasterUserPassword='password',
        VpcSecurityGroupIds=['your-security-group-id'],
        DBSubnetGroupName='your-db-subnet-group',
    )
    print(f"RDS instance {response['DBInstance']['DBInstanceIdentifier']} created.")

if __name__ == '__main__':
    create_rds_instance()
#!/bin/bash

# Update EC2 instance with the latest application code
scp -i "your-key.pem" -r ./app/* ec2-user@${EC2_PUBLIC_IP}:/var/www/html/

# Restart application server
ssh -i "your-key.pem" ec2-user@${EC2_PUBLIC_IP} 'sudo systemctl restart apache2'

# Output success message
echo "Deployment to EC2 successful!"
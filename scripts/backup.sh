#!/bin/bash

# Define backup location and date format
BACKUP_DIR="./backups"
DATE=$(date +\%Y-\%m-\%d_\%H-\%M-\%S)
BACKUP_FILE="$BACKUP_DIR/web-app-backup-$DATE.tar.gz"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Backup EC2 server filesystem
tar -czf $BACKUP_FILE --exclude=$BACKUP_DIR /etc /var /home /usr

# Backup RDS database
aws rds create-db-snapshot --db-instance-identifier app-db --db-snapshot-identifier "snapshot-$DATE"

echo "Backup completed: $BACKUP_FILE"
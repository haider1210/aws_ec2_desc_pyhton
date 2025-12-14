# =====================================
# AWS EC2 CLI – Setup & Execution Guide
# =====================================

### 1. Update system packages
sudo apt update

### 2. Install Python and required tools
sudo apt install -y python3 python3-venv python3-pip

### 3. Install AWS CLI
sudo apt install -y awscli

### Verify AWS CLI installation
aws --version

## 4. Create Python virtual environment
python3 -m venv venv

## 5. Activate virtual environment
source venv/bin/activate

### 6. Upgrade pip
pip install --upgrade pip

### 7. Install project dependencies
pip install -r requirements.txt

### =====================================
### Run EC2 Operations
### =====================================

### Start EC2 instance(s)
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation start \
  --instance_id i-xxxxxxxx i-yyyyyyyy

### Stop EC2 instance
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation stop \
  --instance_id i-xxxxxxxx

### Terminate EC2 instance
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation terminate \
  --instance_id i-xxxxxxxx


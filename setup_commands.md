# AWS EC2 CLI – Setup & Execution Guide

## 1. Update System Packages

```bash
sudo apt update
```

## 2. Install Python and Required Tools

```bash
sudo apt install -y python3 python3-venv python3-pip
```

## 3. Install AWS CLI

```bash
sudo apt install -y awscli
```

### Verify AWS CLI Installation

```bash
aws --version
```

## 4. Create Python Virtual Environment

```bash
python3 -m venv venv
```

## 5. Activate Virtual Environment

```bash
source venv/bin/activate
```

## 6. Upgrade pip

```bash
pip install --upgrade pip
```

## 7. Install Project Dependencies

```bash
pip install -r requirements.txt
```

# =====================================

# Run EC2 Operations

# =====================================

## Start EC2 Instance(s)

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation start \
  --instance_id i-xxxxxxxx i-yyyyyyyy
```

## Stop EC2 Instance

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation stop \
  --instance_id i-xxxxxxxx
```

## Reboot EC2 Instance

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation reboot \
  --instance_id i-xxxxxxxx
```

## Terminate EC2 Instance

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation terminate \
  --instance_id i-xxxxxxxx
```

## Notes

* Multiple instance IDs can be provided as space-separated values.
* Ensure the Python virtual environment is activated before running the script.
* Logs are automatically generated in `ec2_operations<timestamp>.log`.
* The script prints EC2 instance details in JSON format with Instance ID, Name, S

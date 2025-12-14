````markdown
# AWS EC2 CLI – Setup & Execution Guide

This guide explains how to set up your system, install dependencies, and run the Python script to
manage AWS EC2 instances using AWS CLI.

````
## 1. System Setup

### Update system packages
```bash
sudo apt update
```

### Install Python and required tools

```bash
sudo apt install -y python3 python3-venv python3-pip
```

### Install AWS CLI

```bash
sudo apt install -y awscli
```

### Verify AWS CLI installation

```bash
aws --version
```

---

## 2. Python Environment Setup

### Create a Python virtual environment

```bash
python3 -m venv venv
```

### Activate the virtual environment

```bash
source venv/bin/activate
```

### Upgrade pip

```bash
pip install --upgrade pip
```

```bash
pip install sh
```

## cli command example

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --instance_id i-867ghjgxxx 
```


## 4. Output

The script prints EC2 instance details in JSON format:

```json
[
  {
    "InstanceId": "i-0abc12345",
    "Name": "MyEC2test1",
    "State": "running",
    "Private IP": "10.0.0.15",
    "Public IP": "13.233.xxx.xxx"
  },
  {
    "InstanceId": "i-0abc9876",
    "Name": "MyEC2test2",
    "State": "stopped",
    "Private IP": "10.0.0.20",
    "Public IP": "N/A"
  }
]
```

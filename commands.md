Here’s a complete, professional **`commands.md`** file with setup, dependencies, execution, and examples—all in one:

````markdown
# AWS EC2 CLI – Setup & Execution Guide

This guide explains how to set up your system, install dependencies, and run the Python script to manage AWS EC2 instances using AWS CLI.

---

## 1. System Setup

### Update system packages
```bash
sudo apt update
````

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

### Install project dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Running the EC2 Script

The Python script supports multiple operations: **start**, **stop**, **terminate**, and **reboot** EC2 instances. You can provide one or more instance IDs.

### Run script for all instances

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation start
```

### Run script for specific instance(s)

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation stop \
  --instance_id i-xxxxxxxx i-yyyyyyyy
```

### Terminate instance(s)

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation terminate \
  --instance_id i-xxxxxxxx
```

### Reboot instance(s)

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation reboot \
  --instance_id i-xxxxxxxx
```

---

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

---

## 5. Notes

* Make sure the AWS CLI has the correct access rights for the provided credentials.
* You can provide multiple instance IDs separated by space for batch operations.
* Logging is enabled and saved with timestamps in the current directory.
* Ensure the virtual environment is activated before running the script.

```

If you want, I can also **create a matching `README.md`** with long project description, features, and reference this `commands.md` for instructions so the repo looks professional.  

Do you want me to do that next?
```

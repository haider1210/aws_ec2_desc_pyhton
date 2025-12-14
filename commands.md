# AWS EC2 CLI – Setup & Execution Guide

This guide explains how to set up your system, install dependencies, and run the Python script to
manage AWS EC2 instances using AWS CLI on both Linux and Windows.

---

## 1. System Setup (Linux)

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

## 1. System Setup (Windows PowerShell)

### Install Python

Download from [Python.org](https://www.python.org/downloads/) and install.

### Install AWS CLI

Download the MSI installer from [AWS CLI](https://aws.amazon.com/cli/) and install.

### Verify AWS CLI

```powershell
aws --version
```

---

## 2. Python Environment Setup (Linux)

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

### Install required Python packages

```bash
pip install -r requirements.txt
pip install sh
```

---

## 2. Python Environment Setup (Windows PowerShell)

### Create virtual environment

```powershell
python -m venv venv
```

### Activate virtual environment

```powershell
.\venv\Scripts\activate
```

### Upgrade pip

```powershell
pip install --upgrade pip
```

### Install required Python packages

```powershell
pip install -r requirements.txt
pip install sh
```

---

## 3. Running the Script

The script supports multiple EC2 operations: **start**, **stop**, **terminate**, **reboot**. You can pass one or more instance IDs.

### Run script for specific instance (Linux)

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation start \
  --instance_id i-867ghjgxxx
```

### Run script for specific instance (Windows PowerShell)

```powershell
python create_ec2.py `
  --key_id <AWS_ACCESS_KEY_ID> `
  --access_key <AWS_SECRET_ACCESS_KEY> `
  --region ap-south-1 `
  --operation start `
  --instance_id i-867ghjgxxx
```

### Run script for multiple instances

```bash
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation stop \
  --instance_id i-xxxxxxxx i-yyyyyyyy
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

* Ensure AWS credentials have the necessary permissions.
* Multiple instance IDs can be provided separated by spaces.
* The virtual environment must be activated before running the script.
* Logs are created in the current directory with timest

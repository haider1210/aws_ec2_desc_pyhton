Here’s a **short, single `README.md`** covering Linux & Windows, setup, usage, and output:

````markdown
# AWS EC2 CLI – Python Script

This project retrieves AWS EC2 instance details  using Python and AWS CLI. It authenticates via environment variables, executes AWS CLI commands, and prints EC2 metadata (ID, Name, State, Private/Public IP).

---

## Setup

### Linux
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip awscli
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install sh
````

### Windows

```powershell
# Install Python & AWS CLI manually
python -m venv venv
.\venv\Scripts\Activate
pip install --upgrade pip
pip install sh
```

---

## Usage

### Run for all instances

```bash
python create_ec2.py --key_id <KEY> --access_key <SECRET> --region <REGION> --operation start
```

### Run for specific instances

```bash
python create_ec2.py --key_id <KEY> --access_key <SECRET> --region <REGION> --operation stop --instance_id i-123 i-456
```

---

## Output

```json
[
  {
   "InstanceId":"i-0abc123",
   "Name":"MyEC2",
   "State":"running",
   "Private IP":"10.0.0.15",
   "Public IP":"13.233.xxx.xxx"
  },
  {
   "InstanceId":"i-0abc456",
   "Name":"TestEC2",
   "State":"stopped",
   "Private IP":"10.0.0.20",
   "Public IP":"N/A"
  }
]
```


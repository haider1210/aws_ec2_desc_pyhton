# -----------------------------
# SYSTEM UPDATE
# -----------------------------
sudo apt update

# -----------------------------
# INSTALL PYTHON
# -----------------------------
sudo apt install python3 python3-venv python3-pip -y

# -----------------------------
# INSTALL AWS CLI
# -----------------------------
sudo apt install awscli -y

# Verify AWS CLI installation
aws --version

# -----------------------------
# CREATE VIRTUAL ENVIRONMENT
# -----------------------------
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# -----------------------------
# UPGRADE PIP
# -----------------------------
pip install --upgrade pip

# -----------------------------
# INSTALL PYTHON DEPENDENCIES
# -----------------------------
pip install -r requirements.txt

# -----------------------------
# RUN SCRIPT (ALL INSTANCES)
# -----------------------------
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation start \
  --instance_id i-xxxxxxxx i-yyyyyyyy

# -----------------------------
# RUN SCRIPT (SINGLE INSTANCE)
# -----------------------------
python3 create_ec2.py \
  --key_id <AWS_ACCESS_KEY_ID> \
  --access_key <AWS_SECRET_ACCESS_KEY> \
  --region ap-south-1 \
  --operation stop \
  --instance_id i-xxxxxxxx

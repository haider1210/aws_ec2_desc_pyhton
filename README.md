# AWS EC2 Details Using Python & AWS CLI

This project fetches AWS EC2 instance details using Python and AWS CLI.
It authenticates via environment variables, runs AWS CLI commands, and
parses the output to display useful EC2 information.

## Features
- AWS authentication using environment variables
- Fetch EC2 instance details
- Filter by Instance ID
- Shows Instance ID, Name, State, Private IP, Public IP
- Structured logging and error handling

# AWS EC2 Details Using Python & AWS CLI

This project fetches AWS EC2 instance details using Python and AWS CLI.

## Setup & Usage
Refer to `commands.txt` for full installation and execution steps.

## Output
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
        "Name": "MyEC2test",
        "State": "stoped",
        "Private IP": "10.0.0.15",
        "Public IP": "N/A"
    }
  
]

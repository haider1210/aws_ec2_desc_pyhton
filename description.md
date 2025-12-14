Here’s a more detailed and professional version for your description:

---

This project is designed to simplify the retrieval and management of AWS EC2 instance details using **Python** in combination with the **AWS CLI**. The script automates the process of authenticating with AWS using environment variables, executing EC2-related AWS CLI commands, and parsing the resulting JSON output to extract meaningful instance metadata.

Key capabilities include:

* **AWS Authentication:** Automatically sets environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`) for secure access to your AWS account without hardcoding credentials in the script.
* **Instance Metadata Extraction:** Fetches and displays crucial EC2 instance information such as:

  * **Instance ID:** Unique identifier of the EC2 instance
  * **Name:** Human-readable name assigned via tags
  * **State:** Current lifecycle

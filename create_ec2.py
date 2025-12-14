import os
import json
import argparse
import datetime
import sys
import sh
import logging

out =[]
# --------------------------------------------------
# AUTHENTICATION
# --------------------------------------------------
def authentication(params):
    """
    Sets AWS credentials as environment variables
    so that AWS CLI can automatically pick them up.
    """
    try:
        logging.info("Authentication started")

        # Validate required keys exist
        required_keys = ["key_id", "access_key", "region"]
        for key in required_keys:
            if not params.get(key):
                raise ValueError(f"Missing required parameter: {key}")

        # Set AWS environment variables (temporary for this process)
        os.environ["AWS_ACCESS_KEY_ID"] = params["key_id"]
        os.environ["AWS_SECRET_ACCESS_KEY"] = params["access_key"]
        os.environ["AWS_DEFAULT_REGION"] = params["region"]

        # Disable AWS CLI pager (prevents hanging output)
        os.environ["AWS_PAGER"] = ""

        logging.info("Authentication successful")

    except Exception as e:
        # .exception logs full traceback (very useful for debugging)
        logging.exception("Authentication failed")
        sys.exit(1)


# --------------------------------------------------
# HELPER: GET INSTANCE NAME FROM TAGS
# --------------------------------------------------
def get_instance_name(tags):
    """
    Extracts EC2 instance Name from Tags list.
    """
    try:
        if not tags:
            return "N/A"

        for tag in tags:
            if tag.get("Key") == "Name":
                return tag.get("Value", "N/A")

        return "N/A"

    except Exception:
        logging.warning("Failed to parse instance tags")
        return "N/A"


# --------------------------------------------------
# DESCRIBE EC2 INSTANCES
# --------------------------------------------------
def describe_instances(params, out):
    """
    Calls AWS CLI to describe EC2 instances and
    extracts required fields.
    """
    try:
        logging.info("Describing EC2 instances")

        # Run AWS CLI command
        if params["instance_id"]:
            logging.info(f"Filtering by Instance ID: {params['instance_id']}")
            result = sh.aws("ec2", "describe-instances",
                           "--instance-ids", params["instance_id"])
        else:
            result = sh.aws("ec2", "describe-instances")

        # Convert CLI output to Python dictionary
        data = json.loads(str(result))
        

        if "Reservations" not in data:
            logging.warning("No reservations found in AWS response")
            return

        found = False

        for reservation in data["Reservations"]:
            for instance in reservation.get("Instances", []):

                instance_id = instance.get("InstanceId", "N/A")

                # Filter by instance_id if provided
                if params.get("instance_id") and instance_id != params["instance_id"]:
                    continue

                found = True

                instance_info = {
                    "InstanceId": instance_id,
                    "Name": get_instance_name(instance.get("Tags")),
                    "State": instance.get("State", {}).get("Name", "N/A"),
                    "Private IP": instance.get("PrivateIpAddress", "N/A"),
                    "Public IP": instance.get("PublicIpAddress", "N/A")
                }

                out.append(instance_info)

                logging.info(
                    f"Found instance {instance_id} "
                    f"({instance_info['State']})"
                )

        if not found:
            logging.warning("No matching EC2 instance found")
            print("No matching instance found")

    except json.JSONDecodeError:
        logging.exception("Failed to parse AWS CLI JSON output")

    except sh.ErrorReturnCode as e:
        logging.error(f"AWS CLI command failed: {e}")

    except Exception:
        logging.exception("Unexpected error while describing instances")


# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------
def main():
    """
    Entry point of the script.
    Parses arguments, sets logging,
    authenticates, and fetches EC2 details.
    """
    try:
        parser = argparse.ArgumentParser(
            description="Fetch EC2 instance details using AWS CLI"
        )

        # Authentication arguments
        parser.add_argument("--key_id", required=True, help="AWS Access Key ID")
        parser.add_argument("--access_key", required=True, help="AWS Secret Access Key")
        parser.add_argument("--region", required=True, help="AWS Region")

        # Optional filter
        parser.add_argument("--instance_id", help="EC2 Instance ID to filter")

        args = parser.parse_args()
        params = vars(args)

        # Setup logging
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        logging.basicConfig(
            filename=f"ec2_details_{timestamp}.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - line %(lineno)d - %(message)s",
        )

        logging.info("Script execution started")
        authentication(params)
        describe_instances(params, out)

        logging.info("Final EC2 output generated")
        logging.info(json.dumps(out, indent=4))

        # Print final output to terminal
        print(json.dumps(out, indent=4))

    except Exception:
        logging.exception("Fatal error in main execution")
        sys.exit(1)


# --------------------------------------------------
# SCRIPT ENTRY POINT
# --------------------------------------------------
if __name__ == "__main__":
    main()

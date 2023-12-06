# AWS Lambda EBS Snapshot Cleanup

This AWS Lambda function is designed to clean up EBS snapshots by deleting those that are not attached to any volume or are associated with volumes that are not attached to running instances.

## Prerequisites

Before deploying and using this Lambda function, make sure you have the following:

- An AWS account with the necessary permissions to manage EC2 and EBS resources.
- AWS CLI configured with the appropriate credentials.

## Deployment

1. Clone this GitHub repository:

   ```bash
   git clone https://github.com/yourusername/your-repository.git

2. Navigate to the Lambda function directory:

    ```bash
    cd your-repository
    ```

3. Zip the Lambda function code:

    ```bash
    zip -r lambda_function.zip lambda_function.py
    ```
Upload the Lambda function code to your AWS Lambda function.

Configure the Lambda function trigger as needed (e.g., CloudWatch Events).

## Configuration
Ensure that the Lambda function has the necessary IAM role attached with the following permissions:

* __ec2:DescribeSnapshots__
* __ec2:DescribeInstances__
* __ec2:DescribeVolumes__
* __ec2:DeleteSnapshot__

## Usage
The Lambda function will automatically run based on the configured trigger (e.g., CloudWatch Events). Monitor CloudWatch Logs for execution details.
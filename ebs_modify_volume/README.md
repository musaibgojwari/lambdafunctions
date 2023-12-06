# Lambda Function: Modify EBS Volume Type

This Lambda function modifies the type of an Amazon Elastic Block Store (EBS) volume to 'gp3'. It extracts the volume ID from the provided EBS volume ARN.

## Lambda Function Setup

Follow these steps to set up the Lambda function:

1. **AWS Lambda Console:**
   - Navigate to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).

2. **Create a Function:**
   - Click on "Create function."
   - Choose "Author from scratch."
   - Provide a name for your function (e.g., `ModifyEBSVolume`).
   - Choose the runtime as "Python" (ensure it matches the Python version used in your code).
   - In the "Function code" section, copy and paste your Python code.

## Trigger Setup

To automatically trigger this Lambda function upon the creation of a new EBS volume, follow these steps:

1. **CloudWatch Events:**
   - Navigate to the [CloudWatch Console](https://console.aws.amazon.com/cloudwatch/).
   - In the left navigation pane, choose "Rules" under "Events."

2. **Create Rule:**
   - Click on "Create Rule."
   - Choose "Event Source" as "Event Source Type."
   - Under "Service Name," select "EC2."
   - For "Event Type," select "EC2 CreateVolume API Call."
   - Click "Add Target" and select the Lambda function you want to trigger (this Lambda function).

3. **Configure Details:**
   - Click "Configure details."
   - Provide a name and description for your rule.
   - Optionally, add tags.

4. **Create Rule:**
   - Click "Create rule" to create the rule and link it to your Lambda function.

## Usage

1. **Lambda Function:**
   - The Lambda function is now configured to be triggered automatically when a new EBS volume is created in the AWS environment.
   - It extracts the volume ID from the ARN included in the event.
   - The EBS volume type is modified to 'gp3' using the `modify_volume` API.

2. **IAM Permissions:**
   - Ensure that the IAM role associated with the Lambda function has the necessary permissions.
   - Add the following permission to your IAM role:

     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Effect": "Allow",
                 "Action": "ec2:ModifyVolume",
                 "Resource": "*"
             }
         ]
     }
     ```

   - This permission allows the Lambda function to modify any EBS volume. Adjust the `Resource` field for specific volume restrictions.

3. **Logging:**
   - The Lambda function logs the extracted volume ID, successful volume modification, or any errors encountered during the process.

## Notes

- It's recommended to follow the principle of least privilege, granting only the necessary permissions for your Lambda function.
- Replace the generic IAM policy with specific resource ARNs if you want to restrict the permissions to specific EBS volumes.
- Review the CloudWatch Logs for detailed information about Lambda function execution.

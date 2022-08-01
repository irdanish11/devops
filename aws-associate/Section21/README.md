## 21.1 Serverless:
* Serverless is a new paradigm in which the developes don't have to manage servers.
* Serverless doesn't mean that there are no servers but it means that we developers don't have to manage or provision them.
* Serverless in AWS:
  - AWS Lambda
  - DynamoDB
  - AWS Cognito
  - AWS API Gateway
  - AWS S3
  - AWS SNS & SQS
  - AWS Kinesis Data Firehose
  - AWS Aurora
  - Step Functions
  - Fargate

## 21.2 AWS Lambda Overview:
#### Amazon EC2: 
- Virtual Servers in the Cloud.
- Limited by CPU and RAM.
- Continuously Running.
- Scaling means manual intervention.
#### AWS Lambda:
- Virtual Functions - No servers to manage
- Limited by time - short time execution (15 minutes).
- Run on demand.
- Scaling is automated.
- Pay per request and compute time.
- Free tier of 1,000,000 AWS Lambda requests and 400,000 GBs of compute time.
- Integrated with the whole of AWS suite of services.
- Integrated with many programming languages.
- Easy monitoring through AWS CloudWatch.
- Easy to get more resources per function (up to 10 GB of RAM).
- Increasing RAM will also improve CPU and network.

#### AWS Lambda Language Support:
- Node.js
- Python
- Java (Java 8 compatible)
- Golang
- Custom Runtime API
- Lambda Container Image
  * The container image must implement the Lambda Runtime API.
  * ECS/Fargate is preferred for running arbitrary docker images.

#### AWS Lambda Integrations (Main Ones):
- API Gateway
- Kinesis
- DynamoDB
- S3
- CloudFront
- CloudWatch Events - EventBridge
- CloudWatch logs
- SNS
- SQS
- Cognito
- And many others

#### Example: Serverless Thumbnail Creation:
- Whenever an image is uploaded to S3, it triggers the AWS Lambda function that creates the thumbnail.
- Then AWS Lambda creates the thumbnail and pushes to another S3.
- AWS Lambda also pushes some metadata to DynamoDB.
- As shown below:

<p align="center">
<img src="images/serverless-thumbnail.png" width="500">
</p>

#### Example: Serverless CRON Job:
- Let's we set up an EventBridge Rule that would be triggered every one hour and would be integrated with AWS Lambda function that perform a task
- As shown below:

<p align="center">
<img src="images/serverless-cron-job.png" width="300">
</p>

#### AWS Lambda Pricing:
- Pay per calls:
  * First 1,000,000 requests are free.
  * $0.20 per 1 million requests thereafter ($0.0000002 per request).
- Pay per duration (in increment of 1ms):
  * 400,000 GBs of compute per month if free.
  * That means 400,000 seconds if RAM is 1GB.
  * And 3,200,000 seconds if RAM is 128MB.
  * After that $1 for 600,000 GBs.

## 21.3 Lambda - Synchronous Invocation:
- We are doing synchronous invocations when we are invoking lambda functions from CLI, SDL, API Gateway, Application Load Balancer.
  * Synchronous means we are waiting for results and then the results will be returned.
  * Error handling must happen on client side (retries, exponential backoff etc).
- Lambda - Synchronous Invocation Services:
  * User Invoked: 
    - Elastic Load Balancing (Application Load Balancer)
    - Amazon API Gateway
    - Amazon CloudFront(Lambda@Edge)
    - Amazon S3 Batch
  * Service Invoked:
    - Amazon Cognito
    - AWS Step Functions
  * Other Services: 
    - Amazon Lex
    - Amazon Alexa
    - Amazon Kinesis Data Firehose
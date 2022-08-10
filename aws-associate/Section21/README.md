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

- We can make synchronous invocation to our lambda function by using the following command:
```shell
aws lambda invoke --function-name demo-lambda --cli-binary-format raw-in-base64-out --payload '{"key1": "value-1", "key2": "value2", "key3":"value-3"}' response.json
```

### 21.4 Lambda and Application Load Balancer:
* If we want to use lambda function through the internet then we need to expose our lambda function as HTTP/HTTPS endpoint.
* There are two ways we can do this:
  - We can use the Application Load Balancer (ALB) to expose our lambda function as HTTP/HTTPS endpoint.
  - Or we can use API Gateway to expose our lambda function as HTTP/HTTPS endpoint.
* To make lambda function work it must be registered in a `target group`.

<p align="center">
<img src="images/lambda-alb1.png" width="500">
</p>

* Client will be sending HTTP/HTTPS requests to our ALB, and our ALB will be invoking our lambda function synchronously in a target group.
* Synchronously because we are waiting for the lambda function to get back to the ALB, which will in turn send the response to the client.
* How does ALB converts an HTTP/HTTPS request to a lambda invocation?
* From ALB to lambda the HTTP/HTTPS is get transformed to a JSON payload.
* The query string parameters, the headers, and the body all of them are converted into key value pair.
* Lambda function will send a json payload to the ALB and ALB will convert it into HTTP/HTTPS response. The lambda function needs to include the status code, status description, headers, and body and flag of `isBase64Encoded` in the response.
* ALB can support multi-header values, and its an ALB setting.
* If we pass in multiple headers with same value or query string with the same values, then we can enable the multi-header setting.
* Then the HTTP headers and query string parameters that are sent with multiple values are shown as arrays within the AWS Lambda event and response object.

<p align="center">
<img src="images/lambda-alb2.png" height="500">
</p>

### 21.5 Lambda@Edge:
* It is another type of synchronous invocation. 
* Let's say we have deployed a CDN using the CloudFront service.
* What if we wanted to run a lambda function globally alongside each edge location.
* Or how we can implement request filtering before reaching our application?
* For this we can use Lambda@Edge, we'll deploy Lambda functions alongside our CloudFront edge locations.
* Why we want to do this?
  - Build more responsive applications.
  - We don't need to manage servers, and Lambda is deployed globally.
  - Customize the CDN content.
  - Pay only what we use.

* We can use Lambda to change the CloudFront requests and responses.

<p align="center">
<img src="images/lambda@edge1.png" width="500">
</p>

* There are four types of lambda functions at the edge.
* In the CloudFront we have four scenarios where we can use Lambda@Edge:
  - After CloudFront receives the request from a viewer (viewer request).
  - Before CloudFront forwards the request to the origin (origin request).
  - After CloudFront receives the response from the origin (origin response).
  - Before CloudFront forwards the response to the viewer (viewer response).
* We can also send a response to the viewers without ever sending a request to the origin, by using just viewer request and viewer response lambda function.

* ***Lambda@Edge Global Application:***
  - Let's say our website is statically hosted on S3 in the HTML form.
  - The user will visit this and will ask for some client side JS to do API request to CloudFront.
  - Then CloudFront will trigger our Lambda@Edge function, which is running globally alongside our edge locations. 
  - Then the lambda function maybe querying data from DynamoDB.

* ***Lambda@Edge Use Cases:***
  - WebSecurity and Privacy.
  - Dynamic Web Applications at the edge. 
  - Search Engine Optimization.
  - Intelligently Route Across Origins and Data Centres.
  - Bot Mitigation at teh Edge.
  - Real-Time image transformations.
  - A/B Testing.
  - User Authorization and Authentication.
  - User Prioritization.
  - Using Tracking and Analysis.


### 21.6 Lambda - Asynchronous Invocations:
* These are the services that will invoke our Lambda function behind the scenes e.g. S3, SNS, CloudWatch Events etc.

<p align="center">
<img src="images/lambda-async1.png" width="500">
</p>

* Let's say we have S3 bucket and a S3 event notification for new files and this will go into lambda service.
* Because this async and the event will be placed in an internal `Event Queue`.
* Our lambda function will be reading of from that `Event Queue`.
* Then lambda function will try to process these events but if somehow thing goes wrong i.e. an error occurs, lambda function will automatically retry.
* There will be three tries in total:
  - 1st retry will be immediately.
  - 2nd retry will be after 1 minute.
  - 3rd retry will be after 2 minutes.
* If the retries happen that means our lambda function will process the same event multiple times.
* We need to make sure that our lambda function is idempotent (idempotent means in case of retries the result is same).
* If the function is retries then we will see duplicate log entries in CloudWatch Logs and our Lambda function will retry over and over again.
* So to solve this problem we can define a Dead Letter Queue (DLQ) after the retries the Lambda function will send the event to the DLQ (i.e. SQS or SNS) for further processing later on.
* Asynchronous invocations allow us to speed the results if we don't need to wait for the result (e.g. 1000 files are processed at the same time). So we wait for all the 1000 files to be processed in parallel instead of each individual result.
* ***Lambda - Asynchronous Invocation - Services:***
  - S3.
  - SNS.
  - CloudWatch Events/EventBridge.
  - AWS CodeCommit (CodeCommitTrigger: new branch, new commit, new push).
  - AWS CodePipeline (invoke Lambda function during the pipeline, Lambda must callback).
  - Amazon CloudWatch Logs (log processing)
  - Amazon Simple Email Service
  - AWS CloudFormation
  - AWS Config
  - AWS IoT
  - AWS IoT Events

### 21.7 Lambda and CloudWatch Events/EventBridge:
* There are two ways to invoke Lambda functions from EventBridge:
* The first is to do a serverless cron job or a rate and for that we are going to create and EventBridge rule.
* Let's say it will trigger our lambda function every 1 hour to perform our task.

<p align="center">
<img src="images/lambda-eventbridge.png" width="500">

* The second way is that we can create Rule with an event pattern e.g. we can create CodePipeline EventBridge rule.
* Every time CodePipeline state changes, and on state changes it will invoke the lambda function to perform the task.


### 21.8 Lambda and S3 Event Notifications:
* Integrating S3 Events with AWS Lambda.
* There is an event notification whenever:
  - S3:ObjectCreated
  - S3:ObjectRemoved
  - S3:ObjectRestore
  - S3:ObjectReplicated
  - and others
* Object name filtering is possible either by prefix or by suffix (*.jpg).
* The use case can be generate thumbnails of images uploaded to S3.

<p align="center">
<img src="images/lambda-s3-event-notification.png" height="500">
</p>

* So we have our events into S3 and S3 can send those events to three things:
  - SNS and from SNS we can send those to multiple SQS using fan-out pattern.
  - Or we can send them to an SQS Queue and have lambda function read directly from the SQS Queue.
  - Or we can have S3 event notification directly invoke our lambda function and this would be asynchronous invocation, and in case of errors we can setup a dead letter queue.

* These S3 event notifications are normally delivered in seconds but sometimes can take a minute or longer. 
* If we want to make sure that we don't miss any event notification then we need to enable versioning for our bucket, because if two writes are made at the same time, it is possible that only a single event notification will be sent.
* We have a simple use case of S3 Event Pattern for MetaData Sync.

<p align="center">
<img src="images/lambda-s3-event-notification2.png">
</p>

* An S3 bucket will have a new file event to lambda function and then the lambda function will process the file and put the metadata into DynamoDB Table or even a Table in RDS Database.



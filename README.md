# Gamestop Product Availibilty

This project will include the following AWS services:
*  AWS Lambda
*  DynamoDB
*  SNS
*  EventBridge (Cloudwatch Events)
*  Amazon S3

We will also make use of Serverless Framework to deploy the lambda function along with all the necessary its aws resouces. Below is a simpe diagram of the infrastructure. 

![Serverless-GameStop-In-Stock-Notification](https://user-images.githubusercontent.com/47754258/138712064-0cd1924e-8d44-4408-ad89-d424065a7f44.png)


Make sure you have serverless installed locally on your machine. 

https://www.serverless.com/framework/docs/getting-started/

$ serverless --version
Framework Core: 2.55.0 (standalone)
Plugin: 5.4.3
SDK: 4.2.6
Components: 3.15.1

To make use of the 'requests' library being used in our lambda function we will need to run the following before we can deploy. 

* serverless install plugin serverless-python-requirements

Make sure you updated the email address amd phone number in the serverless.yml file. 

Once you have your keys exported as environment variables you can now run 

* sls deploy

You can see the cloudformation stack being launched and all the resources being deployed. 




# Gamestop Product Availability

Have you ever missed out on a product online and wished you would've been notified as soon as it became available for purchase? Well, wait no more, this simple project will scrape a website of your choice and notify you once its available. 

This project will include the following AWS services:
* AWS Lambda
* DynamoDB
* SNS
* EventBridge (Cloud watch Events)
* Amazon S3

We will also make use of Serverless Framework to deploy the lambda function along with all the necessary aws resources. Below is a simple diagram of the infrastructure. 

![Serverless-GameStop-In-Stock-Notification](https://user-images.githubusercontent.com/47754258/138712064-0cd1924e-8d44-4408-ad89-d424065a7f44.png)


Make sure you have server less installed locally on your machine. 

https://www.serverless.com/framework/docs/getting-started/

$ server less --version
Framework Core: 2.55.0 (standalone)
Plugin: 5.4.3
SDK: 4.2.6
Components: 3.15.1

To make use of the 'requests' library being used in our lambda function we will need to run the following before we can deploy. 

* server less install plugin serverless-python-requirements

Make sure you updated the email address amd phone number in the server less.yml file. 

Once you have your keys exported as environment variables you can now run 

* sls deploy

You can see the cloud formation stack being launched and all the resources being deployed. 

# Test Page

There is an html page that was added to let you control the html content and test your code is working as expected.  This static page is being hosted on s3 bucket.  


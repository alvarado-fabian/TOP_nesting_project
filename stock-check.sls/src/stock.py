import requests
from datetime import datetime
import time
import random
import boto3
import os

def publish(ps5_name):
    arn = os.getenv('ARN')
    sns_client = boto3.client( 'sns', region_name=os.getenv('REGION') )
    response = sns_client.publish(
        TopicArn=arn, Message=" The item is finally in stock! Go grab it as ASAP! " + ps5_name )


def stock_check(event, context):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'authority': 'www.bestbuy.com'
        }
    items = [
        {
        'item_url': 'https://www.gamestop.com/consoles-hardware/playstation-5/consoles/products/playstation-5-digital-edition/229026.html',
        'item_name': "PlayStation 5 Digital Edition Console", 
        'search_string': 'Unavailable'
        }, 
        {
        'item_url': 'https://www.gamestop.com/consoles-hardware/playstation-5/consoles/products/playstation-5/229025.html',
        'item_name': "PlayStation 5 Console",  
        'search_string': 'Unavailable'
        }, 
        {
        'item_url': 'http://gamestop-static-website-test-12345.com.s3-website-us-east-1.amazonaws.com',
        'item_name': "Test Page",  
        'search_string': 'Unavailable'
        }    
    ]
    for item in items:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        url = item['item_url']
        name = item['item_name']
        search_string = item['search_string']
        result = requests.get(url, headers=headers)
        result = (result.content.decode())
        search_result = result.find(search_string)
        if search_result != -1:
            print(name +" Out of Stock!")
            dynamodb = boto3.resource('dynamodb', region_name=os.getenv('REGION'))
            table = dynamodb.Table(os.getenv('STATE_TBL_NAME'))
            table.put_item(
                Item={
                    'ConsoleName': name ,
                    'Status': 'Out Of Stock',
                    'Time': current_time
                }
            )
        else:
            print(name + " is available - will notify! " + url)
            publish(name + " " + url )
            dynamodb = boto3.resource('dynamodb', region_name=os.getenv('REGION'))
            table = dynamodb.Table(os.getenv('STATE_TBL_NAME'))
            table.put_item(
                Item={
                    'ConsoleName': name ,
                    'Status': 'In Stock',
                    'Time': current_time
                }
            )
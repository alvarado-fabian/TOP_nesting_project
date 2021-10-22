import requests
from datetime import datetime
import time
import random
import boto3
import os

def publish(ps5_name):
    arn = "arn:aws:sns:us-east-1:891431751772:PS5-IN-STOCK"
    sns_client = boto3.client( 'sns', region_name="us-east-1" )
    response = sns_client.publish(
        TopicArn=arn, Message=" It's in Stock! Go Grab it! " + ps5_name )


# global vars
is_available = 0
attempts = 0

# update header accordingly
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
        'item_url': 'https://www.gamestop.com/consoles-hardware/playstation-5/gaming-accessories/controllers/products/sony-dualsense-wireless-controller-midnight-black/297428.html',
        'item_name': "Sony DualSense Wireless Controller Midnight Black",  
        'search_string': 'Unavailable'
        }
    ]
for item in items:
    url = item['item_url']
    name = item['item_name']
    search_string = item['search_string']
    result = requests.get(url, headers=headers)
    result = (result.content.decode())
    search_result = result.find(search_string)
    if search_result != -1:
        print(name +" Out of Stock!")
    else:
        is_available = 0
        print(name + " available - notify " + url)
        publish(name + " " + url )
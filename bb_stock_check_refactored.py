
import requests
from datetime import datetime
import time
import random
import boto3
import os

# global vars
is_available = 0
attempts = 0

# update header accordingly
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'authority': 'www.bestbuy.com'
    }

# send notification
def publish(ps5_name):
    arn = "arn:aws:sns:us-east-1:891431751772:PS5-IN-STOCK"
    sns_client = boto3.client( 'sns', region_name="us-east-1" )
    response = sns_client.publish(
        TopicArn=arn, Message=" It's in Stock! Go Grab it! " + ps5_name )

while(is_available == 0):
    items = [
        {
        'item_url': 'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161',
        'item_name': "PlayStation 5 Digital Edition Console", 'search_string': 'Sold Out</button>'
        }, 
        {
        'item_url': 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149',
        'item_name': "PlayStation 5 Console",  'search_string': 'Sold Out</button>'
        }, 
        {
        'item_url': 'https://www.bestbuy.com/site/madden-nfl-22-standard-edition-playstation-5/6465432.p?skuId=6465432',
        'item_name': "Madden NFL 22 Standard Edition",  'search_string': 'Sold Out</button>'
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
            print('Time = ' + str(datetime.now()) +
                  " - Attempts = " + str(attempts))
            time.sleep(random.randint(20, 60))
        else:
            is_available = 0
            print(name + " available - notify " + url)
            publish(name + " " + url )
            time.sleep(random.randint(20, 60))
    attempts += 1


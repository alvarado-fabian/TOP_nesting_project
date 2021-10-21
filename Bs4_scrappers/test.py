import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime
import boto3

# global vars
is_available = 0
attempts = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'authority': 'www.bestbuy.com'
    }

URL = "https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161"
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="fulfillment-fulfillment-summary")
# print(results.prettify())

avail = results.get_text()

avail=avail.strip("This item is currently sold out but we are working to get more inventory.")
avail+="ut!"

# def publish(ps5_name):
#     arn = "arn:aws:sns:us-east-1:891431751772:PS5-IN-STOCK"
#     sns_client = boto3.client( 'sns', region_name="us-east-1" )
#     response = sns_client.publish(
#         TopicArn=arn, Message=" It's in Stock! Go Grab it! " + ps5_name )
# 
# while(is_available == 0):
#         if avail == "Sold Out!":
#             print(" PS5 is out of stock!")
#             print('Time = ' + str(datetime.now()) +
#                   " - Attempts = " + str(attempts))
#             time.sleep(random.randint(20, 60))
#         else:
#             is_available = 0
#             print(" available - notify " + URL)
#             publish(URL)
#             time.sleep(random.randint(20, 60))
#         attempts += 1
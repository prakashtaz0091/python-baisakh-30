import requests
import csv
from datetime import datetime
from dotenv import load_dotenv
import os
import time

load_dotenv()


def scrape():
    url = "https://real-time-amazon-data.p.rapidapi.com/deals-v2"

    querystring = {
        "country": "US",
        "min_product_star_rating": "ALL",
        "price_range": "ALL",
        "discount_range": "ALL",
    }

    headers = {
        "x-rapidapi-key": os.getenv("X-RAPID-API-KEY"),
        "x-rapidapi-host": os.getenv("X-RAPID-API-HOST"),
    }

    output_filename = (
        f"./outputs/amazon-deals-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
    )

    deals_data = []

    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
    if response["status"] == "OK":
        deals = response["data"]["deals"]
        for deal in deals:
            deal_title = deal["deal_title"]
            deal_url = deal["deal_url"]
            deal_photo = deal["deal_photo"]
            deal_price = deal["deal_price"]

            new_deal = [
                deal_title,
                deal_url,
                deal_photo,
                deal_price,
            ]
            deals_data.append(new_deal)

        with open(output_filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Title",
                    "URL",
                    "Photo",
                    "Price",
                ]
            )
            writer.writerows(deals_data)

        print("scrape success")
    else:
        print("Something went wrong!")


scrape()

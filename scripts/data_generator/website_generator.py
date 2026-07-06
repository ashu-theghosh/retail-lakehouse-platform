import json
import random
import os
from faker import Faker

fake = Faker("en_IN")

OUTPUT_DIR="sample_data/raw"

with open(f"{OUTPUT_DIR}/erp_products.json") as f:
    products=json.load(f)

with open(f"{OUTPUT_DIR}/crm_customers.json") as f:
    customers=json.load(f)

orders=[]

order_id=5001

for i in range(50):

    customer=random.choice(customers)

    no_items=random.randint(1,4)

    items=[]

    total=0

    for j in range(no_items):

        p=random.choice(products)

        qty=random.randint(1,3)

        price=p["pricing"]["selling_price"]

        total+=qty*price

        items.append({

            "product_id":p["product_id"],

            "product_name":p["product_name"],

            "quantity":qty,

            "price":price

        })

    orders.append({

        "order_id":order_id,

        "customer_id":customer["customer_id"],

        "items":items,

        "coupon":random.choice(["WELCOME10","FESTIVE20",None]),

        "payment_amount":total,

        "shipping_address":customer["address"],

        "order_status":random.choice(

            ["PLACED","SHIPPED","DELIVERED","CANCELLED"]

        ),

        "order_timestamp":

        fake.date_time_between(

            start_date="-6M",

            end_date="now"

        ).isoformat()

    })

    order_id+=1

with open(f"{OUTPUT_DIR}/website_orders.json","w") as f:
    json.dump(orders,f,indent=4)

print("Website Orders Generated")
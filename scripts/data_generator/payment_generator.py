import json
import random
from faker import Faker

fake=Faker()

with open("sample_data/raw/website_orders.json") as f:
    orders=json.load(f)

payments=[]

payment_id=9001

methods=["UPI","Credit Card","Debit Card","Net Banking","COD"]

for order in orders:

    payments.append({

        "payment_id":payment_id,

        "order_id":order["order_id"],

        "customer_id":order["customer_id"],

        "amount":order["payment_amount"],

        "payment_method":random.choice(methods),

        "status":random.choice(

            ["SUCCESS","FAILED","PENDING"]

        ),

        "refund":{

            "eligible":random.choice([True,False]),

            "refund_status":random.choice(

                ["NA","NOT_INITIATED","PROCESSING","COMPLETED"]

            )

        },

        "payment_timestamp":

        fake.date_time_between(

            start_date="-6M",

            end_date="now"

        ).isoformat()

    })

    payment_id+=1

with open("sample_data/raw/payments.json","w") as f:
    json.dump(payments,f,indent=4)

print("Payments Generated")
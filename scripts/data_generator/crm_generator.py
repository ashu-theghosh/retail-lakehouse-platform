import json
import random
import os
from faker import Faker

fake = Faker("en_IN")

NUM_RECORDS = 50

OUTPUT_DIR = "sample_data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

tiers = ["Bronze", "Silver", "Gold", "Platinum"]

customers = []

for customer_id in range(1001, 1001 + NUM_RECORDS):

    customer = {

        "customer_id": customer_id,

        "name": {

            "first_name": fake.first_name(),

            "last_name": fake.last_name()

        },

        "email": fake.email(),

        "phone": fake.phone_number(),

        "gender": random.choice(["Male","Female"]),

        "address":{

            "city": fake.city(),

            "state": fake.state(),

            "pincode": fake.postcode()

        },

        "loyalty":{

            "tier": random.choice(tiers),

            "points": random.randint(0,10000)

        },

        "registration_date": fake.date_between(
            start_date="-4y",
            end_date="-1y"
        ).isoformat(),

        "last_updated": fake.date_time_between(
            start_date="-1y",
            end_date="now"
        ).isoformat()

    }

    customers.append(customer)

with open(f"{OUTPUT_DIR}/crm_customers.json","w") as f:
    json.dump(customers,f,indent=4)

print(f"{NUM_RECORDS} CRM customers generated.")
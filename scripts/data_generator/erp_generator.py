import json
import random
from faker import Faker

fake = Faker("en_IN")

NUM_RECORDS = 50

CATEGORIES = [
    {"category_id": 1, "category_name": "Mobiles"},
    {"category_id": 2, "category_name": "Laptops"},
    {"category_id": 3, "category_name": "Television"},
    {"category_id": 4, "category_name": "Fashion"},
    {"category_id": 5, "category_name": "Home Appliances"}
]

SUPPLIERS = [
    {
        "supplier_id": 501,
        "supplier_name": "Samsung India",
        "supplier_city": "Noida",
        "supplier_rating": 4.8
    },
    {
        "supplier_id": 502,
        "supplier_name": "Dell India",
        "supplier_city": "Bengaluru",
        "supplier_rating": 4.6
    },
    {
        "supplier_id": 503,
        "supplier_name": "Apple India",
        "supplier_city": "Mumbai",
        "supplier_rating": 4.9
    },
    {
        "supplier_id": 504,
        "supplier_name": "LG India",
        "supplier_city": "Pune",
        "supplier_rating": 4.5
    }
]

PRODUCT_CATALOG = [
    {
        "product_name": "Samsung Galaxy S25",
        "category_id": 1,
        "supplier_id": 501
    },
    {
        "product_name": "Samsung Galaxy A56",
        "category_id": 1,
        "supplier_id": 501
    },
    {
        "product_name": "Apple iPhone 17",
        "category_id": 1,
        "supplier_id": 503
    },
    {
        "product_name": "Apple iPhone 16",
        "category_id": 1,
        "supplier_id": 503
    },
    {
        "product_name": "OnePlus 14",
        "category_id": 1,
        "supplier_id": 501
    },
    {
        "product_name": "Dell Inspiron 15",
        "category_id": 2,
        "supplier_id": 502
    },
    {
        "product_name": "HP Pavilion 14",
        "category_id": 2,
        "supplier_id": 502
    },
    {
        "product_name": "Lenovo ThinkPad E16",
        "category_id": 2,
        "supplier_id": 502
    },
    {
        "product_name": "Apple MacBook Air M4",
        "category_id": 2,
        "supplier_id": 503
    },
    {
        "product_name": "LG OLED 55 TV",
        "category_id": 3,
        "supplier_id": 504
    },
    {
        "product_name": "Samsung Crystal UHD 65",
        "category_id": 3,
        "supplier_id": 501
    },
    {
        "product_name": "Sony Bravia 55",
        "category_id": 3,
        "supplier_id": 504
    },
    {
        "product_name": "Whirlpool Refrigerator",
        "category_id": 5,
        "supplier_id": 504
    },
    {
        "product_name": "LG Front Load Washing Machine",
        "category_id": 5,
        "supplier_id": 504
    },
    {
        "product_name": "IFB Microwave Oven",
        "category_id": 5,
        "supplier_id": 504
    },
    {
        "product_name": "Philips Air Fryer",
        "category_id": 5,
        "supplier_id": 504
    },
    {
        "product_name": "Nike Air Max Shoes",
        "category_id": 4,
        "supplier_id": 501
    },
    {
        "product_name": "Levi's 511 Jeans",
        "category_id": 4,
        "supplier_id": 501
    },
    {
        "product_name": "Puma Sports T-Shirt",
        "category_id": 4,
        "supplier_id": 501
    },
    {
        "product_name": "Adidas Running Shoes",
        "category_id": 4,
        "supplier_id": 501
    }
]

def generate_product(product_id):

    catalog = random.choice(PRODUCT_CATALOG)

    category = next(
        c for c in CATEGORIES
        if c["category_id"] == catalog["category_id"]
    )

    supplier = next(
        s for s in SUPPLIERS
        if s["supplier_id"] == catalog["supplier_id"]
    )

    cost_price = random.randint(5000, 80000)

    selling_price = cost_price + random.randint(1000, 12000)

    product = {
        "product_id": product_id,

        "product_name": catalog["product_name"],

        "category": {
            "category_id": category["category_id"],
            "category_name": category["category_name"]
        },

        "supplier": {
            "supplier_id": supplier["supplier_id"],
            "supplier_name": supplier["supplier_name"],
            "supplier_city": supplier["supplier_city"],
            "supplier_rating": supplier["supplier_rating"]
        },

        "pricing": {
            "cost_price": cost_price,
            "selling_price": selling_price
        },

        "status": random.choice(["ACTIVE", "INACTIVE"]),

        "created_date": fake.date_time_between(
            start_date="-2y",
            end_date="-1y"
        ).isoformat(),

        "updated_date": fake.date_time_between(
            start_date="-1y",
            end_date="now"
        ).isoformat()
    }

    return product


products = []

for product_id in range(101, 101 + NUM_RECORDS):
    products.append(generate_product(product_id))

with open("/home/ashu/retail-lakehouse-platform/sample_data/raw/erp_products.json", "w") as file:
    json.dump(products, file, indent=4)

print(f"{NUM_RECORDS} ERP products generated successfully.")
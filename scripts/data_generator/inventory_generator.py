import json
import random

with open("sample_data/raw/erp_products.json") as f:
    products=json.load(f)

warehouses=[

{"warehouse_id":1,"warehouse_name":"Kolkata FC"},

{"warehouse_id":2,"warehouse_name":"Mumbai FC"},

{"warehouse_id":3,"warehouse_name":"Delhi FC"}

]

inventory=[]

for w in warehouses:

    stock=[]

    for p in products:

        stock.append({

            "product_id":p["product_id"],

            "available_stock":random.randint(0,500),

            "reorder_level":20

        })

    inventory.append({

        "warehouse_id":w["warehouse_id"],

        "warehouse_name":w["warehouse_name"],

        "products":stock

    })

with open("sample_data/raw/inventory_stock.json","w") as f:
    json.dump(inventory,f,indent=4)

print("Inventory Generated")
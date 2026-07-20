from pyspark.sql.functions import *


def erp_validator():
    return (
    col("product_id").isNotNull() &
    col("product_name").isNotNull() &
    col("category.category_id").isNotNull() &
    col("category.category_name").isNotNull() &
    col("supplier.supplier_id").isNotNull() &
    col("supplier.supplier_name").isNotNull() &
    col("pricing.cost_price").isNotNull() &
    col("pricing.selling_price").isNotNull() &
    (col("pricing.cost_price") > 0) &
    (col("pricing.selling_price") > 0) &
    col("status").isin("ACTIVE", "INACTIVE") &
    col("created_date").isNotNull()
    )

def crm_validator():
    return (
        col("customer_id").isNotNull() &
        col("email").isNotNull() &
        col("address.city").isNotNull() &
        col("address.pincode").isNotNull() &
        col("address.state").isNotNull() &
        col("name.first_name").isNotNull() &
        col("name.last_name").isNotNull() &
        col("phone").isNotNull() &
        col("registration_date").isNotNull()
        )
    

def website_validator():
    return (
        col("customer_id").isNotNull() &
        (size(col("items")) > 0) &
        col("order_id").isNotNull() &
        col("order_status").isNotNull() &
        col("order_timestamp").isNotNull() &
        col("shipping_address.city").isNotNull() &
        col("shipping_address.pincode").isNotNull() &
        col("shipping_address.state").isNotNull() &
        col("payment_amount").isNotNull()
         )
    

def inventory_validator():
    return (
      col("products").isNotNull() &
      (size(col("products"))>0) &
      col("warehouse_id").isNotNull() &
      col("warehouse_name").isNotNull()
       )
    


def payment_validator():
    return (
       col("amount").isNotNull() &
       col("customer_id").isNotNull() &
       col("order_id").isNotNull() &
       col("payment_id").isNotNull() &
       col("payment_method").isNotNull() &
       col("payment_timestamp").isNotNull() &
       col("refund.eligible").isin([True, False]) &
       col("refund.refund_status").isNotNull() &
       col("status").isNotNull()
       )
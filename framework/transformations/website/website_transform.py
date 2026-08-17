from pyspark.sql.functions import *
from pyspark.sql.types import *

def build_orders_fact(bronze_df):
    input_record=bronze_df.count()
    fact_orders=bronze_df.select(col("order_id"),col("customer_id"),col("order_status"),col("payment_amount"),col("order_timestamp").cast("timestamp"),col("coupon"),col("shipping_address.city").alias("shipping_city"),col("shipping_address.pincode").cast("long").alias("shipping_pincode"),col("shipping_address.state").alias("shipping_state"),col("ingestion_timestamp"),col("batch_id"),col("source_system"),col("source_file"))
    output_record=fact_orders.count()
    duplicate_removed_record=0
    return fact_orders,input_record,output_record,duplicate_removed_record

def build_order_items_fact(bronze_df):
    input_record=bronze_df.count()
    bronze_website_explode=bronze_df.withColumn("items", explode_outer("items"))
    fact_order_items=bronze_website_explode.select(col("order_id"),col("customer_id"),col("items.product_id").alias("product_id"),col("items.product_name").alias("product_name"),col("items.quantity").alias("quantity"),col("items.price").alias("price"))
    output_record=fact_order_items.count()
    duplicate_removed_record=0
    return fact_order_items,input_record,output_record,duplicate_removed_record
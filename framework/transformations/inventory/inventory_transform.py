from pyspark.sql.functions import *
from pyspark.sql.types import *

def build_warehouse_dimension(bronze_df):
    bronze_inventory_explode=bronze_df.withColumn("products",explode_outer(col("products")))
    dim_warehouse=bronze_inventory_explode.select(col("warehouse_id"),col("warehouse_name")).dropDuplicates(["warehouse_id"])
    return dim_warehouse

def build_inventory_fact(bronze_df):
    bronze_inventory_explode=bronze_df.withColumn("products",explode_outer(col("products")))
    fact_inventory=bronze_inventory_explode.select(col("products.available_stock").alias("available_stock"),col("products.product_id").alias("product_id"),col("products.reorder_level").alias("reorder_level"),col("warehouse_id"),col("ingestion_timestamp"),col("source_system"),col("batch_id"),col("source_file"))
    return fact_inventory

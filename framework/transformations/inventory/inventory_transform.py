from pyspark.sql.functions import *
from pyspark.sql.types import *

def build_warehouse_dimension(bronze_df):
    input_record=bronze_df.count()
    bronze_inventory_explode=bronze_df.withColumn("products",explode_outer(col("products")))
    transformed_record=bronze_inventory_explode.count()
    dim_warehouse=bronze_inventory_explode.select(col("warehouse_id"),col("warehouse_name")).dropDuplicates(["warehouse_id"])
    output_record=dim_warehouse.count()
    duplicate_removed_record=transformed_record-output_record
    return dim_warehouse,input_record,output_record,duplicate_removed_record

def build_inventory_fact(bronze_df):
    input_record=bronze_df.count()
    bronze_inventory_explode=bronze_df.withColumn("products",explode_outer(col("products")))
    fact_inventory=bronze_inventory_explode.select(col("products.available_stock").alias("available_stock"),col("products.product_id").alias("product_id"),col("products.reorder_level").alias("reorder_level"),col("warehouse_id"),col("ingestion_timestamp"),col("source_system"),col("batch_id"),col("source_file"))
    output_record=fact_inventory.count()
    duplicate_removed_record=0
    return fact_inventory,input_record,output_record,duplicate_removed_record
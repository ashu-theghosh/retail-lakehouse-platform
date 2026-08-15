from pyspark.sql.functions import *
from pyspark.sql.types import *


def build_product_dimension(bronze_df):
    dim_product=bronze_df.select(col("product_id"),col("category.category_id").alias("category_id"),col("supplier.supplier_id").alias("supplier_id"),col("product_name"),col("status"),col("pricing.cost_price").alias("cost_price"),col("pricing.selling_price").alias("selling_price"),col("created_date").cast("date"),col("updated_date").cast("date"),col("ingestion_timestamp"),col("batch_id"))
    return dim_product

def build_category_dimension(bronze_df):
    dim_category=bronze_df.select(col("category.category_id").alias("category_id"),col("category.category_name").alias("category_name"),col("batch_id"))
    dim_category_final=dim_category.dropDuplicates(["category_id"])
    return dim_category_final

def build_supplier_dimension(bronze_df):
    dim_supplier=bronze_df.select(col("supplier.supplier_id").alias("supplier_id"),col("supplier.supplier_name").alias("supplier_name"),col("supplier.supplier_city").alias("supplier_city"),col("supplier.supplier_rating").alias("supplier_rating"),col("batch_id"))
    dim_supplier_final=dim_supplier.dropDuplicates(["supplier_id"])
    return dim_supplier_final
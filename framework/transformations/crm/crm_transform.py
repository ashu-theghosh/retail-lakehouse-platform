from pyspark.sql.functions import *
from pyspark.sql.types import *

def build_customer_dimension(bronze_df):
    input_record=bronze_df.count()
    dim_customer_final=bronze_df.select(col("customer_id"),col("name.first_name").alias("first_name"),col("name.last_name").alias("last_name"),col("gender"),col("email"),col("phone"),col("address.city").alias("city"),col("address.state").alias("state"),col("address.pincode").alias("pincode"),col("registration_date").cast("date"),col("loyalty.points").alias("loyalty_points"),col("loyalty.tier").alias("loyalty_tier"),col("ingestion_timestamp"),col("batch_id"))
    output_record=dim_customer_final.count()
    duplicate_removed_records=0
    return dim_customer_final,input_record,output_record,duplicate_removed_records
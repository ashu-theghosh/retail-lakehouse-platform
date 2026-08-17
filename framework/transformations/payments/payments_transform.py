from pyspark.sql.functions import *
from pyspark.sql.types import *

def build_payment_fact(bronze_df):
    input_record=bronze_df.count()
    fact_payment=bronze_df.select(col("payment_id"),col("order_id"),col("customer_id"),col("payment_method"),col("amount"),col("payment_timestamp").cast("timestamp"),col("status"),col("refund.eligible").alias("refund_eligible"),col("refund.refund_status").alias("refund_status"),col("ingestion_timestamp"),col("source_system"),col("batch_id"),col("source_file"))
    output_record=fact_payment.count()
    duplicate_removed_record=0
    return fact_payment,input_record,output_record,duplicate_removed_record
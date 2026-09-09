from pyspark.sql.functions import *
from pyspark.sql.types import *

def build_daily_product_sales(dataframes):
    orders=dataframes["fact_orders"].alias("o")
    order_items=dataframes["fact_order_items"].alias("oi")
    joined_df=orders.join(order_items,on='order_id',how="inner").filter(col("order_status")=="DELIVERED").select(col("order_id"),col("oi.customer_id"),col("order_timestamp"),col("product_id"),col("product_name"),col("quantity"),col("price")).withColumn("order_date",to_date(col("order_timestamp")))
    daily_product_sales=joined_df.groupby(col("order_date"),col("product_id"),col("product_name")).agg(sum(col("quantity")).alias("total_quantity"),sum(col("quantity")*col("price")).alias("gross_revenue"),countDistinct(col("order_id")).alias("total_orders"))
    output_record=daily_product_sales.count()
    return daily_product_sales,output_record

def build_customer_sales_summary(dataframes):
    orders=dataframes["fact_orders"].alias("o")
    order_items=dataframes["fact_order_items"].alias("oi")
    customers=dataframes["dim_customer"]
    joined_df=orders.join(order_items,on='order_id',how="inner").filter(col("order_status")=="DELIVERED").select(col("order_id"),col("oi.customer_id"),col("order_timestamp"),col("product_id"),col("product_name"),col("quantity"),col("price")).withColumn("order_date",to_date(col("order_timestamp")))
    customer_join=joined_df.join(customers,on='customer_id',how="inner").select(col("customer_id"),col("order_id"),col("quantity"),col("price"),col("first_name"),col("last_name"))
    group_cust=customer_join.groupby(col("customer_id"),col("first_name"),col("last_name")).agg(sum(col("quantity")).alias("total_quantity"),sum(col("quantity")*col("price")).alias("gross_revenue"),countDistinct(col("order_id")).alias("total_orders"))
    customer_sales_summary=group_cust.withColumn("avg_order_value",col("gross_revenue")/col("total_orders"))
    output_record=customer_sales_summary.count()
    return customer_sales_summary,output_record

def build_product_performance(dataframes):
    orders=dataframes["fact_orders"].alias("o")
    order_items=dataframes["fact_order_items"].alias("oi")
    joined_df=orders.join(order_items,on='order_id',how="inner").filter(col("order_status")=="DELIVERED").select(col("order_id"),col("oi.customer_id"),col("order_timestamp"),col("product_id"),col("product_name"),col("quantity"),col("price")).withColumn("order_date",to_date(col("order_timestamp")))
    product_performance_summary=joined_df.groupby(col("product_id"),col("product_name")).agg(sum(col("quantity")).alias("total_quantity"),sum(col("quantity")*col("price")).alias("gross_revenue"),countDistinct(col("order_id")).alias("total_orders"))
    product_performance_summary_final=product_performance_summary.withColumn("average_unit_price",col("gross_revenue")/col("total_quantity"))
    output_record=product_performance_summary_final.count()
    return product_performance_summary_final,output_record

def build_daily_sales_summary(dataframes):
    orders=dataframes["fact_orders"].alias("o")
    order_items=dataframes["fact_order_items"].alias("oi")
    joined_df=orders.join(order_items,on='order_id',how="inner").filter(col("order_status")=="DELIVERED").select(col("order_id"),col("oi.customer_id"),col("order_timestamp"),col("product_id"),col("product_name"),col("quantity"),col("price")).withColumn("order_date",to_date(col("order_timestamp")))
    daily_sales_summary=joined_df.groupBy(col("order_date")).agg(sum(col("quantity")).alias("total_quantity"),sum(col("quantity")*col("price")).alias("gross_revenue"),countDistinct(col("order_id")).alias("total_orders"))
    daily_sales_summary_final=daily_sales_summary.withColumn("average_unit_price",col("gross_revenue")/col("total_quantity")).withColumn("average_order_value",col("gross_revenue")/col("total_orders"))
    output_record=daily_sales_summary_final.count()
    return daily_sales_summary_final,output_record
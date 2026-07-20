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
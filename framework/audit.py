from pyspark.sql.functions import *

def add_audit_columns_clean(df,source_system,batch_id,source_file_column="_metadata.file_path"):
    return df.withColumn("ingestion_timestamp", current_timestamp()) \
            .withColumn("source_system",lit(source_system.upper())) \
            .withColumn("batch_id",lit(batch_id)) \
            .withColumn("source_file",col(source_file_column))

def prepare_bad_records(df,batch_id,pipeline_name,source_system,table_name,failure_reason,source_file_column="_metadata.file_path"):
    return df.withColumn("batch_id", lit(batch_id))\
        .withColumn("pipeline_name", lit(pipeline_name))\
        .withColumn("source_system", lit(source_system.upper()))\
        .withColumn("table_name", lit(table_name))\
        .withColumn("failure_reason", lit(failure_reason))\
        .withColumn("source_file", col(source_file_column))\
        .withColumn("ingestion_timestamp", current_timestamp())\
        .withColumn("raw_record", to_json(struct(*df.columns)))\
        .select(
        col("batch_id"),
        col("pipeline_name"),
        col("source_system"),
        col("table_name"),
        col("failure_reason"),
        col("source_file"),
        col("ingestion_timestamp"),
        col("raw_record")
        )



def combine_bad_records(business_bad_df,corrupt_bad_df,corrupt_count,batch_id,pipeline_name,source_system,table_name):
    business_bad_df=prepare_bad_records(df1,batch_id,pipeline_name,source_system,table_name,"MANDATORY_FIELD_VALIDATION_FAILED")
    
    if df2 is not None and corrupt_count>0:
        corrupt_bad_df=prepare_bad_records(df2,batch_id,pipeline_name,source_system,table_name,"CORRUPT_JSON")
        return business_bad_df.unionByName(corrupt_bad_df,allowMissingColumns=True)
    else:
        return business_bad_df
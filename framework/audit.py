def add_audit_columns(df,source_system,batch_id,source_file_column="_metadata.file_path"):
    return df.withColumn("ingestion_timestamp",current_timestamp()) \
            .withColumn("source_system",lit(source_system.upper())) \
            .withColumn("batch_id",lit(batch_id)) \
            .withColumn("source_file",col(source_file_column))
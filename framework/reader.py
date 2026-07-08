def read_json(spark, raw_path):
        return spark.read.format("json")\
                .option("multiLine", "true")\
                .option("mode","PERMISSIVE")\
                .load(raw_path)
    
def separate_corrupt_records(df):
      if "_corrupt_record" in df.columns:
          corrupt_df=df.filter(col("_corrupt_record").isNotNull())
          clean_df=df.filter(col("_corrupt_record").isNull())
          corrupt_count=corrupt_df.count()
          return clean_df,corrupt_df,corrupt_count
      return df,None,0
def read_json(raw_path):
    try:
        df=spark.read.format(my_format)\
                .option("multiLine", "true")\
                .option("mode","PERMISSIVE")\
                .load(raw_path)
        return df
    except Exception as e:
         raise Exception(f"Failed to read JSON from {raw_path}: {e}")
from pyspark.sql.functions import *

def write_delta(df,output_path,my_mode):
    return df.write \
             .format("delta") \
             .mode(my_mode) \
             .save(output_path)
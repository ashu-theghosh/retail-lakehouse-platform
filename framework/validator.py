from pyspark.sql.functions import *

def split_records(df, validation_condition):
      good_df=df.filter(validation_condition)
      bad_df=df.filter(~validation_condition)
      return good_df,bad_df
def write_delta(df,output_path,my_mode):
    return df.write \
             .format("delta") \
             .mode(my_mode) \
             .save(output_path)


def write_bad_records_delta(df,output_path,my_mode):
    return bad_df.write \
                 .format("delta") \
                 .mode(my_mode) \
                 .save(output_path)
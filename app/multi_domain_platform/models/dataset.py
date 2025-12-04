import pandas as pd

# Loads dataset metadata from the database.
def get_all_datasets(conn):
    return pd.read_sql("SELECT * FROM datasets_metadata", conn)

import pandas as pd

# Loads all IT ticket records from the database.
def get_all_tickets(conn):
    return pd.read_sql("SELECT * FROM it_tickets", conn)

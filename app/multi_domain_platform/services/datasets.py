import pandas as pd
from app.multi_domain_platform.database import connect_database

def get_all_datasets():
    conn = connect_database()
    query = "SELECT * FROM datasets_metadata"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
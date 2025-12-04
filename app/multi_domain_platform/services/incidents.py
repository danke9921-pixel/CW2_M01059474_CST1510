import pandas as pd
from app.multi_domain_platform.database import connect_database

def get_all_incidents():
    conn = connect_database()
    query = "SELECT * FROM cyber_incidents"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

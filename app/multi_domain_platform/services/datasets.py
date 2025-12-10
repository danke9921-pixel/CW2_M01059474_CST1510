# Author: Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - Programming and Data Communication Networks
# Description:
# This module handles dataset‑related queries, including retrieving metadata,
# category information, and record counts from the SQLite database. It provides
# the Data Science dashboard with structured information for analysis and
# visualisation.

import pandas as pd
from app.multi_domain_platform.database import connect_database

def get_all_datasets():
    """
    Retrieves all dataset metadata from the database and returns it as a DataFrame.
    """
    conn = connect_database()
    query = "SELECT * FROM datasets_metadata"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
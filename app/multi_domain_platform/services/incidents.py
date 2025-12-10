# Author: Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - Programming and Data Communication Networks
# Description:
# This service module contains SQL queries and helper functions for retrieving
# and managing incident data. It supplies the Cybersecurity dashboard with the
# information required to display incident trends and severity levels.

import pandas as pd
from app.multi_domain_platform.database import connect_database

def get_all_incidents():
    conn = connect_database()
    query = "SELECT * FROM cyber_incidents"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

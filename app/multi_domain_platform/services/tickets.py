# Author: Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - Programming and Data Communication Networks
# Description:
# This module manages SQL queries for IT operations tickets. It supplies the
# IT Operations dashboard with ticket statuses, priorities, and resolution times
# to support operational monitoring.

import pandas as pd
from app.multi_domain_platform.database import connect_database

def get_all_tickets():
    conn = connect_database()
    query = "SELECT * FROM it_tickets"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
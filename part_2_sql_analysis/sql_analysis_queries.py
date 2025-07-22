import sqlite3

# Script: sql_analysis_queries.py
# Purpose: Connect to marketing_data.db and run analytical queries on campaign_performance table

def connect_db(db_path):
    """Connect to the SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        print(f"Connected to database: {db_path}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def query_campaign_with_most_leads(conn):
    """Query for the campaign with the most leads."""
    sql = '''
        SELECT campanha, SUM(leads) as total_leads
        FROM campaign_performance
        GROUP BY campanha
        ORDER BY total_leads DESC
        LIMIT 1;
    '''
    print("\n[Query 1] Campaign with Most Leads:")
    print(sql)
    try:
        cursor = conn.execute(sql)
        result = cursor.fetchone()
        if result:
            print(f"Campaign: {result[0]} | Total Leads: {result[1]}")
        else:
            print("No results found.")
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")

def query_campaign_with_best_cpl(conn):
    """Query for the campaign with the best (lowest) CPL (Cost Per Lead)."""
    sql = '''
        SELECT campanha, 
               ROUND(SUM(valor_gasto) / NULLIF(SUM(leads), 0), 2) as CPL
        FROM campaign_performance
        GROUP BY campanha
        HAVING SUM(leads) > 0
        ORDER BY CPL ASC
        LIMIT 1;
    '''
    print("\n[Query 2] Campaign with Best (Lowest) CPL:")
    print(sql)
    try:
        cursor = conn.execute(sql)
        result = cursor.fetchone()
        if result:
            print(f"Campaign: {result[0]} | Best CPL: R$ {result[1]}")
        else:
            print("No results found.")
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")

def main():
    db_path = 'marketing_data.db'
    conn = connect_db(db_path)
    if not conn:
        return
    try:
        # Query 1: Campaign with Most Leads
        query_campaign_with_most_leads(conn)
        # Query 2: Campaign with Best CPL
        query_campaign_with_best_cpl(conn)
    finally:
        conn.close()
        print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()

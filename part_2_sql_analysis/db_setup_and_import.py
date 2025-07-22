import pandas as pd
import sqlite3
import os
from datetime import datetime

def create_database():
    """Create SQLite database and establish connection"""
    try:
        conn = sqlite3.connect('marketing_data.db')
        print("Database created successfully!")
        return conn
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
        raise

def infer_sql_type(column_name, sample_value):
    """Infer SQLite data type based on column name and sample value"""
    # Convert column name to lowercase for easier comparison
    col_lower = column_name.lower()
    
    # Check if it's a monetary or percentage column
    if any(term in col_lower for term in ['valor', 'custo', 'cpc', 'taxa', 'rate']):
        return 'REAL'
    
    # Check if it's a count/integer column
    if any(term in col_lower for term in ['impressões', 'cliques', 'leads', 'conversões']):
        return 'INTEGER'
    
    # Check if it's a date column
    if any(term in col_lower for term in ['data', 'date']):
        return 'TEXT'
    
    # Default to TEXT for other columns
    return 'TEXT'

def create_table(conn, df):
    """Create table with appropriate schema based on DataFrame columns"""
    try:
        # Start with ID column
        columns = ['id INTEGER PRIMARY KEY AUTOINCREMENT']
        
        # Add other columns with inferred types
        for col in df.columns:
            sql_type = infer_sql_type(col, df[col].iloc[0] if len(df) > 0 else None)
            # Replace spaces and special characters in column names
            safe_col_name = col.replace(' ', '_').replace('-', '_')
            columns.append(f'"{safe_col_name}" {sql_type}')
        
        # Create the table
        create_table_sql = f'''
        CREATE TABLE IF NOT EXISTS campaign_performance (
            {','.join(columns)}
        )
        '''
        conn.execute(create_table_sql)
        conn.commit()
        print("Table created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
        raise

def process_dates(df):
    """Convert date columns to YYYY-MM-DD format"""
    for col in df.columns:
        if 'data' in col.lower() or 'date' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col]).dt.strftime('%Y-%m-%d')
            except Exception as e:
                print(f"Warning: Could not convert column {col} to date format: {e}")
    return df

def import_data(conn, df):
    """Import data from DataFrame to SQLite database"""
    try:
        # Process dates before import
        df = process_dates(df)
        
        # Replace spaces and special characters in column names
        df.columns = [col.replace(' ', '_').replace('-', '_') for col in df.columns]
        
        # Import data
        df.to_sql('campaign_performance', conn, if_exists='append', index=False)
        print(f"Successfully imported {len(df)} rows of data!")
    except Exception as e:
        print(f"Error importing data: {e}")
        raise

def print_table_info(conn):
    """Print table schema and first few rows"""
    try:
        # Print schema
        print("\nTable Schema:")
        cursor = conn.execute("PRAGMA table_info(campaign_performance);")
        for row in cursor:
            print(f"Column: {row[1]}, Type: {row[2]}")
        
        # Print sample data
        print("\nFirst few rows of data:")
        cursor = conn.execute("SELECT * FROM campaign_performance LIMIT 3")
        columns = [description[0] for description in cursor.description]
        print("\nColumns:", columns)
        for row in cursor:
            print(row)
    except sqlite3.Error as e:
        print(f"Error retrieving table info: {e}")

def main():
    try:
        # Check if Excel file exists
        excel_file = "Isadora Perdigao - [HP] PLANILHA TESTE TÉCNICO.xlsx"
        if not os.path.exists(excel_file):
            raise FileNotFoundError(f"Excel file {excel_file} not found!")
        
        # Read Excel file
        print(f"Reading Excel file: {excel_file}")
        df = pd.read_excel(excel_file, sheet_name=0)
        
        # Create database and connection
        conn = create_database()
        
        # Create table
        create_table(conn, df)
        
        # Import data
        import_data(conn, df)
        
        # Print table information
        print_table_info(conn)
        
        # Close connection
        conn.close()
        print("\nDatabase connection closed. Process completed successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()

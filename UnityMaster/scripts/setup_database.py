import pyodbc

# Database connection details
connection_string = r'DRIVER={SQL Server};SERVER=DESKTOP-1B1FLGB\MASTERSQL;DATABASE=UnitMasterDB;Trusted_Connection=yes'

# Read SQL scripts
with open('database_schema.sql', 'r') as file:
    schema_sql = file.read()

with open('sample_data.sql', 'r') as file:
    data_sql = file.read()

# Execute SQL scripts
try:
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(schema_sql)  # Create tables
        cursor.execute(data_sql)    # Insert sample data
        conn.commit()
    print("Database setup completed successfully!")
except pyodbc.Error as e:
    print(f"Error: {e}")
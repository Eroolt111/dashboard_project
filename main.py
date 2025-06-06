import psycopg2
import re
from config.dashboard_config import dashboard_config

def sanitize_table_name(name):
    return re.sub(r'\W+', '_', name.lower())

# Create a table in the specified schema
def create_table(conn, schema_name, table_name):
    try:
        cursor = conn.cursor()
        # Create the schema if it doesn’t exist
        cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")
        # Create the table inside the schema
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (
                id SERIAL PRIMARY KEY,
                period VARCHAR(50),
                code VARCHAR(50),
                scr_mn VARCHAR(255),
                scr_eng VARCHAR(255),
                code1 VARCHAR(50),
                scr_mn1 VARCHAR(255),
                scr_eng1 VARCHAR(255),
                code2 VARCHAR(50),
                scr_mn2 VARCHAR(255),
                scr_eng2 VARCHAR(255),
                dtval_co NUMERIC,
                fetched_at TIMESTAMP DEFAULT NOW()
            );
        """)
        conn.commit()
        print(f"✅ Table '{schema_name}.{table_name}' created successfully.")
    except Exception as e:
        print(f"❌ Error creating table '{schema_name}.{table_name}': {e}")

# Connect to the PostgreSQL database
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="dashboard_project",
            user="postgres",
            password="80123615",
            host="localhost",
            port="5432"
        )
        print("✅ Connected to PostgreSQL database.")
        return conn
    except Exception as e:
        print(f"❌ Error connecting to database: {e}")
        return None

# Insert data into a table
def fetch_and_save(conn, schema_name, table_name, records):
    try:
        cursor = conn.cursor()
        # Truncate table to refresh data
        cursor.execute(f"TRUNCATE TABLE {schema_name}.{table_name};")
        
        for record in records:
            dtval_co = record["DTVAL_CO"].replace(",", "") if record["DTVAL_CO"] else None
            cursor.execute(f"""
                INSERT INTO {schema_name}.{table_name} (
                    period, code, scr_mn, scr_eng,
                    code1, scr_mn1, scr_eng1,
                    code2, scr_mn2, scr_eng2,
                    dtval_co
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (
                record["Period"],
                record["CODE"],
                record["SCR_MN"],
                record["SCR_ENG"],
                record["CODE1"],
                record["SCR_MN1"],
                record["SCR_ENG1"],
                record["CODE2"] if record["CODE2"] else None,
                record["SCR_MN2"] if record["SCR_MN2"] else None,
                record["SCR_ENG2"] if record["SCR_ENG2"] else None,
                dtval_co
            ))
        conn.commit()
        print(f"✅ Inserted {len(records)} records into '{schema_name}.{table_name}'.")
    except Exception as e:
        print(f"❌ Error inserting data into '{schema_name}.{table_name}': {e}")

# Fetch and save data 
def fetch_all_data(dashboard_config):
    all_data = {}
    conn = connect_db()
    if not conn:
        return all_data
    
    for item in dashboard_config:
        print(f"📊 Fetching: {item['topic']} > {item['name']}")
        schema_name = sanitize_table_name(item["topic"])  
        table_name = sanitize_table_name(item["name"])    
        create_table(conn, schema_name, table_name)
        try:
            code_list = item.get("code_list", None)
            response = item["fetch_func"](item["tbl_id"], code_list)  # API
            print(f"DEBUG: Response type for {item['name']}: {type(response)}")
            print(f"DEBUG: Response sample for {item['name']}: {response[:2] if isinstance(response, list) else response}")
            
            if isinstance(response, dict) and response.get("Response") == "success":
                records = response.get("DataList", [])
            elif isinstance(response, list):
                records = response
            else:
                print(f"❌ Unexpected response format for {item['name']}: {type(response)}")
                all_data[item["name"]] = []
                continue
                
            if records:
                fetch_and_save(conn, schema_name, table_name, records)
                all_data[item["name"]] = records
            else:
                print(f"❌ No records found for {item['name']}")
                all_data[item["name"]] = []
        except Exception as e:
            print(f"❌ Error fetching {item['name']}: {e}")
            all_data[item["name"]] = []
    
    conn.close()
    return all_data

if __name__ == "__main__":
    result = fetch_all_data(dashboard_config)
import sqlite3
import pandas as pd

Testzeile = (28.35, "lidl", 50, "grocery", 21, 12, 1990)
direction = "data/"
database_name = "expenses"


def create_sql_database(table_name, db_name = database_name):
    #connect database
    conn = sqlite3.connect(f"{direction}{db_name}.db")

    # ceate a table
    c = conn.cursor()

    # Create a Table
    c.execute(f"""CREATE TABLE {table_name} (
            id integer,
            amount integer,
            store text,
            organic_percentage integer,
            category text,
            day integer,
            month integer,
            year integer
            )""")
    # Datatypes:
    # Null, integer, real, text, blob

    # commit our command
    conn.commit()

    # close our connection
    conn.close()
    return

def insert_line(db_name, table_name, content):
    conn = sqlite3.connect(f"{direction}{db_name}.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name} ORDER BY id DESC")
    first_line = c.fetchone()
    if first_line is None:
        expense_id = 1
    else:
        expense_id = str(int(first_line[0])+1)
    c.execute(f"INSERT INTO {table_name} VALUES ({expense_id}, ?, ?, ?, ?, ?, ?, ?)", content)
    conn.commit()
    conn.close()
    print("line added")
    return

def fetch_data(db_name, table_name):
    conn = sqlite3.connect(f"{direction}{db_name}.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name} ")
    df = pd.DataFrame(c.fetchall())
    print(df)
    conn.commit()
    conn.close()
    return

def read_table_names(db_name=database_name):
    #connect database
    conn = sqlite3.connect(f"{direction}{db_name}.db")

    # ceate a table
    c = conn.cursor()

    # Create a Table
    c.execute(""" SELECT name from sqlite_master where type= 'table' """)
    # Datatypes:
    user_tables = c.fetchall()[0]
    
    # close our connection
    conn.close()
    return user_tables

if __name__ == '__main__':
    #main()
    #create_sql_database("expenses", "expenses")
    #insert_line("expenses", "expenses", Testzeile)
    fetch_data("expenses", "expenses")

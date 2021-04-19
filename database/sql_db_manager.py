import sqlite3
import pandas as pd

Testzeile = (28.35, "lidl", 50, "grocery", 21, 12, 1990)
direction = "data/"
database_name = "expenses"


def create_sql_database(db_name = database_name):
    #connect database
    conn = sqlite3.connect(f"{direction}{db_name}.db")

    # ceate a table
    c = conn.cursor()
    # Create a Table
    c.execute(f"""CREATE TABLE unique_expenses (
            un_expense_id integer,
            amount integer,
            store text,
            organic_percentage integer,
            category text,
            day integer,
            month integer,
            year integer,
            user_id integer
            )""")
    # Datatypes:
    # Null, integer, real, text, blob

    # commit our command
    conn.commit()
    
    c.execute(f"""CREATE TABLE reoccuring_expenses (
            re_expense_id integer,
            amount integer,
            store text,
            organic_percentage integer,
            category text,
            day integer,
            month integer,
            year integer,
            interval integer,
            user_id integer
            )""")
    conn.commit()
    c.execute(f"""CREATE TABLE users (
            user_id integer,
            username string,
            countries text
            )""")
    conn.commit()

    # close our connection
    conn.close()
    return

def insert_user(content, db_name= database_name, table_name="users"):
    conn = sqlite3.connect(f"{direction}{db_name}.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name} ORDER BY user_id DESC")
    first_line = c.fetchone()
    if first_line is None:
        user_id = 1
    else:
        user_id = str(int(first_line[0])+1)
    c.execute(f"INSERT INTO {table_name} VALUES ({user_id}, ?, ?)", content)
    conn.commit()
    conn.close()
    print("user added")
    return

def insert_line(table_name, content, db_name= database_name):
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

def fetch_data(table_name, db_name=database_name):
    conn = sqlite3.connect(f"{direction}{db_name}.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name} ")
    df = pd.DataFrame(c.fetchall())
    conn.commit()
    conn.close()
    return df

def read_table_names(db_name=database_name):
    #connect database
    conn = sqlite3.connect(f"{direction}{db_name}.db")

    # ceate a table
    c = conn.cursor()

    # Create a Table
    c.execute(""" SELECT name from sqlite_master where type= 'table' """)
    # Datatypes:
    table_df = c.fetchall()
    table_list = [i[0] for i in table_df]
    # close our connection
    conn.close()
    return table_list

if __name__ == '__main__':
    #main()
    #create_sql_database("expenses", "expenses")
    #insert_line("expenses", "expenses", Testzeile)
    fetch_data("expenses", "expenses")

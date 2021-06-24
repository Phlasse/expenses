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
    c.execute(f"""CREATE TABLE variable_expenses (
            variable_expense_id integer,
            amount real,
            store text,
            category text,
            date text
            )""")
    # Datatypes:
    # Null, integer, real, text, blob

    # commit our command
    conn.commit()
    
    c.execute(f"""CREATE TABLE fixed_expenses (
            fixed_expense_id integer,
            amount real,
            organization text,
            category text,
            date text
            )""")
    
    conn.commit()
    
    c.execute(f"""CREATE TABLE periodic_expenses (
            periodic_expense_id integer,
            amount real,
            organization text,
            category text,
            date text,
            period integer
            )""")
    
    conn.commit()
    
    # close our connection
    conn.close()
    return

def fetch_data(table_name, db_name=database_name):
    conn = sqlite3.connect(f"{direction}{db_name}.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name} ")
    df = pd.DataFrame(c.fetchall(), columns=["variable_expense_id","amount","store","category","date"])
    conn.commit()
    conn.close()
    return df

def get_uniques(table, column, db_name=database_name):
    #connect database
    conn = sqlite3.connect(f"{direction}{db_name}.db")

    # ceate a table
    c = conn.cursor()

    # Create a Table
    c.execute(f" SELECT DISTINCT {column} FROM {table}")
    # Datatypes:
    table_df = pd.DataFrame(c.fetchall())
    # close our connection
    conn.close()
    return table_df

def add_variable_expense(content, db_name= database_name, table_name="variable_expenses"):
    conn = sqlite3.connect(f"{direction}{db_name}.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name} ORDER BY variable_expense_id DESC")
    first_line = c.fetchone()
    if first_line is None:
        variable_expense_id = 1
    else:
        variable_expense_id = str(int(first_line[0])+1)
    c.execute(f"INSERT INTO {table_name} VALUES ({variable_expense_id}, ?, ?, ?, ?)", content)
    conn.commit()
    conn.close()
    print("line added")
    return

def change_variable_expense(id, content, table_name="variable_expenses", db_name=database_name):
    conn = sqlite3.connect(f"{direction}{db_name}.db")
    c = conn.cursor()
    print(content)
    c.execute(f"Update {table_name} SET amount={content[0]}, date = {content[3]} WHERE variable_expense_id={id}")
    conn.commit()
    conn.close()
    print("line changed")
    return


def delete_variable_expense(id):
    return

if __name__ == '__main__':
    create_sql_database()


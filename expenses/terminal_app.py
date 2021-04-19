import database.sql_db_manager as dbm
import pandas as pd

def startup():
    print("Welcome to the expense tracker\n")
    try:
        dbm.create_sql_database()
        add_user(True)
        user_id = 1
    except: 
        found_tables = len(dbm.read_table_names())
        if found_tables == 3:
            user_df = dbm.fetch_data("users")
            if user_df.empty:
                add_user(True)
                user_id = 1
            else:
                print("Which user do you want to use?")
                print(0," : ","Create new user")
                for index, row in user_df.iterrows():
                    print(row.user_id, " : ", row.username)
                    user_id = int(input("\n"))
                if user_id == 0:
                    add_user(False)
                    user_id = 1

    return user_id

    
def add_user(first_user=False):
    if first_user is True:
        print("You are the first user of this programm.\n")
    new_name = input("What will be your username?\n\n")
    print("germany is yet the only availbale country.")
    countries = "ger" #input("")
    dbm.insert_user([new_name, countries])
    return new_name

def main():
    user = startup() 
    print(f"So what do you want to do {user}")
    
    
if __name__ == '__main__':
    main()
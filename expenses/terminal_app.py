import database.sql_db_manager as dbm
import pandas as pd

def startup():
    print("Welcome to the expense tracker\n")
    try: 
        user_tables = dbm.read_table_names("expenses")
        print("Which user do you want to use?")
        print(0," : ","Create new user")
        for i in range(len(user_tables)):
            print(i+1," : ",user_tables[i])
        user_choice = int(input("\n"))
        if user_choice == 0:
            user = add_user(False)
        else:
            user = user_tables[user_choice-1]
    except:
        user = add_user(True)
    return user

    
def add_user(first_user=False):
    if first_user is True:
        print("You are the first user of this programm.\n")
    new_name = input("What will be your username?\n\n")
    dbm.create_sql_database(new_name)
    return new_name

def main():
    user = startup() 
    print(f"So what do you want to do {user}")
    
if __name__ == '__main__':
    main()
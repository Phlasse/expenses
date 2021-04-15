import database.sql_db_manager as dbm
import pandas as pd

def startup():
    print("Welcome to the expense tracker\n")
    try: 
        user_df = pd.read_csv("data/user.csv")
    except:
        user_df =pd.DataFrame(columns=["username"])
        user_df.to_csv("data/user.csv")
    if len(user_df.username.to_list()) == 0:
        print("You are new!\n\n")
        add_user()
    else:
    
def add_user(user_df):
    new_name = Input("What will be your username?")
    user_df.username = user_df.to_list().append(new_name)
    user_df.to_csv("data/user.csv")
    return user_df

def main():
    startup() 
        
    
if __name__ == '__main__':
    main()
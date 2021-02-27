import pandas as pd
import datetime

Testzeile = [28.01, "lidl", 50, "grocery", 21, 12, 1990]
direction = "../data/"

def df_dummy(direction):
    df = pd.DataFrame()
    columns = ["id", "amount", "product/store", "organic percentage","category", "day", "month", "year"]
    for i in columns:
        df[i] = [0]
    df.to_csv(f"{direction}expenses_df.csv", index=False)
    return

def load_df(direction):
    df = pd.read_csv(f"{direction}expenses_df.csv")
    return df

def create_backup(df, direction):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M_")
    df.to_csv(f'{direction}backup/{timestamp}_backup.csv')
    return

def add_line(input, df, direction):
    df = load_df(direction)
    new_id = len(df.id)
    new_input = [new_id]+input
    columns = df.columns.tolist()
    new_line_df = pd.DataFrame()
    for index, i in enumerate(new_input):
        new_line_df[columns[index]] = [i]
    new_df = pd.concat([df, new_line_df], axis=0)
    if len(new_df.index)%5 == 0:
        create_backup(new_df, direction)
    new_df.to_csv(f"{direction}expenses_df.csv", index=False)
    return new_df

if __name__ == '__main__':
  # main()

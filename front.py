import streamlit as st
import datetime as dt
import database.sql_db_manager as db
import pandas as pd
today = dt.date.today()
st.sidebar.header("Manage Expenses")

expense_choice = st.sidebar.radio(
    "",
    ('Variable Expenses', 'Fixed Expenses', 'Periodic Expenses', 'Explore Data')
)
########## Variable Expenses    ##############################
if expense_choice == 'Variable Expenses':
    vari_mode = st.sidebar.radio(
        "What do you want to do?",
        ('Add Expense', 'Manage Entries')
    )
    #list_of_stores = ['store_a', 'store_b', "other"]
    list_of_stores = db.get_uniques("variable_expenses", "store")[0].to_list()
    list_of_stores.append("other")
    list_of_categories = db.get_uniques("variable_expenses", "category")[0].to_list()
    list_of_categories.append("other")
    
    if vari_mode == 'Add Expense':
        store = st.selectbox("Which store", list_of_stores)
        if store == "other":
            vari_store = st.text_input("New store?")
        else:
            vari_store = store
        vari_date = st.date_input("Purchase date", dt.date.today(), dt.date(2021, 1, 1), dt.date(2030, 12, 31))
        vari_amount = st.number_input("How much did you spend?") 
        category = st.selectbox("Select a category?", list_of_categories)
        if category == "other":
            vari_category = st.text_input("What kind of expense was it?")
        else:
            vari_category = category
        add_line = st.button("Add Expense?")
        if add_line == True:
            db.add_variable_expense([vari_amount, vari_store, vari_category, str(vari_date)])
    elif vari_mode == "Manage Entries":
        data = db.fetch_data("variable_expenses")
        st.write(data.tail(10))
        st.subheader("Which Entry do yo want to edit?")

        vari_modify = st.selectbox("Choose the entry by id", data.variable_expense_id.to_list())
        
        list_of_stores.append(data.loc[data.variable_expense_id == vari_modify].store.to_list()[0])
        list_of_categories.append(data.loc[data.variable_expense_id == vari_modify].category.to_list()[0])

        new_store = st.selectbox("Change Store?",list_of_stores, index=(len(list_of_stores)-1))
        new_category = st.selectbox("Change Category?",list_of_categories, index=(len(list_of_categories)-1))
        new_amount = st.number_input("Change Amount?", data.loc[data.variable_expense_id == vari_modify].amount.to_list()[0])
        new_date = st.date_input("Change Date?", dt.datetime.strptime(data.loc[data.variable_expense_id == vari_modify].date.to_list()[0], '%Y-%M-%d'), dt.date(2021, 1, 1), dt.date(2030, 12, 31))
        
        variable_change = st.sidebar.button("Commit changes?")
        variable_delete = st.sidebar.button("Delete Expense?")
        if variable_change == True:
            db.change_variable_expense(vari_modify, [new_store, new_category, new_amount, new_date])
        if variable_delete==True:
            db.delete_variable_expense(vari_modify, [new_store, new_category, new_amount, new_date])
        
########## Fixed Expenses       ##############################
elif expense_choice == 'Fixed Expenses':
    fix_mode = st.sidebar.radio(
        "What do you want to do?",
        ('Quick add', 'Regular add', 'Manage Entries')
    )
    
    
########## Periodic Expenses    ##############################
elif expense_choice == 'Periodic Expenses':
    peri_mode = st.sidebar.radio(
        "What do you want to do?",
        ('Quick add', 'Regular add', 'Manage Entries')
    )
    
########## Explore Data         ##############################
elif expense_choice == 'Periodic Expenses':
    st.write('Here will soon be some statistics and stuff')
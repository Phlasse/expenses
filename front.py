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
    standard_stores = ["other", "Lidl", "Aldi", "Rewe", "EDEKA", "Amazon", "Zalando", "About You", "DM", "Rossmann"]
    standard_categories = ["other", "Groceries", "Electronics", "Clothes", "Dining Out", "Business Lunch", "Cosmetics"]
    vari_mode = st.sidebar.radio(
        "What do you want to do?",
        ('Add Expense', 'Manage Entries')
    )
    store_uniques = db.get_uniques("variable_expenses", "store")
    if len(store_uniques) == 0:
        list_of_stores = standard_stores
    else:
        store_uniques = db.get_uniques("variable_expenses", "store")[0].to_list()
        list_of_stores = standard_stores + store_uniques
        list_of_stores = list(set(list_of_stores))
    
    category_uniques = db.get_uniques("variable_expenses", "category")
    if len(category_uniques) == 0:
        list_of_categories = standard_categories
    else:
        category_uniques = db.get_uniques("variable_expenses", "category")[0].to_list()
        list_of_categories = standard_categories + category_uniques
        list_of_categories = list(set(list_of_categories))
    ## add expense
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
    ## manage entries
    elif vari_mode == "Manage Entries":
        data = db.fetch_data("variable_expenses")
        if len(data.variable_expense_id) < 1:
            st.warning("Add a variable expense first!")
        else:
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
                db.change_variable_expense(vari_modify, [new_amount, new_store, new_category, new_date])
            if variable_delete==True:
                db.delete_variable_expense(vari_modify, [new_store, new_category, new_amount, new_date])
                
########## Fixed Expenses       ##############################
elif expense_choice == 'Fixed Expenses':
    standard_organisations = ["Ammerlaender", "Vattenfall", "other", "Telekom", "Gasag", "Vodafone", "DAZN", "Spotify", "Allianz"]
    standard_categories = ["Electricity", "other", "Internet", "Mobile Data", "Media Subscription", "Insurance", "Rent", "Gas"]
    fix_mode = st.sidebar.radio(
        "What do you want to do?",
        ('Add Expense', 'Manage Entries')
    )
    organisation_uniques = db.get_uniques("fixed_expenses", "organization")
    if len(organisation_uniques) == 0:
        list_of_organizations = standard_organisations
    else:
        organisation_uniques = db.get_uniques("fixed_expenses", "organization")[0].to_list()
        list_of_organizations = standard_organisations + organisation_uniques
        list_of_organizations = list(set(list_of_organizations))
    
    category_uniques = db.get_uniques("fixed_expenses", "category")
    if len(category_uniques) == 0:
        list_of_categories = standard_categories
    else:
        category_uniques = db.get_uniques("fixed_expenses", "category")[0].to_list()
        list_of_categories = standard_categories + category_uniques
        list_of_categories = list(set(list_of_categories))
    ## add expense
    if fix_mode == 'Add Expense':
        organisation = st.selectbox("Which organisation", list_of_organizations)
        if organisation == "other":
            fixed_organisation = st.text_input("New organisation?")
        else:
            fixed_organisation = organisation
        fixed_start_date = st.date_input("Start date", dt.date.today(), dt.date(2021, 1, 1), dt.date(2030, 12, 31))
        fixed_amount = st.number_input("How much do you pay monthly?") 
        category = st.selectbox("Select a category?", list_of_categories)
        if category == "other":
            fixed_category = st.text_input("What kind of expense was it?")
        else:
            fixed_category = category
        add_line = st.button("Add Expense?")
        if add_line == True:
            db.add_fixed_expense([fixed_amount, fixed_organisation, fixed_category, str(fixed_start_date)])
    ## manage entries
    elif fix_mode == "Manage Entries":
        data = db.fetch_data("fixed_expenses")
        if len(data.fixed_expense_id) <1:
            st.warning("Add a fixed expense first!")
        else:
            st.write(data.tail(10))
            st.subheader("Which Entry do yo want to edit?")

            fixed_modify = st.selectbox("Choose the entry by id", data.fixed_expense_id.to_list())
            
            list_of_organizations.append(data.loc[data.fixed_expense_id == fixed_modify].organisation.to_list()[0])
            list_of_categories.append(data.loc[data.fixed_expense_id == fixed_modify].category.to_list()[0])

            new_organisation = st.selectbox("Change Store?",list_of_organizations, index=(len(list_of_organizations)-1))
            new_category = st.selectbox("Change Category?",list_of_categories, index=(len(list_of_categories)-1))
            new_amount = st.number_input("Change Amount?", data.loc[data.fixed_expense_id == fixed_modify].amount.to_list()[0])
            new_start_date = st.date_input("Change Date?", dt.datetime.strptime(data.loc[data.fixed_expense_id == fixed_modify].start_date.to_list()[0], '%Y-%M-%d'), dt.date(2021, 1, 1), dt.date(2030, 12, 31))
            
            fixed_change = st.sidebar.button("Commit changes?")
            fixed_delete = st.sidebar.button("Delete Expense?")
            if fixed_change == True:
                db.change_fixed_expense(fixed_modify, [new_amount, new_organisation, new_category, new_start_date])
            if fixed_delete==True:
                db.delete_fixed_expense(fixed_modify, [new_organisation, new_category, new_amount, new_start_date])
    
########## Periodic Expenses    ##############################
elif expense_choice == 'Periodic Expenses':
    standard_organisations = ["ALBA Berlin", "other", "Ammerlaender", "GEZ"]
    standard_categories = ["Season Ticket", "TV-fee", "Insurance", "other"]
    peri_mode = st.sidebar.radio(
        "What do you want to do?",
        ('Add Expense', 'Manage Entries')
    )
    organisation_uniques = db.get_uniques("periodic_expenses", "organization")
    if len(organisation_uniques) == 0:
        list_of_organizations = standard_organisations
    else:
        organisation_uniques = db.get_uniques("periodic_expenses", "organization")[0].to_list()
        list_of_organizations = standard_organisations + organisation_uniques
        list_of_organizations = list(set(list_of_organizations))
    
    category_uniques = db.get_uniques("periodic_expenses", "category")
    if len(category_uniques) == 0:
        list_of_categories = standard_categories
    else:
        category_uniques = db.get_uniques("periodic_expenses", "category")[0].to_list()
        list_of_categories = standard_categories + category_uniques
        list_of_categories = list(set(list_of_categories))
    ## add expense
    if peri_mode == 'Add Expense':
        organisation = st.selectbox("Which organisation", list_of_organizations)
        if organisation == "other":
            periodic_organisation = st.text_input("New organisation?")
        else:
            periodic_organisation = organisation
        periodic_start_date = st.date_input("Start date", dt.date.today(), dt.date(2021, 1, 1), dt.date(2030, 12, 31))
        periodicd_amount = st.number_input("How much do you per period?") 
        category = st.selectbox("Select a category?", list_of_categories)
        if category == "other":
            periodic_category = st.text_input("What kind of expense was it?")
        else:
            periodic_category = category
        period = st.number_input("How big is the period (in months)?", 2, 24, 2)
        add_line = st.button("Add Expense?")
        if add_line == True:
            db.add_periodic_expense([periodicd_amount, periodic_organisation, periodic_category, str(periodic_start_date), period])
    ## manage entries
    elif peri_mode == "Manage Entries":
        data = db.fetch_data("periodic_expenses")
        if len(data.periodic_expense_id) <1:
            st.warning("Add a periodic expense first!")
        else:
            st.write(data.tail(10))
            st.subheader("Which Entry do yo want to edit?")

            periodic_modify = st.selectbox("Choose the entry by id", data.periodic_expense_id.to_list())
            
            list_of_organizations.append(data.loc[data.periodic_expense_id == periodic_modify].organisation.to_list()[0])
            list_of_categories.append(data.loc[data.periodic_expense_id == periodic_modify].category.to_list()[0])

            new_organisation = st.selectbox("Change Store?",list_of_organizations, index=(len(list_of_organizations)-1))
            new_category = st.selectbox("Change Category?",list_of_categories, index=(len(list_of_categories)-1))
            new_amount = st.number_input("Change Amount?", data.loc[data.periodic_expense_id == periodic_modify].amount.to_list()[0])
            new_start_date = st.date_input("Change Date?", dt.datetime.strptime(data.loc[data.periodic_expense_id == periodic_modify].start_date.to_list()[0], '%Y-%M-%d'), dt.date(2021, 1, 1), dt.date(2030, 12, 31))
            new_period = st.number_input("Change Period?", 2,24, data.loc[data.periodic_expense_id == periodic_modify].period.to_list()[0])
            
            periodic_change = st.sidebar.button("Commit changes?")
            periodic_delete = st.sidebar.button("Delete Expense?")
            if periodic_change == True:
                db.change_fixed_expense(periodic_modify, [new_amount, new_organisation, new_category, new_start_date, new_period])
            if periodic_delete==True:
                db.delete_fixed_expense(periodic_modify, [new_organisation, new_category, new_amount, new_start_date, new_period])
    
########## Explore Data         ##############################
elif expense_choice == 'Periodic Expenses':
    st.write('Here will soon be some statistics and stuff')
import expenses.img_processor as pro
import re

def store_identifier(string_list):
    stores = {1:'edeka', 2:'rewe', 3:'lidl', 4:'aldi', 5:'penny', 6:'dm', 7:'rossmann', 8:'kaufland'}
    store_id = 0
    grocery_token = False
    haul = False
    for string in string_list:
        for store_no, store_name in stores.items():
            if store_name is in string:
                grocery_token = True
                store_id = store_no
            else:
                grocery_token = False
                store_id = 0

    if grocery_token == True:
        if store_id == 2:
            haul = rewe_search(string_list)

    return haul

def pivot_foot(string_list):
    haul = False:
    while haul == False:
        haul = store_identifier(string_list)

    return haul

def rewe_search(string_list):
    haul = {'category': 'grocery', 'store':'rewe'}
    sum_regex = re.compile(r'EUR\d\d.\d\d')
    """noch iteriert er nicht ueber die stringlisten"""

    summed_findings =[]
    for i in string_list:
        findings = re.findall(sum_regex, i.replace(' ',''))
        summed_findings.extend(findings)

    print(f"Der Einkauf kostete {summed_findings[0].replace('EUR','').replace(',','.')} Euro")
    return

def identify():
    rewe_search(string_list)
    return

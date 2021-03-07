import re
import numpy as np

def store_identifier(string_list):
    stores = {0:'no store', 1:'edeka', 2:'rewe', 3:'lidl', 4:'aldi', 5:'penny', 6:'rossmann', 7:'kaufland', 8:'dm'}
    store_id = 0
    grocery_token = False
    haul = False
    for string in string_list:
        if grocery_token == True:
            pass
        else:
            for store_no, store_name in stores.items():
                if grocery_token == True:
                    pass

                elif store_name in string:
                    grocery_token = True
                    store_id = store_no
                else:
                    grocery_token = False
                    store_id = 0

    print(stores[store_id])
    if grocery_token == True:
        if store_id == 2:
            haul = rewe_search(string_list)
        else:
            print("no store was identified")
    return haul

def pivot_foot(string_list):
    haul = False
    while haul == False:
        haul = store_identifier(string_list)
        haul = True

    return haul

def rewe_search(string_list):
    print("rewe seach started")
    haul = {'category': 'grocery', 'store':'rewe'}
    sum_regex = re.compile(r'eur\d\d.\d\d')
    date_regex = re.compile(r'\d\d.d\d.\d\d\d\d')
    """noch iteriert er nicht ueber die stringlisten"""

    sum_findings =[]
    date_findings = []
    for i in string_list:
        sum_find = re.findall(sum_regex, i.replace(' ','').replace('br', '').replace('"',''))
        date_find = re.findall(date_regex, i.replace(' ','').replace('br', '').replace('"',''))

        sum_find = [float(string.replace('eur','').replace(',','.')) for string in sum_find]
        sum_findings.extend(sum_find)
        date_findings.extend(date_find)
    haul['sum'] = np.max(sum_findings)
    #haul['date'] = date_findings[0]
    print(haul)
    return haul

def identify(string_list):
    haul = pivot_foot(string_list)
    return

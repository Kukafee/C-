#  -*- encoding:utf-8 -*-

import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def enum_row(row):
    print(row['state'])


def find_state_code(row):
    if row['state'] != 0:
        print(process.extractOne(row['state'], states, score_cutoff=80))
def capital(str):
    return str.capitalize()


def correct_state(row):
    if row['state'] != 0:
        state = process.extractOne(row['state'], states, score_cutoff=80)
        if state:
            state_name = state[0]
            return ' '.join(map(capital, state_name.split(' ')))
    return row['state']

def fill_state_code(row):
    if row['state'] != 0:
        state = process.extractOne(row['state'], states, score_cutoff=80)
        if state:
            state_name = state[0]
            return state_to_code[state_name]
    return ''

def main():
    pd.set_option('display.width', 200)
    pd.set_option('display.max_columns', 200)
    data = pd.read_excel('../3.Data/sales.xlsx', sheet_name='sheet1', header=0)
    # print('data.head() = \n', data.head())
    # print('data.tail = ', data.tail())
    print('data.dtypes = ', data.dtypes)
    print(data)
    print('*'*100)
    # print('data.columns = ', data.columns)
    # for c in data.columns:
    #     print(c, end=' - ')
    data['total'] = data['Jan'] + data['Feb'] + data['Mar']
    print(data.head())
    print(data['Jan'].sum())
    print(data['Jan'].min())
    print(data['Jan'].max())
    print(data['Jan'].mean())

    print('='*100)
    print(data.columns)
    s1 = data[['Jan', 'Feb', 'Mar', 'total']].sum()
    print(s1)
    s2 = pd.DataFrame(data=s1)
    print(s2)
    print(s2.T)
    s3 = s2.T.reindex(columns=data.columns)
    print(s3)
    s = pd.DataFrame(data=data[['Jan', 'Feb', 'Mar', 'total']].sum()).T
    s = s.reindex(columns=data.columns, fill_value=0)
    print(s)
    data = data.append(s, ignore_index=True)
    data = data.rename(index={15:'Totla'})
    print(data)

    print('='*40, 'APPLY', '='*40)
    data.apply(enum_row, axis=1)
    global state_to_code
    state_to_code = {
        "VERMONT": "VT", "GEORGIA": "GA", "IOWA": "IA", "Armed Forces Pacific": "AP", "GUAM": "GU",
        "KANSAS": "KS", "FLORIDA": "FL", "AMERICAN SAMOA": "AS", "NORTH CAROLINA": "NC", "HAWAII": "HI",
        "NEW YORK": "NY", "CALIFORNIA": "CA", "ALABAMA": "AL", "IDAHO": "ID",
        "FEDERATED STATES OF MICRONESIA": "FM",
        "Armed Forces Americas": "AA", "DELAWARE": "DE", "ALASKA": "AK", "ILLINOIS": "IL",
        "Armed Forces Africa": "AE", "SOUTH DAKOTA": "SD", "CONNECTICUT": "CT", "MONTANA": "MT",
        "MASSACHUSETTS": "MA",
        "PUERTO RICO": "PR", "Armed Forces Canada": "AE", "NEW HAMPSHIRE": "NH", "MARYLAND": "MD",
        "NEW MEXICO": "NM",
        "MISSISSIPPI": "MS", "TENNESSEE": "TN", "PALAU": "PW", "COLORADO": "CO",
        "Armed Forces Middle East": "AE",
        "NEW JERSEY": "NJ", "UTAH": "UT", "MICHIGAN": "MI", "WEST VIRGINIA": "WV", "WASHINGTON": "WA",
        "MINNESOTA": "MN", "OREGON": "OR", "VIRGINIA": "VA", "VIRGIN ISLANDS": "VI",
        "MARSHALL ISLANDS": "MH",
        "WYOMING": "WY", "OHIO": "OH", "SOUTH CAROLINA": "SC", "INDIANA": "IN", "NEVADA": "NV",
        "LOUISIANA": "LA",
        "NORTHERN MARIANA ISLANDS": "MP", "NEBRASKA": "NE", "ARIZONA": "AZ", "WISCONSIN": "WI",
        "NORTH DAKOTA": "ND",
        "Armed Forces Europe": "AE", "PENNSYLVANIA": "PA", "OKLAHOMA": "OK", "KENTUCKY": "KY",
        "RHODE ISLAND": "RI",
        "DISTRICT OF COLUMBIA": "DC", "ARKANSAS": "AR", "MISSOURI": "MO", "TEXAS": "TX", "MAINE": "ME"
    }


    global states
    states = list(state_to_code.keys())
    print(states)
    # fuzz.ratio()对位置敏感，全匹配
    print(fuzz.ratio('Python Package', 'PythonPackage'))
    print(fuzz.ratio('Kukafee', 'kukafee'))
    print(fuzz.ratio('KUKAFEE', 'kukafee'))
    print(process.extract('Mississippi', states))
    print(process.extract('Mississippi', states, limit=1))
    print(process.extractOne('Mississippi', states))
    print('+'*100)
    print(data)
    data.apply(find_state_code, axis=1)
    print("*"*100)
    print('Before Correct State:\n', data['state'])
    data['state'] = data.apply(correct_state, axis=1)
    print('After Correct States:\n', data['state'])

    data.insert(5, 'State Code', np.nan)
    print(data)
    data['State Code'] = data.apply(fill_state_code, axis=1)
    print(data)

    print('#'*100)
    print('group by')
    print(data.groupby('State Code'))
    print('All Columns:\n')
    print(data.groupby('State Code').sum())
    print('short Columns:\n')
    print(data[['State Code', 'Jan', 'Feb', 'Mar', 'total']].groupby('State Code').sum())

    data.to_excel('Sales_result.xls', sheet_name='one', index=False)





    pass



if __name__ == "__main__":
    main()
#  -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def enum_row(row):
    print(row['state'])



def main():
    pd.set_option('display.width', 200)
    pd.set_option('display.max_columns', 200)
    data = pd.read_excel('../3.Data/sales.xlsx', sheet_name='sheet1', header=0)
    # print('data.head() = \n', data.head())
    # print('data.tail = ', data.tail())
    # print('data.dtypes = ', data.dtypes)
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
    s = s.reindex(columns=data.columns)
    print(s)
    data = data.append(s, ignore_index=True)
    data = data.rename(index={15:'Totla'})
    print(data)

    print('='*40, 'APPLY', '='*40)
    data.apply(enum_row, axis=1)
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
    states = list(state_to_code.keys())
    print(states)
    # fuzz.ratio()对位置敏感，全匹配
    print(fuzz.ratio('Python Package', 'PythonPackage'))
    print(fuzz.ratio('Kukafee', 'kukafee'))
    print(fuzz.ratio('KUKAFEE', 'kukafee'))
    print(process.extract('Mississippi', states))
    print(process.extract('Mississippi', states, limit=1))
    print(process.extractOne('Mississippi', states))

    data.apply(find_state_code, axis=1)



    pass



if __name__ == "__main__":
    main()
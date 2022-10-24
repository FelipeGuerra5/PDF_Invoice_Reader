from ast import main
from hashlib import new
from operator import index
import pandas as pd
import numpy as np

def setMainCsv():
    try:
        pd.read_csv('main_do_not_use.csv')
    except:

        df = pd.DataFrame(columns=[
            'filename',
            'Issuer',
            # 'Issuer_info',
            'Receiver',
            'Receiver_name',
            'Enumerator_name',
            'CNPJ/CPF',
            'Date_of_emission',
            'Quantity (Ton)',
            'Number',
            'Serie',
            'Access_key'
            ])

        df.to_csv('main_do_not_use.csv')


def openCsv():
    df = pd.read_csv('main_do_not_use.csv')
    return df


def toTable(infos):
    main_df = openCsv()


    rows = []

    c = len(main_df['Issuer'])

    for key in infos:
 
        row_dict = infos[key]

        new_row = []
        new_row.append(c)
        c += 1
        for key in row_dict:
            new_row.append(row_dict[key])  

        main_df.loc[-1] = new_row
        main_df.index += 1
            
    main_df.sort_index()
    main_df.to_csv('main_do_not_use.csv', index=False)
    main_df.to_excel('Base_Nfe.xlsx', index=False)
    
    print(main_df)

if __name__ == '__main__':
    setMainCsv()
    openCsv()
import re
import time
import pandas as pd
import numpy as np

# Status OK
def getIssuer(text):
    result = re.sub(' +', ' ', text)
    text = repr(result)

    idx_start = text.find("recebemos de")
    idx_fin = text.find("os produtos")

    lenght = len('recebemos')

    res = text[idx_start + lenght + 3 :  + idx_fin]

    if res == '':
        res = 'Not Found'

    return res.title()

# Status OK
def getDest(text):

    try:
        r = re.compile('\d\d\d.\d\d\d.\d\d\d-\d\d')
        cpfs = r.findall(text)
        res = cpfs[-1]
    except:
        r = re.compile('\d\d.\d\d\d.\d\d\d/\d\d\d\d-\d\d')
        cnpjs = r.findall(text)
        res = cnpjs[-1]

    return res

# get Dest Name
def getName(cpf):

    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
        
    try:   
        user_id = pd.read_csv('./Atualizar_Planilha_Usuarios/user_id_df.csv', index_col=0)
        line = user_id.loc[user_id['cpf'] == cpf]
        index = line.index[0]
        name = user_id.iloc[index, 1]
        enumerator_name = user_id.iloc[index, 2]
    except:
        name = 'Not Found'
        enumerator_name = 'Not Found'

    return name, enumerator_name

# Status OK
def getCnpj(text):
    param = "cnpj / cpf"
    idx_start = text.find(param)
    text[idx_start + len(param) + 1 : ]

    try:
        r = re.compile('\d\d.\d\d\d.\d\d\d/\d\d\d\d-\d\d')
        cnpj = r.findall(text)
        # cnpj = set(cnpj)
        res = cnpj[0]
        
    except:
        r = re.compile("\d\d\d.\d\d\d.\d\d\d-\d\d")
        cpf = r.findall(text)

        # cpf = set(cpf)
        res = cpf[0]
    return res

# Status OK
def getEmission(text):
    
    try:
        r = re.compile("\d\d/\d\d/\d\d\d\d")
        date = r.findall(text)
    except:
        r = re.compile("\d\d-\d\d-\d\d\d\d")
        date = r.findall(text)

    try:
        res = date[1]
    except:
        res = date[0]


    return res



# Invoice 5 couldn't get quantity
def getQuantity(text):
    r = re.compile('\skg.*')
    amounts = r.findall(text)

    q = len(amounts)
    string = ''

    last  = text[-1]
    base = text.rfind(last)

    counter = 0
    value = int(0)
    for i in range(q):
        
        base = text[ : base].rfind('kg')
        
        start = text[base + 1 : ].find('\n')
        start = start + base + 1

        end = text[start + 1 : ].find('\n')
        end = end + start + 1

        # substring = str(f'Quantidade nº {i + 1}: ({text[start : end]} Kg); \n')
        amount = text[start + 1: end]
        print(f'amount {counter + 1} {amount}')
        fin = amount.find(',')
        amount = amount[ : fin]
        amount = amount.replace('.', '')
        amount = int(amount)
        value += amount
        print(f'amount after sum {value}')
        counter += 1

    res = value/1000
    print(f'res = {res} ')

    return res



# invoices 4 and 8 got it with str(serie) at the end
def getNumber(text):
    # Número
    param = "nº"
    idx_start = text.find(param)
    idx_fin = text[idx_start : ].find('\n')
    lenght = len(param)
    num = text[ idx_start + lenght + 1 : idx_start +idx_fin]

    # Number with '-'
    dash = num.find('-')
    if dash == -1:
        pass
    elif dash > 0:
        num = num[ : dash - 1]

    # num to int
    try:
        num = num.replace('.', '')
        num = int(num)
    except:
        if num == '':
            num = 'Not Found'

    # Série:
    param = "série"

    idx_start = text.find(param)
    second_idx_start = text[idx_start : ].find(' ')
    idx_fin = text[idx_start + second_idx_start : ].find('\n')
    lenght = len(param)
    serie = text[idx_start + second_idx_start : idx_start + second_idx_start + idx_fin]

    try:
        serie = int(serie)
    except:
        serie = 'Not found'

    return (num, serie)

#  Status OK
def getKey(text):
    r = re.compile('\d\d\d\d\s\d\d\d\d\s\d\d\d\d\s\d\d\d\d\s\d\d\d\d\s\d\d\d\d\s\d\d\d\d\s\d\d\d\d\s\d\d\d\d\s\d\d\d\d\s\d\d\d\d')
    res = r.findall(text)
    res = res[0]

    return res


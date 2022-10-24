
# Imports
import fitz
from openfiles import openFiles

from parameters import getIssuer, getDest, getCnpj, getEmission, getKey, getNumber, getQuantity, getName


def readFiles(files):

    infos = {}

    for n, file in enumerate(files):


        with fitz.open(file) as doc:
            text = ""
            for page in doc:
                text += page.get_text()

        nfe_title = file[file.rfind('/') + 1 : ]
        
        print(nfe_title)

        text = text.lower()
        
        info = getInfo(text, nfe_title)
        infos[nfe_title] = info

    return infos
    

def getInfo(text, filename):

    info = {}


    info['Filename'] = filename
    info['Issuer'] = getIssuer(text)
    # info['info_sender'] = ''
    info['Receiver'] = getDest(text)
    (info['Receiver_name'], info['Enumerator_name']) = getName(info['Receiver'])
    info['CNPJ/CPF'] = getCnpj(text)
    info['Date_emission'] = getEmission(text)
    info['Quantity (Ton)'] = getQuantity(text)
    (info['Number'], info['series']) = getNumber(text)
    info['Access_key'] = getKey(text)

    return info


if __name__ == "__main__":
    print('readfiles')
import fitz
import easygui

from parameters import getIssuer, getDest, getCnpj, getEmission, getKey, getNumber, getQuantity, getName


def readFiles(files):

    infos = {}

    for n, file in enumerate(files):

        nfe_title = file[file.rfind('/') + 1 : ]
        try:    
            with fitz.open(file) as doc:
                pages = []
                for page in doc:
                    text = page.get_text()
                    text = text.lower()
                    pages.append(text)
                    print(f'[PAGE TEXT] {text}')
            # test for multiple.

            
            print(nfe_title)

            
            for i, page in enumerate(pages):
                filename = f'{nfe_title}_{i + 1}'
                try:
                    info = getInfo(page, filename)
                except:
                    alertUser(filename)
                print(f'[PAGE] {page}')
                infos[f'{nfe_title}_{i + 1}'] = info

            print(f'[INFOS] {infos}')

            return infos
            
        except:
            alertUser(nfe_title)
    

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

def alertUser(file_name):
    msg = f'O arquivo:\n\n [ {file_name.title()} ] \n\nNão pode ser lido!'
    easygui.msgbox(msg, title="Alerta!")


if __name__ == "__main__":
    print('readfiles')
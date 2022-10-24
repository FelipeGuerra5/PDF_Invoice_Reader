from openfiles import openFiles
from readfile import readFiles
from format_n_table import toTable, setMainCsv


def execute():
    
    files = openFiles()
    infos = readFiles(files)
    for item in infos:
        print('\n[START OF FILE]' + '-'* 30 + '[START OF FILE]\n')
        print(f'[FILE NAME] {infos[item]} ')
        # print(f'[FILE TYPE] {dic[invoice].file_type} ')
        # print(f'[LINE DATA] {dic[invoice].file_data} ')
        print('\n[END OF FILE]' + '-'* 30 + '[END OF FILE]\n')
    setMainCsv()
    toTable(infos)
    
    
if __name__ == '__main__':
    execute()
    
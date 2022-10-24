from openfiles import openFiles
from readfile import readFiles
import parameters
from format_n_table import toTable, setMainCsv


def execute():
    
    files = openFiles()
    infos = readFiles(files)
    setMainCsv()
    toTable(infos)
    
    
if __name__ == '__main__':
    execute()
    
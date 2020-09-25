import pandas as pd
from os import getcwd



def getContactMatrices():
    matrixPath = 'model/data/NLmatrices4x4.xlsx'
    c = list()

    overall = pd.read_excel(matrixPath, sheet_name='NL_all_locations')
    home = pd.read_excel(matrixPath, sheet_name='NL_home')
    work = pd.read_excel(matrixPath, sheet_name='NL_work')
    school = pd.read_excel(matrixPath, sheet_name='NL_school')
    other = pd.read_excel(matrixPath, sheet_name='NL_other')
    c = [overall,home,work,school,other]
    return c

def getPop():
    popTable = pd.read_excel('data/NLdemographics.xlsx',sheet_name='4x4')
    popTable = popTable.set_index('Age')
    return popTable.iloc[:,3],popTable 



getContactMatrices()
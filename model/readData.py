import pandas as pd
from posix import getcwd

def getContactMatrices():
    c = list()
    overall = pd.read_excel('model/data/NLmatrices4x4.xlsx', sheet_name='NL_all_locations')
    home = pd.read_excel('model/data/NLmatrices4x4.xlsx', sheet_name='NL_home')
    work = pd.read_excel('model/data/NLmatrices4x4.xlsx', sheet_name='NL_work')
    school = pd.read_excel('model/data/NLmatrices4x4.xlsx', sheet_name='NL_school')
    other = pd.read_excel('model/data/NLmatrices4x4.xlsx', sheet_name='NL_other')
    c = [overall,home,work,school,other]
    return c

def getPop():
    popTable = pd.read_excel('model/data/NLdemographics.xlsx',sheet_name='4x4')
    popTable = popTable.set_index('Age')
    return popTable.iloc[:,3],popTable 

    
pop,popTable = getPop()
c = getContactMatrices()
print(pop)
print(popTable)


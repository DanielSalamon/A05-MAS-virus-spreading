import pandas as pd
from os import getcwd



def getContactMatrices():
    matrixPath = 'data/NLmatrices4x4.xlsx'
    c = list()

    overall = pd.read_excel(matrixPath, sheet_name='NL_all_locations',header=None).values
    home = pd.read_excel(matrixPath, sheet_name='NL_home',header=None).values
    work = pd.read_excel(matrixPath, sheet_name='NL_work',header=None).values
    school = pd.read_excel(matrixPath, sheet_name='NL_school',header=None).values
    other = pd.read_excel(matrixPath, sheet_name='NL_other',header=None).values
    c = [overall,home,work,school,other]
    return c

def getPop():
    popTable = pd.read_excel('data/NLdemographics.xlsx',sheet_name='4x4').values
    return popTable[:,4]

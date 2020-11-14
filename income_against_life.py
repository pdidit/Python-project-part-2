# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 23:45:52 2020

@author: padra
"""

def compareIncomeLife(incomedata, yeardata):
    
    averageIncome = sum(incomedata) / len(incomedata)
    averageYear = sum(yeardata) / len(yeardata)
    
    devIncome = [x - averageIncome for x in incomedata ]
    devYear = [y - averageYear for y in yeardata]
    
    sqrDevIncome = {(x - averageIncome) ** 2 for x in incomedata}
    sqrDevYear = {(x - averageYear) ** 2 for x in yeardata}
    

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:40:05 2020

@author: padra
"""

from math import sqrt
def yearlyStats(yearList, year):
    """
    Thie function is descigned to look at the stats for a particular year

    Parameters
    ----------
    yearList : List
        a list of the life expectancy for the year
    year : int
        the year that we are examining 

    Returns
    -------
    None.

    """
    averageExpectedLife = sum(yearList)/len(yearList)
    deviation = [x - averageExpectedLife for x in yearList]
    sqrDeviation = [(x - averageExpectedLife) ** 2 for x in yearList]
    standardDev = sqrt(sum(sqrDeviation)/(len(yearList)-1))
    
    print(f"The average Life expectancy for the year {year}: {averageExpectedLife:.2f} " ) 
    print(f"The standard deviation Life expectancy for the year {year}: {standardDev} " )
    print(f"the range of life expectancy for the year {year} is from {min(yearList)} and {max(yearList)}")
    

if __name__ == "__main__":
    yearlyStats([234,3453,134,1234,1234,1234,1234,1234,51], 2009) 
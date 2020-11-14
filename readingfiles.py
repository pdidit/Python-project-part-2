# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def readFiles(file):
    """
    

    Parameters
    ----------
    file : TYPE
        DESCRIPTION.

    Returns
    -------
    output : TYPE
        DESCRIPTION.

    """
    output =[]
    country = []
    year2000 = []
    year2001 = []
    year2002 = []
    year2003 = []
    year2004 = []
    year2005 = []
    year2006 = []
    year2007 = []
    year2008 = []
    year2009 = []
    year2010 = []
    year2011 = []
    year2012 = []
    year2013 = []
    year2014 = []
    year2015 = []
    year2016 = []
    year2017 = []
    year2018 = []
    year2019 = []
    try:
        with open(file) as life_data:
            life_data.readline()
            
            for line in life_data:
                try:
                    cty=""
                    yr00=0.0
                    yr01=0.0
                    yr02=0.0
                    yr03=0.0
                    yr04=0.0
                    yr05=0.0
                    yr06=0.0
                    yr07=0.0
                    yr08=0.0
                    yr09=0.0
                    yr10=0.0
                    yr11=0.0
                    yr12=0.0
                    yr13=0.0
                    yr14=0.0
                    yr15=0.0
                    yr16=0.0
                    yr17=0.0
                    yr18=0.0
                    yr19=0.0
                                                            
                    cty, yr00, yr01, yr02, yr03, yr04, yr05, yr06, yr07, yr08, yr09, yr10, yr11, yr12, yr13, yr14, yr15, yr16, yr17, yr18, yr19 = line.split(",")
        
                    country.append(cty)
                    year2000.append(float(yr00))
                    year2001.append(float(yr01))
                    year2002.append(float(yr02))
                    year2003.append(float(yr03))
                    year2004.append(float(yr04))
                    year2005.append(float(yr05))
                    year2006.append(float(yr06))
                    year2007.append(float(yr07))
                    year2008.append(float(yr08))
                    year2009.append(float(yr09))
                    year2010.append(float(yr10))
                    year2011.append(float(yr11))
                    year2012.append(float(yr12))
                    year2013.append(float(yr13))
                    year2014.append(float(yr14))
                    year2015.append(float(yr15))
                    year2016.append(float(yr16))
                    year2017.append(float(yr17))
                    year2018.append(float(yr18))
                    year2019.append(float(yr19))               
                   
                except ValueError:
                    print("there is value error")
    except FileNotFoundError:
        print("there was an issue with accessing the file")
    output.append(country)
    output.append(year2000)
    output.append(year2001)
    output.append(year2002)
    output.append(year2003)
    output.append(year2004)
    output.append(year2005)
    output.append(year2006)
    output.append(year2007)
    output.append(year2008)
    output.append(year2009)
    output.append(year2010)
    output.append(year2011)
    output.append(year2012)
    output.append(year2013)
    output.append(year2014)
    output.append(year2015)
    output.append(year2016)
    output.append(year2017)
    output.append(year2018)
    output.append(year2019)
    print("file has downloaded:"+file)
    return output
    
    
if __name__ ==  "__main__":
    readFiles("income_for_project.csv")
            
       # with open("income_for_project.csv") as income_data:
            
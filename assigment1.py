# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 21:35:26 2020

@author: padra
"""

from math import sqrt
files = ["life_projects.csv", "income_for_project.csv"]
income_data = []
life_expectancy = []
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
for file in files:
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
                    line.strip()
                    if line.find("Congo") != -1 or line.find("Micronesia") != -1:
                        cty1=""
                        cty2=""
                        cty1, cty2, yr00, yr01, yr02, yr03, yr04, yr05, yr06, yr07, yr08, yr09, yr10, yr11, yr12, yr13, yr14, yr15, yr16, yr17, yr18, yr19 = line.split(",")
                        cty= cty1+","+cty2
                    elif line.find(",,") != -1:
                        line = line.replace(',,', ' ')
                        cty, yr00, yr01, yr02, yr03, yr04, yr05, yr06, yr07, yr08, yr09, yr10, yr11, yr12, yr13, yr14, yr15, yr16, yr17 = line.split(",")
                        yr18 = 0
                        yr19 = 0
                    else:
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
    if file == "life_projects.csv":
        life_expectancy.append(country)
        life_expectancy.append(year2000)
        life_expectancy.append(year2001)
        life_expectancy.append(year2002)
        life_expectancy.append(year2003)
        life_expectancy.append(year2004)
        life_expectancy.append(year2005)
        life_expectancy.append(year2006)
        life_expectancy.append(year2007)
        life_expectancy.append(year2008)
        life_expectancy.append(year2009)
        life_expectancy.append(year2010)
        life_expectancy.append(year2011)
        life_expectancy.append(year2012)
        life_expectancy.append(year2013)
        life_expectancy.append(year2014)
        life_expectancy.append(year2015)
        life_expectancy.append(year2016)
        life_expectancy.append(year2017)
        life_expectancy.append(year2018)
        life_expectancy.append(year2019)
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
    elif file == "income_for_project.csv":
        income_data.append(country)
        income_data.append(year2000)
        income_data.append(year2001)
        income_data.append(year2002)
        income_data.append(year2003)
        income_data.append(year2004)
        income_data.append(year2005)
        income_data.append(year2006)
        income_data.append(year2007)
        income_data.append(year2008)
        income_data.append(year2009)
        income_data.append(year2010)
        income_data.append(year2011)
        income_data.append(year2012)
        income_data.append(year2013)
        income_data.append(year2014)
        income_data.append(year2015)
        income_data.append(year2016)
        income_data.append(year2017)
        income_data.append(year2018)
        income_data.append(year2019)
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
    print("file has downloaded:"+ file)

option1file = "default1.csv"
option2file = "dafault2.csv"
option3file = "default3.csv"
while True:
    print()
    print("Welcome to Analysis tool to look at life expectancy.")
    print("1. To look as stat of life expectancy for a particular year.")
    print("2. To Sort list based on life expectancy or income.")
    print("3. Provide a correlation for country based on life expectancy against income.")
    print("4. Print out a list of the countries that can be examined.")
    print("5. Allows the user to change the name of output files.")
    print("0. Exit the tool")
    
    try:
        option = int(input("Which option do you wish to examine? "))
        if option == 1:
            yearToExam = int(input("What year do you wish to examine? "))
            if yearToExam >= 2000 and yearToExam <= 2019:
                yearindex = yearToExam - 1999
                yearexam =[]
                yearexam = life_expectancy[yearindex]
                try: 
                    yearexam.remove(0.0)
                    yearexam.remove(0.0)
                    yearexam.remove(0.0)
                except ValueError:
                    print("")
                averageExpectedLife = sum(yearexam)/len(yearexam)
                deviation = [x - averageExpectedLife for x in yearexam ]
                sqrDeviation = [(x - averageExpectedLife) ** 2 for x in yearexam]
                standardDev = sqrt(sum(sqrDeviation)/(len(yearexam)-1))
                
                frequencies = {}
                for value in life_expectancy[yearindex]:
                    if not value in frequencies:
                        frequencies[value] = 1
                    else:
                        frequencies[value] += 1
                    
                modeYear = max(frequencies, key=frequencies.get)
                print(f"The average Life expectancy for the year {yearToExam}: {averageExpectedLife:.2f} " ) 
                print(f"The mode for the {yearToExam} is {modeYear}")
                print(f"The range of life expectancy for the year {yearToExam} is from {min(yearexam)} and {max(yearexam)}")
                print(f"The standard deviation Life expectancy for the year {yearToExam}: {standardDev}" )
                
                t=[]
                try:
                    with open(option1file, 'a') as out_file:
                        t.append(yearToExam)
                        t.append(min(yearexam))
                        t.append(max(yearexam))
                        t.append(modeYear)
                        t.append(averageExpectedLife)
                        t.append(standardDev)
                        s = str(t)
                        s.strip('[')
                        s.strip(']')
                        
                        out_file.write(s)
                        out_file.write("\n")
                except FileNotFoundError:
                     print("file not found")
            else:
                print("That is the wrong year " , yearToExam)
        elif option == 2:
            yearToExam2 = int(input("What year do you wish to examine? "))
            if yearToExam >= 2000 and yearToExam <= 2019:
                sort1 = int(input("How would you like to sort (1 life expancy 2. income)? "))
                if sort1 == 1 or sort1 == 2:
               
                    yearindex = yearToExam2 - 1999
                    copiedtable=[]
                    sortBy = ""
                    for country in life_expectancy[0]:
                        copiedtable.append(income_data[yearindex][income_data[0].index(country)])
                    
                    comparelist = sorted(zip(life_expectancy[0], life_expectancy[yearindex], copiedtable), key=lambda x: x[sort1])
                    if sort1 == 1:
                        sortBy = "Life Expectancy"
                    elif sort1 == 2:
                        sortBy = "Income"
                    try:
                        with open(option2file, 'a') as out_file2:
                            out_file2.write("This is sort by " + sortBy + "for the year " + str(yearToExam2) + ".\n")
                            for name in comparelist:
                                print(name) 
                                out_file2.write(str(name))
                                out_file2.write("\n")
                            out_file2.write("\n")
                    except FileNotFoundError:
                        print("file is not found")
                    
                    
                elif sort1 != 2 and sort1 != 1:
                    print("This is not the correct selection")
            else:
                print("This is a incorrect year")
        elif option == 3:
            selection3Country=input("What is the country you want to examine? ")
            lifeIndex = life_expectancy[0].index(selection3Country)
            incomeindex = income_data[0].index(selection3Country)
            life2 = []
            income2=[]
            for i in range(2000, 2020):
                life2.append(life_expectancy[i-1999][lifeIndex])
                income2.append(income_data[i-1999][incomeindex])
            try: 
                life2.remove(0.0)
                life2.remove(0.0)
                del income2[-1]
                del income2[-1]
            except ValueError:
                    print("")
                    
            life_mean = sum(life2)/len(life2)
            income_mean = sum(income2)/len(income2)
            
            income_dev = [x - income_mean for x in income2]
            life_dev = [y + life_mean for y in life2]
            
            life_income_deviations = [ x*y for (x,y) in zip(income_dev, life_dev)]
            
            income_sqr_dev = [ ( x - income_mean) ** 2 for x in income2]
            life_sqr_dev = [ ( y - life_mean ) ** 2 for y in life2]
            
            correlation = sum(life_income_deviations)/(sqrt(sum(income_sqr_dev))*sqrt(sum(life_sqr_dev)))
            
            print(f"The correlation for {selection3Country} is {correlation}")
            
            try:
                with open(option3file, 'a') as out_file:
                    out_file.write(selection3Country + "," + str(correlation) + "\n")
            except FileNotFoundError:
                print("file was not found")
        elif option == 4:
            for country in life_expectancy[0]:
                print(country)
        elif option == 5:
            option5=int(input("Which file name do you want to change? "))
            if option5 == 1:
                option1file = input("Please put the file name for option 1: ")
            elif option5 == 2:
                option2file = input("Please put the file name for option 2: ")
            elif option5 == 3:
                option3file = input("Please put the file name for option 3: ")
        elif option == 0:
            print("Thank you for using this tool.")
            break
        else:
            print("Your selection is incorrect. Please check again.")
    except ValueError:
        print("There was an incorrect entry!!!!  Please check the options again")
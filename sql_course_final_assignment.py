# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 23:21:16 2025

@author: Tatiana Shousterman
"""

import sqlite3 
import pandas as pd
con = sqlite3.connect("FinalDB.db")
cur = con.cursor() 

chicago_census_df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01')
chicago_school_df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01')
chicago_crime_df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01')




"""SQL Magic in SpyderIDE """ 

%load_ext sql

%sql sqlite:///FinalDB.db

""" Load the dataframes to rhe database as tables """ 
chicago_census_df.to_sql("CENSUS_DATA", con, if_exists='replace', index=False,method="multi")
chicago_school_df.to_sql("CHICAGO_PUBLIC_SCHOOLS", con, if_exists='replace', index=False,method="multi")
chicago_crime_df.to_sql("CHICAGO_CRIME_DATA", con, if_exists='replace', index=False,method="multi")

"""find total number of crimes in crime table"""
query1= '''SELECT COUNT(ID) FROM CHICAGO_CRIME_DATA'''

#query1 = ''' SELECT * FROM CHICAGO_CRIME_DATA'''
#statement = '''SELECT * FROM INSTRUCTOR'''
cur.execute(query1)

sum1 = cur.fetchall()

query2 = '''SELECT COMMUNITY_AREA_NUMBER,COMMUNITY_AREA_NAME FROM CENSUS_DATA WHERE PER_CAPITA_INCOME<11000 '''
cur.execute(query2)

out2 = cur.fetchall()
print(out2)

""" List all case numbers for crimes involving minors?
(children are not considered minors for the purposes of crime analysis)"""


query3 = ''' '''


query4 = '''SELECT * FROM CHICAGO_CRIME_DATA WHERE PRIMARY_TYPE=='KIDNAPPING' '''
cur.execute(query4)
out4 = cur.fetchall()
print(out4)

"""list kind of crimes that were reported at schools """
query5 = '''SELECT DISTINCT PRIMARY_TYPE,DESCRIPTION FROM CHICAGO_CRIME_DATA WHERE LOCATION_DESCRIPTION LIKE '%School%'  ''' 
cur.execute(query5)
out5 = cur.fetchall()
print(out5)

"""Problem 6
List the type of schools along with the average safety score for each type"""

query6 = ''' SELECT NAME_OF_SCHOOL FROM CHICAGO_PUBLIC_SCHOOLS GROUP BY 'ELEMENTARY, MIDDLE, OR HIGH SCHOOL' \
    WHERE SAFETY_SCORE > (SELECT AVG(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS) '''

query6 = '''SELECT NAME_OF_SCHOOL 
FROM CHICAGO_PUBLIC_SCHOOLS 
GROUP BY 'ELEMENTARY, MIDDLE, OR HIGH SCHOOL'
HAVING SAFETY_SCORE > (SELECT AVG(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS);'''

query6 = '''SELECT "Elementary, Middle, or High School", AVG(SAFETY_SCORE) AS avg_safety_score
FROM CHICAGO_PUBLIC_SCHOOLS
GROUP BY "Elementary, Middle, or High School" ''';
cur.execute(query6)
out6=cur.fetchall()
print(out6)

SELECT COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA WHERE COUNT(COMMUNITY_AREA_NUMBER) == MAX(COUNT(COMMUNITY_AREA_NUMBER)) 
query7 = '''SELECT COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA WHERE COUNT(COMMUNITY_AREA_NUMBER) == MAX(COUNT(COMMUNITY_AREA_NUMBER)) 
  ''' 
cur.execute(query7)
out7=cur.fetchall()
print(out7)



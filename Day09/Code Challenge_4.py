#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import requests
#import urllib



#specify the url
wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())



right_table = soup.find('table', class_='table')

print (right_table.prettify())


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]


for row in right_table.findAll('tr'):
    # first row has no TH, but other rows have one TH and 6 TD
    cells = row.findAll('td') 
   
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        #skip the sequence number column
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
       


from collections import OrderedDict

col_name = ["Pos","Team","WeightedMatches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))


# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")



import sqlite3
from pandas import DataFrame


# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'cricket.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE employees(
          pos INTEGER,
          Team  TEXT,
          Weighted_Matches INTEGER,
          Pointer INTEGER,
          Rating INTEGER
          )""")


for i in range(0,len(A)):
    c.execute("INSERT INTO employees VALUES ('{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i]))
    

df = DataFrame(c.fetchall())
c.execute("SELECT * FROM employees")
df.columns = ["Pos","Team","Weighted_Matches","Points","Rating"]




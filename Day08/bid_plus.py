
import pandas as pd
from selenium import webdriver

wiki = "https://bidplus.gem.gov.in/bidlists"


#driver = webdriver.Chrome("C:/Users/rohit/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome("C:\\Users\\Shiv Mohan\\Downloads\\chromedriver.exe")

driver.get(wiki)   # Opening the submission url



right_table=driver.find_element_by_class_name('wikitable')


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())

//*[@id="pagi_content"]/div[1]


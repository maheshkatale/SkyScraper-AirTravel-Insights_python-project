from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

serv_obj=Service("C:\Program Files (x86)\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.kayak.co.in/flights")
driver.implicitly_wait(10)
print(driver.title)
selector='.react-navigation-column~ .react-navigation-column+ .react-navigation-column li:nth-child(2) .HKWm-mod-theme-default'
link=driver.find_element(By.CSS_SELECTOR,selector)
print(link.text)
link.click()
driver.implicitly_wait(5)
ls=driver.find_elements(By.CLASS_NAME,"c-P1H-row")
list=[]
for i in ls:
    list.append(i.text.split("\n"))
column_name=list[0][1:]
list=list[1:]
df=pd.DataFrame([sublist[1:] for sublist in list],columns=column_name,index=range(1,len(list)+1))
df.to_csv("List_Of_Airlines.csv")
print("Done")
driver.close()
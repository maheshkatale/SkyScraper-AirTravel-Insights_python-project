from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

serv_obj=Service("C:\Program Files (x86)\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.kayak.co.in/flights")
print(driver.title)

ls=driver.find_elements(By.CLASS_NAME,"P_Ok-title")
driver.implicitly_wait(10)
list=[]
for i in ls:
    list.append(i.text)
df=pd.DataFrame({'List of Flights':list},index=range(1,len(list)+1))
df.to_csv("List_Of_Flights.csv")
print("Done")
driver.close()
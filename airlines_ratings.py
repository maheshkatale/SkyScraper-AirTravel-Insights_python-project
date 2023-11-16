from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

serv_obj=Service("C:\Program Files (x86)\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.kayak.co.in/flights")
driver.implicitly_wait(5)
print(driver.title)
selector1='.react-navigation-column~ .react-navigation-column+ .react-navigation-column li:nth-child(2) .HKWm-mod-theme-default'
link=driver.find_element(By.CSS_SELECTOR,selector1)
print(link.text)
link.click()
selector2='.c-P1H-code-container+ .c-P1H-cell .acPF-mod-enabled'
ls=driver.find_elements(By.CSS_SELECTOR,selector2)
list=[]
for i in range(len(ls)):
    sublist=[]
    ls=driver.find_elements(By.CSS_SELECTOR,selector2)
    driver.implicitly_wait(5)
    sublist.append([ls[i].text])
    ls[i].click()
    driver.implicitly_wait(2)
    selector3='.overall__review-count , .overall__score--fresh , .col-score'
    ratings=driver.find_elements(By.CSS_SELECTOR,selector3)
    for rating in ratings:
        sublist.append(rating.text.split("\n"))
    list.append([item for nlist in sublist for item in nlist])
    driver.implicitly_wait(2)
    driver.back()
column_name=['Airline','Overall Rating','Reviews','Boarding','Comfort','Crew','Entertainment','Food']
df=pd.DataFrame([sublist[:] for sublist in list],columns=column_name,index=range(1,len(list)+1))
df['Reviews'] = df['Reviews'].replace(r'[^\d]', '', regex=True)
df.to_csv("Airline_ratings.csv")

driver.quit()
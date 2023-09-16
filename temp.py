import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By

dff = pd.DataFrame(columns=['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Address', 'Salary Range', 'Date Posted', 'Rating', 'Site', 'URL'])

url = "https://www.foundit.in/srp/results?locations=india"

page = requests.get(url)
# print(page.text)

# Making the Driver Headless: (next 3 lines)
driver = webdriver.Chrome()
driver.headless = True

# time.sleep(3)

# driver = webdriver.Chrome()
driver.get(url)
  
driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/section[2]/div[1]/div[2]/span/span[2]/p').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/section[2]/div[1]/div[2]/span/span[2]/ul/li[2]').click()

time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html5lib')

# print(soup.prettify())

results = soup.find(class_='list')
job_elems=results.find_all('article', class_='jobTuple')

  # print(job_elems)
pages = np.arange(1,26)

for pages in pages:
  for job_elem in job_elems:
    # Post Title
    T = job_elem.find('a',class_='title ellipsis')
    Title=T.text
    # print("Job Title: " + Title.text)
    # print(Title)

    D = job_elem.find('dev', class_='ellipsis job-description')
    Description = D

    # Experience
    E = job_elem.find('span', class_='ellipsis fleft expwdth')
    if E is None:
      Exp = "Not-Mentioned"
    else:
      Exp = E.text
    print(Exp)
    # print('Experience: ' + Exp.text)
    # print(" "*2)

    # Company
    C = job_elem.find('a', class_='subTitle ellipsis fleft')
    Company=C.text
    # print("Company: " + Company.text)
    
    # City
    C2 = job_elem.find('span', class_='ellipsis fleft locWdth')
    City=C2

    # Address
    A = job_elem.find('span', class_='ellipsis fleft locWdth')
    Address=A

    # Salary Range
    S = job_elem.find('span', class_='ellipsis fleft')
    Salary=S.text

    # Date Posted
    D = job_elem.find('span', class_='fleft postedDate')
    Date=D.text

    # Rating
    R = job_elem.find('span',class_='starRating fleft dot')
    Rating = R

    # Site
    S = 'Naukri.com'
    Site=S

    U = job_elem.find('a',class_='title ellipsis').get('href')
    URL = U
    # print(URL)

    # df=df.append({'Title':Title, 'Company':Company,'URL':URL}, ignore_index = True)
    # df = pd.DataFrame([[Title, Company, URL]], columns=['Title','Company','URL'])
    dff = pd.concat([dff, pd.DataFrame([[Title, Description, Exp, Company, City, Address, Salary, Date, Rating, Site, URL]], columns = ['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Address', 'Salary Range', 'Date Posted', 'Rating', 'Site', 'URL'])], ignore_index=True)
    print(dff)
    # Second Way using Concat:
    # df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    # df3 = pd.concat([df3, df2], ignore_index=True)
    # dff.to_csv("Naukri.com_Data_Collection.csv", index = False)
    dff.to_excel("New_Outputss.xlsx", index = False)
    
    
  
  driver.execute_script("window.scrollTo(0,(document.body.scrollHeight) - 1500)")

  time.sleep(0.5)

  # script = 'your JavaScript goes here'
  # element = driver.find_element_by_*('your element identifier goes here')
  # driver.execute_script(script, element)
  driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/section[2]/div[3]/div/a[2]  ').click()
  # /html/body/div[1]/div[4]/div/div/section[2]/div[3]/div/a[2]
  # //*[@id="root"]/div[4]/div/div/section[2]/div[3]/div/a[2]

  time.sleep(0.5)


time.sleep(15)
driver.close()




# driver.close() #END OPERATION
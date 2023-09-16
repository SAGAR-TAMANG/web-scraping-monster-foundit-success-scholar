from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By

dff = pd.DataFrame(columns=['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Address', 'Salary Range', 'Date Posted', 'Rating', 'Site', 'URL'])

url = "https://www.foundit.in/srp/results?locations=india"

# time.sleep(3)

driver = webdriver.Chrome()
driver.get(url)

# Clicking the stuff
# driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/section[2]/div[1]/div[2]/span/span[2]/p').click()
# driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/section[2]/div[1]/div[2]/span/span[2]/ul/li[2]').click()

soup = BeautifulSoup(driver.page_source,'html5lib')

# print(soup.prettify())

results = soup.find(class_='srpResultCard')
job_elems=results.find_all('div', class_='srpResultCardContainer')

pages = np.arange(1,100000)

# for pages in pages: 
for job_elem in job_elems:
  # Post Title
  # T = job_elem.find('div',class_='jobTitle')
  # Title=T.text
  # print(Title)

  # # # No description found
  # # D = job_elem.find('dev', class_='ellipsis job-description')
  # # Description = D.text
  # # print(Description)

  # # Experience
  # E = job_elem.find('div', class_='details')
  # if E is None:
  #   Exp = "Not-Mentioned"
  # else:
  #   Exp = E.text
  # print(Exp)

  # # Company
  # C = job_elem.find('a', class_='companyName')
  # Company=C.text
  # # print("Company: " + Company.text)
  
  # # City
  # C2 = job_elem.find('span', class_='ellipsis fleft locWdth')
  # City=C2.text

  # # Address
  # A = job_elem.find('span', class_='ellipsis fleft locWdth')
  # Address=A.text

  # # Salary Range
  # S = job_elem.find('span', class_='ellipsis fleft')
  # Salary=S.text

  # # Date Posted
  # D = job_elem.find('span', class_='fleft postedDate')
  # Date=D.text

  # # Rating
  # R = job_elem.find('span',class_='starRating fleft dot')
  # Rating = R

  # # Site
  # S = 'Naukri.com'
  # Site=S

  # U = job_elem.find('a',class_='title ellipsis').get('href')
  # URL = U
  # print(URL)

  body = job_elem.find('div', 'cardBody')

  body_divs = body.find('div', 'bodyRow')
  
  counter = 1
  for body_divs in body:
    print(body_divs)
    print('THIS IS ' + str(counter) + ' body_div')
    counter = counter + 1
    
  # dff = pd.concat([dff, pd.DataFrame([[Title, Description, Exp, Company, City, Address, Salary, Date, Rating, Site, URL]], columns = ['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Address', 'Salary Range', 'Date Posted', 'Rating', 'Site', 'URL'])], ignore_index=True)
  # print(dff)

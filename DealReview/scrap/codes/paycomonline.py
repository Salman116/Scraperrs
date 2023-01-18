# !pip install selenium
# !apt-get update # to update ubuntu to correctly run apt install
# !apt install chromium-chromedriver
# !cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from lxml import etree
import requests
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

session = requests.Session()

import os
import pandas as pd


path = "advertiser_scraper"
if not os.path.exists(path):
  os.mkdir(path)


def getJobs():
  wd = webdriver.Chrome('chromedriver',options=chrome_options)

  wd.get("https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey=516DAB1969CA2B74E21EBC6BFB0CF1FF")
  jobsLinks = []

  for page in range(17):
    results = wd.find_element(By.ID, "results")
    jobs = results.find_elements(By.CLASS_NAME, "jobInfo")
    for job in jobs:
      jobLink = job.find_element(By.TAG_NAME, "a").get_attribute("href")
      jobsLinks.append(jobLink)
    time.sleep(0.2)
    wd.find_element(By.XPATH, "//i[text() = 'arrow_forward']").click()
    print("Done with", page)
  return jobsLinks

def getJobsDetails(jobsLinks):
  jobees = []
  for jobLink in jobsLinks:
    soup = BeautifulSoup(session.get(jobLink).text, "html.parser")
    job_title = soup.find("span", class_="atsJobTitle").text.strip()
    dom = etree.HTML(str(soup))
    level = ""
    if len(dom.xpath("//span[@name='level']")) > 0:
      level = dom.xpath("//span[@name='level']")[0].text
    else:
      level = ""

    location = ""
    if len(dom.xpath('//span[@aria-label="Job Location"]')) > 0:
      location = dom.xpath('//span[@aria-label="Job Location"]')[0].text
    else:
      location = ""

    pos_type = ""
    if len(dom.xpath('//span[@aria-label="Position Type"]')) > 0:
      pos_type = dom.xpath('//span[@aria-label="Position Type"]')[0].text
    else:
      pos_type = ""
    
    edu_level = ""
    if len(dom.xpath('//span[@aria-label="Education Level"]')) > 0:
      edu_level = dom.xpath('//span[@aria-label="Education Level"]')[0].text
    else:
      edu_level = ""

    travel_percentage = ""
    if len(dom.xpath('//span[@aria-label="Travel Percentage"]')) > 0:
      travel_percentage = dom.xpath('//span[@aria-label="Travel Percentage"]')[0].text
    else:
      travel_percentage = ""

    job_shift = ""
    if len(dom.xpath('//span[@aria-label="Job Shift"]')) > 0:
      job_shift = dom.xpath('//span[@aria-label="Job Shift"]')[0].text
    else:
      job_shift = ""
    
    jobees.append({
        "job_title": job_title,
        "level": level,
        "location": location,
        "pos_type": pos_type,
        "edu_level": edu_level,
        "travel_percentage": travel_percentage,
        "job_shift": job_shift
    }) 
  return jobees

Jobs = getJobsDetails(getJobs())
df = pd.DataFrame.from_records(Jobs)
df.to_csv(f"{path}/paycomeonline.csv")
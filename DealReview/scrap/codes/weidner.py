import requests
from bs4 import BeautifulSoup
import os
import pandas as pd


path = "advertiser_scraper"
if not os.path.exists(path):
  os.mkdir(path)
  
def wediner():
  jobsPosted = []

  for page in range(0, 2):
    soup = BeautifulSoup(requests.get("https://jobs.jobvite.com/weidner/search/?p={}".format(page)).content, "html.parser")
    try:
      table = soup.find('table')
      table_body = table.find('tbody')
      rows = table_body.find_all('tr')
      for row in rows:
          cols = row.find_all('td')
          cols = [ele.text.strip() for ele in cols]
          jobsPosted.append([ele for ele in cols if ele])
    except:
      print("Page ends.")
      break
  jobsPosted = [{"title": job[0], "location": job[1].replace(" ", "").replace("\n", " ")} for job in jobsPosted] 
  jobsPosted = [i for n, i in enumerate(jobsPosted) if i not in jobsPosted[n + 1:]]
  return jobsPosted

jobsList = wediner()
df = pd.DataFrame.from_records(jobsList)
df.to_csv(f"{path}/wediner.csv")

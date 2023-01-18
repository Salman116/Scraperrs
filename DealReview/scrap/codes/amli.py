import os
import requests
import xmltodict
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

def amli():
  file = urllib.request.urlopen('https://careers-amli.icims.com/sitemap.xml')
  data = file.read()
  file.close()
  data = xmltodict.parse(data)
  jobsLinks = data['urlset']['url'][1:]
  jobs = []
  for jobLink in jobsLinks:
    soup = BeautifulSoup(requests.get(jobLink['loc']+"?in_iframe=1").content, "html.parser")
    jobMeta = {}
    details = soup.find_all("div", class_="iCIMS_JobHeaderTag")

    for detail in details:
      jobMeta[detail.find("dt").text.strip()] = detail.find("dd").text.strip()
    jobMeta['title'] = soup.find(id="iCIMS_Header").text.strip()
    jobs.append(jobMeta)
  return jobs
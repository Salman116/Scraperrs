import requests
from bs4 import BeautifulSoup

def assetliving():
    url = "https://boards.greenhouse.io/assetliving"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    jobs = soup.find_all("div", class_="opening")
    jobsList = []
    for job in jobs:
        location = job.find("span").text
        title = job.find("a").text
        link = "https://boards.greenhouse.io"+job.find("a").get("href")
        jobsList.append({"title": title, "location": location, "link": link})
    return jobsList
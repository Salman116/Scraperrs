import requests
import os
import pandas as pd


path = "advertiser_scraper"
if not os.path.exists(path):
  os.mkdir(path)

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://gables.wd5.myworkdayjobs.com',
    'Referer': 'https://gables.wd5.myworkdayjobs.com/Gables_Careers',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua-mobile': '?0',
}

def gables():
    session = requests.Session()
    jobs = []
    for offset in range(0, 80, 20):
        json_data = {
            'appliedFacets': {},
            'limit': 20,
            'offset': offset,
            'searchText': '',
        }

        response = session.post(
            'https://gables.wd5.myworkdayjobs.com/wday/cxs/gables/Gables_Careers/jobs',
            headers=headers,
            json=json_data,
        )
        if response.status_code == 200:
            response = response.json()
            for job in response['jobPostings']:
                jobs.append(job)
        else:
            print("No response recieved")
    jobs = [i for n, i in enumerate(jobs) if i not in jobs[n + 1:]]
    return jobs

jobs = gables()
df = pd.DataFrame.from_records(jobs)
df.to_csv(f"{path}/gables.csv")

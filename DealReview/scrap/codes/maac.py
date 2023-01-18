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
    'Origin': 'https://maa.wd1.myworkdayjobs.com',
    'Referer': 'https://maa.wd1.myworkdayjobs.com/en-US/MAA/?clientRequestID=d4fb56b1e5de485f97f8116147275861',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

def maac():
    session = requests.Session()
    jobs = []
    for offset in range(0, 220, 20):
        json_data = {
            'appliedFacets': {},
            'limit': 20,
            'offset': offset,
            'searchText': '',
        }
        response = session.post(
            'https://maa.wd1.myworkdayjobs.com/wday/cxs/maa/MAA/jobs',
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

jobsList = maac()
df = pd.DataFrame.from_records(jobsList)
df.to_csv(f"{path}/maac.csv")
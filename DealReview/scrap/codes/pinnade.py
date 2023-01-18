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
    # 'Cookie': 'wd-browser-id=c0c6283e-2455-4840-a0e2-c8108331dfc0; CALYPSO_CSRF_TOKEN=e6f0540e-4d6f-4207-869c-432dee962738; PLAY_SESSION=c7da65fb23af252df77717a6a67605a2ca46cb95-cw_pSessionId=rmmok06d2p2nv9tqumrtato0ua&instance=wd1prvps0003a; wday_vps_cookie=3425085962.53810.0000; TS014c1515=01dc4a3ac82286bd95f830fbb14a08e4154d455aa543123d807a470f64a1bba14636540853ffe5a9bc66144d88eb370a2d34cf4e2b; timezoneOffset=-300',
    'Origin': 'https://cw.wd1.myworkdayjobs.com',
    'Referer': 'https://cw.wd1.myworkdayjobs.com/en-US/External/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def pinnade():
    session = requests.Session()
    jobs = []
    for offset in range(0, 1840, 20):
        json_data = {
            'appliedFacets': {},
            'limit': 20,
            'offset': offset,
            'searchText': '',
        }
        response = session.post(
            'https://cw.wd1.myworkdayjobs.com/wday/cxs/cw/External/jobs',
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

jobsList = pinnade()
df = pd.DataFrame.from_records(jobsList)
df.to_csv(f"{path}/pinnade.csv")
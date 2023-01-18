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
    # 'Cookie': 'wd-browser-id=23971f0e-e979-4261-84a3-3bb9ed64e181; CALYPSO_CSRF_TOKEN=e20d3459-afed-44eb-a0f8-2665af350957; PLAY_SESSION=7a3d7a2a85a37afc9690c5b9cc30c5271d8a15f6-greystar_pSessionId=pbjqid1n5s7qj0hdna0o0rknvs&instance=wd1prvps0007i; wday_vps_cookie=3324422666.8755.0000; TS014c1515=01dc4a3ac863e7637724597d82ed1a1a3db7430e293369cdb138822c904e88ffd6ae996ed4a0ecbdcd16c4d645ed703f846a5a66ec; timezoneOffset=-300; _ga=GA1.4.1228915537.1673703895; _gat=1',
    'Origin': 'https://greystar.wd1.myworkdayjobs.com',
    'Referer': 'https://greystar.wd1.myworkdayjobs.com/External?clientRequestID=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


def greystar():
    session = requests.Session()
    jobs = []
    for offset in range(0, 1680, 20):
        json_data = {
            'appliedFacets': {},
            'limit': 20,
            'offset': offset,
            'searchText': '',
        }
        response = session.post(
            'https://greystar.wd1.myworkdayjobs.com/wday/cxs/greystar/External/jobs',
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


jobs = greystar()
df = pd.DataFrame.from_records(jobs)
df.to_csv(f"{path}/greystar.csv")
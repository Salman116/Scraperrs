import os
import requests
import pandas as pd


path = "advertiser_scraper"
if not os.path.exists(path):
  os.mkdir(path)

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en',
    'Connection': 'keep-alive',
    'Content-Type': 'application/vnd.oracle.adf.resourceitem+json;charset=utf-8',
    'Ora-Irc-Cx-UserId': '6eb23787-106d-4d6e-801b-33c8f230787f',
    'Ora-Irc-Language': 'en',
    'Referer': 'https://ehap.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/requisitions',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua-mobile': '?0',
}


def camden():
    session = requests.Session()

    jobsPosted = []
    for offset in range(25, 100, 25):
        response = session.get(
            'https://ehap.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true&expand=requisitionList.secondaryLocations,flexFieldsFacet.values&finder=findReqs;siteNumber=CX,facetsList=LOCATIONS%3BWORK_LOCATIONS%3BTITLES%3BCATEGORIES%3BORGANIZATIONS%3BPOSTING_DATES%3BFLEX_FIELDS,limit=25,sortBy=POSTING_DATES_DESC,offset={}'.format(offset),
            headers=headers,
        )
        if response.status_code == 200:
            response = response.json()
            jobsPosted.append(response['items'][0]['requisitionList'])
        else:
            print("No Response")
    allJobs = []
    for jobPosted in jobsPosted:
        for job in jobPosted:
            allJobs.append(job)
    return allJobs
    
jobs = camden()
df = pd.DataFrame.from_records(jobs)
df.to_csv(f"{path}/camden.csv")
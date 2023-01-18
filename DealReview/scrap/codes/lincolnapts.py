import requests
import os
import pandas as pd


path = "advertiser_scraper"
if not os.path.exists(path):
  os.mkdir(path)

def lincolnapts():
    jobsList = []
    for index in range(1, 6):
        url = f"https://careers.lincolnapts.com/api/jobs?limit=100&page={index}&sortBy=relevance&descending=false&internal=false"
        response = requests.get(url).json()
        jobs = response.get("jobs")
        if len(jobs) == 0:
            print("No jobs found")
            return
        print("Done with page", index)
        for job in jobs:
            job = job.get('data')
            title = job.get("title")
            description = job.get("description")
            location_name = job.get("location_name")
            street_address = job.get("street_address")
            city = job.get("city")
            state = job.get("state")
            country = job.get("country")
            country_code = job.get("country_code")
            postal_code = job.get("postal_code")
            location_type = job.get("location_type")
            latitude = job.get("latitude")
            longitude = job.get("longitude")
            tags2 = job.get("tags2")
            tags3 = job.get("tags3")
            tags4 = job.get("tags4")
            employment_type = job.get("employment_type")
            qualifications = job.get("qualifications")
            hiring_organization = job.get("hiring_organization")
            responsibilities = job.get("responsibilities")
            posted_date = job.get("posted_date")
            apply_url = job.get("apply_url")
            full_location = job.get("full_location")
            category = job.get("category")[0]
            jobsList.append({
                "title": title,
                "description": description,
                "location_name": location_name,
                "street_address": street_address,
                "city": city,
                "state": state,
                "country": country,
                "country_code": country_code,
                "postal_code": postal_code,
                "location_type": location_type,
                "latitude": latitude,
                "longitude": longitude,
                "tags2": tags2,
                "tags3": tags3,
                "tags4": tags4,
                "employment_type": employment_type,
                "qualifications": qualifications,
                "hiring_organization": hiring_organization,
                "responsibilities": responsibilities,
                "posted_date": posted_date,
                "apply_url": apply_url,
                "full_location": full_location,
                "category": category,
            })
    return jobsList

jobsList = lincolnapts()
df = pd.DataFrame.from_records(jobsList)
df.to_csv(f"{path}/lincolnapts.csv")
import os
import requests

def jobSearch(title):
    url = "https://jobs-api14.p.rapidapi.com/v2/linkedin/search"

    headers = {
        "x-rapidapi-key": "",
        "x-rapidapi-host": "jobs-api14.p.rapidapi.com"
    }

    params = {
        "query": title,
        "experienceLevels": "intern;entry;associate;midSenior;director",
        "workplaceTypes": "remote;hybrid;onSite",
        "location": "Worldwide",
        "datePosted": "month",
        "employmentTypes": "contractor;fulltime;parttime;intern;temporary"
    }

    response = requests.get(url, headers=headers, params=params, timeout=20)

    print("STATUS:", response.status_code)
    print("RAW:", response.text)   # keep this for debugging

    if response.status_code != 200:
        return []

    data = response.json()
    return data.get("data", [])


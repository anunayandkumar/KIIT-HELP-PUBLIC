import requests


def jobSearch(title):
    url = "https://jobs-api14.p.rapidapi.com/list"

    querystring = {"query": title, "location": "India",
                   "remoteOnly": "false", "datePosted": "month",
                   "employmentTypes": "fulltime;parttime;intern;contractor", "index": "0"}

    headers = {
        "X-RapidAPI-Key": "API KEY",
        "X-RapidAPI-Host": "jobs-api14.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    array_of_jobs = []

    count = 0
    strID = ""
    for job in data.get("jobs", []):
        if count < 3:
            countProvider = 0
            strID = strID + "Title: " + job.get("title") + "\n"
            strID = strID + "Company: " + job.get("company") + "\n"
            strID = strID + "Location: " + job.get("location") + "\n"
            strID = strID + "Date Posted: " + job.get("datePosted") + "\n\n"
            for provider in job.get("jobProviders", []):
                if countProvider < 2:
                    strID = strID + "Provider: " + provider.get("jobProvider") + "\n"
                    strID = strID + "URL: " + provider.get("url") + "\n\n"
                    countProvider = countProvider + 1

            array_of_jobs.append(strID)
            strID = ""

            count = count + 1

    return array_of_jobs





import requests

def love(sname, fname):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname": sname, "fname": fname}

    headers = {
        "X-RapidAPI-Key": "API KEY",
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }

    data = requests.get(url, headers=headers, params=querystring)
    res = data.json()

    str = "The love percentage between the given two persons is " + res['percentage']

    return str
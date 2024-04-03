import requests

def getjokes():
    url = "https://world-of-jokes1.p.rapidapi.com/v1/jokes/random-joke"

    headers = {
        "X-RapidAPI-Key": "API KEY",
        "X-RapidAPI-Host": "world-of-jokes1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    res = response.json()
    str = ""
    str += res['title'] + "\n"
    str += res['body'] + "\n"

    return str
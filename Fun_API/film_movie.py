import requests

def mov(g,s,e,n):
	url = "https://moviesdatabase.p.rapidapi.com/titles"

	querystring = {"genre": g, "startYear": s, "endYear": e, "limit": n}

	headers = {
		"X-RapidAPI-Key": "API KEY",
		"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	parsed_data = response.json()

	str = ""
	array_of_movie = []
	# Extract and print title, release date, and URL for each entry
	for entry in parsed_data['results']:
		title = entry['titleText']['text']
		release_date = f"{entry['releaseDate']['year']}-{entry['releaseDate']['month']}-{entry['releaseDate']['day']}"
		url = entry['primaryImage']['url'] if entry['primaryImage'] else None

		str = str + "Title: " + title + "\n"
		str = str + "Release Date : " + release_date + "\n"
		str = str + "URL : " + url + "\n"

		array_of_movie.append(str)
		str = ""

	return array_of_movie





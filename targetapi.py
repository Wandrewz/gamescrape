import requests

url = "https://feeditem-target.p.rapidapi.com/itemID/52161284"

headers = {
    'x-rapidapi-host': "feeditem-target.p.rapidapi.com",
    'x-rapidapi-key': "1167c5a233msh60ccafe772449f8p1bc540jsn304b2d05e0ba"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
import requests

url = "https://axesso-walmart-data-service.p.rapidapi.com/wlm/walmart-lookup-product"

querystring = {"url":"https://www.walmart.com/ip/The-Legend-of-Zelda-Breath-of-the-Wild-Nintendo-Nintendo-Switch-045496590420/55432568"}

headers = {
    'x-rapidapi-host': "axesso-walmart-data-service.p.rapidapi.com",
    'x-rapidapi-key': "cbe7bbccbamsh155304094958281p187d2fjsn2783009cf0b4"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
import requests

url = "https://amazon-products1.p.rapidapi.com/product"

querystring = {"country":"US","asin":"B01MS6MO77"}

headers = {
    'x-rapidapi-host': "amazon-products1.p.rapidapi.com",
    'x-rapidapi-key': "cbe7bbccbamsh155304094958281p187d2fjsn2783009cf0b4"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
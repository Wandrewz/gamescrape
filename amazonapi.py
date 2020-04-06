import requests

url = "https://amazon-products1.p.rapidapi.com/product"

querystring = {"country":"US","asin":"B01MS6MO77"}

headers = {
    'x-rapidapi-host': "amazon-products1.p.rapidapi.com",
    'x-rapidapi-key': "1167c5a233msh60ccafe772449f8p1bc540jsn304b2d05e0ba"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
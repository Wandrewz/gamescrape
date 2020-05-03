import sqlite3
import requests


def walmartapi(walmarturl):
    url = "https://axesso-walmart-data-service.p.rapidapi.com/wlm/walmart-lookup-product"

    querystring = {"url": walmarturl}

    headers = {
        'x-rapidapi-host': "axesso-walmart-data-service.p.rapidapi.com",
        'x-rapidapi-key': "1167c5a233msh60ccafe772449f8p1bc540jsn304b2d05e0ba"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()['price']


def amazonapi(amazonurl):
    url = "https://axesso-axesso-amazon-data-service-v1.p.rapidapi.com/amz/amazon-lookup-product"

    querystring = {"url": amazonurl}

    headers = {
        'x-rapidapi-host': "axesso-axesso-amazon-data-service-v1.p.rapidapi.com",
        'x-rapidapi-key': "1167c5a233msh60ccafe772449f8p1bc540jsn304b2d05e0ba"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()['price']


def main():

    path = '/home/drew/Documents/School/Spring20/IFT402/gamescrape/gamescrapesite/db.sqlite3'

    conn = sqlite3.connect(path)

    conn.row_factory = sqlite3.Row

    c = conn.cursor()
    c2 = conn.cursor()

    for row in c.execute('SELECT * from gamescrape_game'):
        wprice = walmartapi(row['walmarturl'])
        aprice = amazonapi(row['amazonurl'])

        query = 'Update gamescrape_game set walmartprice = ?, amazonprice = ? where id = ?'
        values = (wprice, aprice, row['id'])
        c2.execute(query, values)
        conn.commit()

        if wprice < aprice:
            q = 'Update gamescrape_game set lowestprice = ?, loweststore = ?, lowesturl = ? where id = ?'
            v = (wprice, 'Walmart', row['walmarturl'], row['id'])
            c2.execute(q, v)
        else:
            q = 'Update gamescrape_game set lowestprice = ?, loweststore = ?, lowesturl = ? where id = ?'
            v = (aprice, 'Amazon', row['amazonurl'], row['id'])
            c2.execute(q, v)
        conn.commit()

        if wprice < row['historiclow']:
            c2.execute(
                'Update gamescrape_game set historiclow = ? where id = ?', (wprice, row['id']))
        if aprice < row['historiclow']:
            c2.execute(
                'Update gamescrape_game set historiclow = ? where id = ?', (aprice, row['id']))
        conn.commit()

        print(row['title'])

    conn.close()


if __name__ == "__main__":
    main()

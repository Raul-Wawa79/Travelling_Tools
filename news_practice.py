import requests

#commenting out the learning code used in the lesson
"""r = requests.get(
    'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-12-01&to=2022-12-02&sortBy=popularity&language=en&apiKey=121657808dcb407380857fd35291e006')

content = r.json()

articles = content['articles']

for article in articles:
    print('TITLE\n', article['title'],
          '\nDESCRIPTION\n', article['description'])"""

def get_news(topic, from_date, to_date, api_key= '121657808dcb407380857fd35291e006'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language=en&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(topic='space', from_date='2022-12-02', to_date='2022-12-11'))

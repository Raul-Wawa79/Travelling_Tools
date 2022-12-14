"""For now just adding a list of potential URL to be used"""
#https://es.yahoo.com/?p=us&guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAC9f-8cwdV7pPZqAKhsq-JS5N1dNPzQKmiVeWT4EZZiL3-_GkzDjyXTmWgdB36wxwH2MRhzK9mEprIhSU111THtHgQu52BCaXohzd_LUur3_q3NRlPIIU4qxyRO8JFin9Z1SivRhnIuogBTV3PSFh89kb4DWGiyPgMl6Bn3W0sqm
#https://news.un.org/en/?gclid=Cj0KCQiA4uCcBhDdARIsAH5jyUkNMBvz83Voj1RE6Z5_hBZG55_ESZf3reoeXQwaXSSbYLzY1oj5a2EaAuesEALw_wcB
#https://www.democracynow.org/?gclid=Cj0KCQiA4uCcBhDdARIsAH5jyUkeOXjrwoZvJhy_SscsKb01XsLiLrkGBVLGm_Me1lfa6WF69PxxlpIaAsJdEALw_wcB
#https://www.bbc.com/news/world

import requests

def get_news(country, api_key= '121657808dcb407380857fd35291e006'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"\nTITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(country='gb'))
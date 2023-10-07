import requests
import json

query = input("Enter your intrested topic of the news !!\n ->")
num_articles = int(input("Enter the number of news articles you want to fetch ? \n ->"))
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-10-06&to=2023-10-06&sortBy=popularity&apiKey=37dc720283d447eda3b78cd589b5a4e6"
a = requests.get(url)
news = json.loads(a.text)


for index, article in enumerate(news["articles"][:num_articles]):
    print(f"Article {index + 1}")
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------")

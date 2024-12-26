import json 
from dotenv import load_dotenv
load_dotenv()

import requests
from newspaper import Article

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

article_urls = ['https://www.thehindubusinessline.com/markets/indian-markets-are-less-dependent-on-fpi-flows-vallum-capital-ceo/article69018830.ece',
       'https://www.thehindubusinessline.com/markets/share-market-nifty-sensex-highlights-26-december-2024/article69025963.ece']
article_titles=[]
article_content=[]
session = requests.Session()

for article_url in article_urls:
    try:
        response = session.get(article_url, headers=headers, timeout=60)
        
        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()
            article_titles.append(article.title)
            article_content.append(article.text)
            print(f"Title: {article.title}")
            print(f"Text: {article.text}")
            
        else:
            print(f"Failed to fetch article at {article_url}")
    except Exception as e:
        print(f"Error occurred while fetching article at {article_url}: {e}")

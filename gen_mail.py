import json 
from dotenv import load_dotenv
load_dotenv()
import os 
from langchain_groq import ChatGroq
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
            # print(f"Title: {article.title}")
            # print(f"Text: {article.text}")
            
        else:
            print(f"Failed to fetch article at {article_url}")
    except Exception as e:
        print(f"Error occurred while fetching article at {article_url}: {e}")

print(article_titles)


from langchain_core.messages import HumanMessage, SystemMessage

# we get the article data from the scraping part
article_title = article_titles
article_text = article_content

# prepare template for prompt
template = """You are an excellent assistant that summarizes stock market news in a user-friendly format for retail investors.

Here's the stock market news you need to summarize.

==================
Title: {article_title}

{article_text}
==================

Write a concise and readable summary of the news. Ensure the summary includes:
1. A brief headline that highlights the key point of the news.
2. A short explanation of the news in 2-3 sentences, making it easy for retail investors to understand.
3. Bullet points summarizing the most important details or takeaways from the news.
4. A brief sentiment analysis of how the news might impact the market (e.g., bullish, bearish, or neutral).
5. Optional: Provide actionable insights or considerations for retail investors based on the news.

Be sure to maintain a consistent format and clarity across each summary for easy reading.
Give the output as a daily mail format, so that this text can be automatically mailed(dont mention subject/header, start with greetings and mention  Best Regards The Daily Bugle)
"""


prompt = template.format(article_title="~$~".join(article_titles), article_text="~$~".join(article_content))


messages = [HumanMessage(content=prompt)]

groq_api_key=os.environ['GROQ_API_KEY']
# llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="mixtral-8x7b-32768")

summary = llm.invoke(messages)
print(summary.content)


# Daily Stock Market Newsletter Generator

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![NewsAPI](https://img.shields.io/badge/NewsAPI-2.0-orange)
![LangChain](https://img.shields.io/badge/LangChain-v0.0.1-green)
![Groq](https://img.shields.io/badge/Groq-v0.13.1-blueviolet)
![Requests](https://img.shields.io/badge/Requests-v2.26.0-red)
![Newspaper3k](https://img.shields.io/badge/Newspaper3k-v0.2.8-yellow)


This project generates a daily stock market newsletter for retail investors, summarizing the latest Indian stock market news using a combination of NewsAPI, Natural Language Processing (NLP), and OpenAI's Groq model. 

### Features

- **Real-time stock market news aggregation**: Fetches the latest headlines from top sources in India via [NewsAPI](https://newsapi.org/).
- **Automated summarization**: Uses Groq's large language model (`mixtral-8x7b-32768`) to summarize stock market news into concise, user-friendly summaries.
- **Actionable insights**: The generated summary includes key market points, sentiment analysis, and recommendations for retail investors.
- **Customizable email format**: The summarized content is formatted into a daily newsletter format ready for distribution.

### Workflow

1. **Fetch Top News**: Fetch top headlines from the Indian stock market using NewsAPI.
2. **Article Scraping**: Retrieve detailed articles using `newspaper3k` to extract titles and content.
3. **Summarization**: Pass the article data to the Groq model for generating user-friendly summaries.
4. **Output**: Format the summaries into an email template with headlines, key points, sentiment analysis, and actionable insights.
- **Future Plans**: A pipeline will be developed to automatically send these summaries via email to subscribers.

### How It Works

- The script uses the **NewsAPI** to get the latest stock market news articles for the specified date range.
- Articles are scraped for full content and parsed using the **newspaper** library.
- The parsed data is processed through **LangChain** and **Groq's Mixtral LLM** to summarize the articles.
- The summary is formatted into an email template with headlines, key points, sentiment analysis, and actionable insights.
- **Future Plans**: A pipeline will be developed to automatically send these summaries via email to subscribers.

### Setup

1. **NewsAPI API Key**: Sign up at [NewsAPI](https://newsapi.org/) and obtain your API key. Replace `your_api_key` in the code.
2. **Groq API Key**: Get an API key from [Groq](https://groq.com/) for using the `ChatGroq` model.
3. **Environment Variables**: Store your API keys in an `.env` file:

```
NEWS_API_KEY=your_api_key
GROQ_API_KEY=your_groq_api_key
```

4. **Run the Script**: Execute the script to get the top stock market news and generate the daily newsletter:

```bash
python generate_newsletter.py
```
---
### Output

The final output will look like this:

**Dear Reader,**

I hope you're doing well. Here's today's summary of the stock market news.

**Headline:** Indian Markets Show Reduced Dependence on FPI Flows, Favoring Domestic Investments

**News Summary:** In an interview, Manish Bhandari, Founder, CEO, and Portfolio Manager of Vallum Capital Advisors, mentioned that the Indian market has become less dependent on foreign portfolio investor (FPI) inflows. Strong domestic flows, especially through systematic investment plans (SIPs), have been evident in the market.

**Key Points:**
- FPI holdings amount to ₹70-71 lakh crores out of India's total market capitalization of ₹444 lakh crores.
- Recent FPI holdings decline cannot be directly attributed to SEBI's new ODI regulations.
- The market's reduced dependence on FPI investments is due to strong domestic flows.
- Investors should tailor strategies based on individual styles and risk tolerances.

**Sentiment Analysis:** Neutral. The news highlights the Indian market's shift towards domestic investments and reduced dependence on FPI flows, which can be positive for market stability and long-term performance.

**Actionable Insights:** Consider investing in sectors with strong long-term growth potential and tailor your investment strategies based on your unique risk profile and market knowledge.

Best Regards,  
The Daily Bugle

---

### Future Improvements

- **Automated Email Pipeline**: The next step is to create a pipeline that automatically sends the daily newsletters to subscribers via email using SMTP or other email services.
- **Personalized Content**: Future versions will allow tailoring the newsletter to individual preferences based on market segments and interests.
-**Agent Driven**: Plan on using agents to scrape more related data, focussing specific aspects of stock markets like rate cuts and dollar index.
### Acknowledgments

- [NewsAPI](https://newsapi.org/) for providing access to global news sources.
- [LangChain](https://www.langchain.com/) for its excellent toolset to manage LLM prompts.
- [Groq](https://groq.com/) for providing powerful AI models.
- [newspaper3k](https://newspaper.readthedocs.io/) for article scraping.

---

Feel free to fork the repository and contribute improvements!

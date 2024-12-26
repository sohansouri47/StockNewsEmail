from newsapi import NewsApiClient
import pandas as pd

# Init
newsapi = NewsApiClient(api_key='API-KEY')

# top-headlines
top_headlines = newsapi.get_everything(q='Indian Stock Market',
                                       from_param='2024-12-24',
                                       to='2024-12-26',
                                       sort_by='popularity',
                                       page_size=2)



def get_links(data):
    import pandas as pd
    articles=data['articles']
    df=pd.DataFrame(articles)
    df[['source_id', 'source_name']] = df['source'].apply(pd.Series)
    df['publishedAt'] = pd.to_datetime(df['publishedAt'], format='%Y-%m-%dT%H:%M:%SZ')
    df=df.drop(labels='source',axis=1)
    newws_links=data1['url'].to_numpy()
    return newws_links

data1=get_links(top_headlines)

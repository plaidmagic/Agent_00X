import tweepy
import requests
import os

def collect_twitter_hype(hashtags, count=100):
    """
    Collects tweets mentioning specific hashtags using the Twitter API.

    Args:
        hashtags (list): List of hashtags to search for.
        count (int): Number of tweets to retrieve for each hashtag.

    Returns:
        list: Collected tweet texts.
    """
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_SECRET"),
    )
    api = tweepy.API(auth)
    tweets = []

    for hashtag in hashtags:
        try:
            for tweet in tweepy.Cursor(api.search_tweets, q=f"#{hashtag}", lang="en").items(count):
                tweets.append(tweet.text)
        except Exception as e:
            print(f"Error fetching tweets for #{hashtag}: {e}")
    
    return tweets

def fetch_market_data(coins):
    """
    Fetches market cap and trading volume data for given coins from CoinGecko.

    Args:
        coins (list): List of coin IDs (e.g., 'dogecoin', 'shiba-inu').

    Returns:
        dict: Dictionary containing market cap and volume data for each coin.
    """
    url = os.getenv("COINGECKO_API_URL") + "/simple/price"
    params = {
        "ids": ",".join(coins),
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching market data: {e}")
        return {}

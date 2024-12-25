from data_collector import collect_twitter_hype, fetch_market_data
from tweet_generator import generate_tweet
from twitter_client import post_tweet
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def main():
    """
    Main function to collect data, generate a tweet, and post it on Twitter.
    """
    try:
        # Define hashtags and coins to track
        hashtags = ["memecoins", "dogecoin", "shibainu"]
        coins = ["dogecoin", "shiba-inu", "pepe"]

        print("Collecting hype data from Twitter...")
        hype_data = collect_twitter_hype(hashtags, count=50)

        print("Fetching market data from CoinGecko...")
        market_data = fetch_market_data(coins)

        print("Generating tweet content...")
        tweet = generate_tweet(hype_data, market_data)
        print(f"Generated Tweet: {tweet}")

        print("Posting the tweet...")
        post_tweet(tweet)
        print("Tweet posted successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

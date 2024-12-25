import tweepy
import os

def create_twitter_client():
    """
    Creates and authenticates a Tweepy API client using credentials from the environment variables.

    Returns:
        tweepy.API: Authenticated Tweepy API client.
    """
    try:
        auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_SECRET"),
        )
        api = tweepy.API(auth)
        # Test authentication
        api.verify_credentials()
        print("Twitter authentication successful.")
        return api
    except Exception as e:
        print(f"Error during Twitter authentication: {e}")
        return None

def post_tweet(content):
    """
    Posts a tweet to Twitter using the authenticated client.

    Args:
        content (str): The tweet content to post.

    Returns:
        None
    """
    client = create_twitter_client()
    if client:
        try:
            client.update_status(content)
            print("Tweet posted successfully!")
        except Exception as e:
            print(f"Error posting tweet: {e}")

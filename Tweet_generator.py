import openai
import os

# Load the OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tweet(hype_data, market_data):
    """
    Generates an engaging tweet based on Twitter hype and market data.

    Args:
        hype_data (list): A list of trending tweet texts.
        market_data (dict): Market cap and volume data for specific coins.

    Returns:
        str: Generated tweet content.
    """
    # Summarize hype data for the prompt
    top_hype_summary = " ".join(hype_data[:5])  # Use the first 5 tweets for the prompt

    # Format market data for the prompt
    market_summary = "\n".join(
        f"{coin}: Market Cap: ${data['usd_market_cap']:,}, 24H Volume: ${data['usd_24h_vol']:,}"
        for coin, data in market_data.items()
        if "usd_market_cap" in data and "usd_24h_vol" in data
    )

    # Compose the AI prompt
    prompt = (
        f"Based on the following Twitter hype and market data, generate an engaging tweet:\n\n"
        f"Trending Twitter Hype:\n{top_hype_summary}\n\n"
        f"Market Data:\n{market_summary}\n\n"
        f"Focus on making it appealing to the crypto and meme community."
    )

    try:
        # Generate the tweet using OpenAI's GPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=280,
            temperature=0.7,
        )
        tweet = response.choices[0].text.strip()
        return tweet
    except Exception as e:
        print(f"Error generating tweet: {e}")
        return "Error generating tweet. Stay tuned for updates!"


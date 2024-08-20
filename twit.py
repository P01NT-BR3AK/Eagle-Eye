import tweepy

# Twitter API v2 credentials
BEARER_TOKEN = 'your_bearer_token'
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate with the Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN, 
                       consumer_key=API_KEY, 
                       consumer_secret=API_SECRET_KEY, 
                       access_token=ACCESS_TOKEN, 
                       access_token_secret=ACCESS_TOKEN_SECRET)

# Define the search terms you want to track
search_terms = ['#extremistcontent', '#suspiciousactivity', '#radicalization']

# Function to search for tweets and reply
def search_and_reply():
    for term in search_terms:
        query = f"{term} lang:en"
        
        # Search for recent tweets containing the term
        tweets = client.search_recent_tweets(query=query, max_results=10)
        
        if tweets.data:
            for tweet in tweets.data:
                try:
                    # Reply to the tweet
                    response_text = f"@{tweet.author_id} According to Eagle Eye, this content may be extremist, act with caution."
                    client.create_tweet(text=response_text, in_reply_to_tweet_id=tweet.id)
                    print(f"Replied to tweet by user with ID {tweet.author_id}")

                except Exception as e:
                    print(f"Error: {e}")
        else:
            print(f"No recent tweets found for {term}")

# Run the function
search_and_reply()

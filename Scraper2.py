import tweepy
import os
import pandas as pd
# from dotenv import load_dotenv

# load_dotenv()
BEARER_TOKEN = os.getenv("BEARER")

client = tweepy.Client(BEARER_TOKEN)

# Search data
def get_data():
    search_term = input("Search term: ") # Search query & csv filename
    count = input("Count: ")
    return search_term,count

# Scrape tweets
def scrape_tweets(username,count):

    try:
        # grabbing user id from username 
        user_id = client.get_user(username=username).data.id
        
        # Creation of query method using parameters
        tweets = tweepy.Paginator(client.get_users_tweets, user_id, tweet_fields=["author_id", "created_at", "lang", "public_metrics"], expansions=["author_id"], max_results=100).flatten(limit = count)
        
        tweets_list = []
        
        # Pulling information from tweets generator
        tweets_list = [[tweet.created_at, tweet.id, tweet.text, tweet.public_metrics["retweet_count"], tweet.public_metrics["like_count"]]for tweet in tweets]
        
        # Creation of dataframe from tweets list
        tweets_df = pd.DataFrame(tweets_list, columns=["Created At", "Tweet Id", "Text", "Retweet Count", "Like Count"])
        
        # Converting dataframe to CSV 
        tweets_df.to_csv("{}-tweets.csv".format(username), sep=",", index = False)
        
        print("Completed Scrape!")
        
    except BaseException as e:
        print("failed on_status,",str(e))

    return
from functions import top_10_hashtags, top_10_tweets, top_10_tweets_retweeted, top_10_users
import json

if __name__ == "__main__":
    with open("dataset.json", "r") as f:
        dataset = json.load(f)
        top_10_hashtags(dataset)
        top_10_tweets(dataset)
        top_10_tweets_retweeted(dataset)
        top_10_users(dataset)
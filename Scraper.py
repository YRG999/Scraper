# Simple Scraper
# See README.md for details.

# Import modules
import snscrape.modules.twitter as sntwitter
import snscrape.modules.reddit as snredditsub
import pandas as pd
import os
import csv
import json
import random

# Choose platform to search
choice = input("1-Twitter; 2-Reddit; 3-Subreddit name\n(As of 12-18-22 Reddit search unavailable, see readme)\n")

# Create filename
def filename_func(max_num_str,filename):
    rstring = str(random.randrange(10000))
    full_filename = filename+rstring+"-"+max_num_str
    print('File name is '+full_filename+'.csv')
    return full_filename

# User choices, max results, search term, filename number
def userInput():
    max_num_str = input("Maximum results (number):\n")
    search_term = input("Search term:\n")
    filename = input("Filename prefix (no spaces):\n")
    return max_num_str, search_term, filename

# Create global variables for answers
answer = userInput()
max_num_str = answer[0]
search_term = answer[1]
filename = answer[2]
full_filename = filename_func(max_num_str,filename)
max_num = int(max_num_str)

# Choice 1: Search Twitter
# For example, from:username since:2022-01-01 until:2022-12-01
if choice == "1":

    tweets_list2 = []

    # get tweets
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search_term).get_items()):
        if i > (max_num - 1):
            break
        tweets_list2.append([tweet.date, tweet.content, tweet.user.username, tweet.url, tweet.media])
        
    tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Text', 'Username', 'URL', 'Media'])

    # print to csv
    tweets_df2.to_csv('output/'+full_filename+'.csv')

# Choice 2: Reddit
elif choice == "2":

    # os command
    command = "snscrape --jsonl --progress --max-results {} reddit-search '{}' > {}.json"

    # command with user choices
    run_command = command.format(max_num, search_term, full_filename)

    infile0 = "output/"+full_filename+".json"
    outfile0 = "output/"+full_filename+".csv"

    os.system(run_command)

    infile = open(infile0,"r")
    outfile = open(outfile0,"w")

    writer = csv.writer(outfile)

    # csv header
    header = "_type","author","body","created","id","parentId","link","selftext","subreddit","title","url"
    writer.writerow(header)

    # csv body
    for row in infile:
      data = json.loads(row)
      if data["_type"] == "snscrape.modules.reddit.Submission":
        data_to_write = [data["_type"], data["author"],"", data["created"], data["id"],"", data["link"], data["selftext"], data["subreddit"], data["title"], data["url"]]
        writer.writerow(data_to_write)
      else:
        data_to_write = [data["_type"], data["author"], data["body"], data["created"], data["id"], data["parentId"],"","", data["subreddit"],"", data["url"]]
        # data_to_write = [data["body"]]
        writer.writerow(data_to_write)

# Choice 3: Subreddit name - show posts
elif choice == "3":

    datalist3 = []

    # get subreddit name
    for i,post in enumerate(snredditsub.RedditSubredditScraper(search_term).get_items()):
        if i > (max_num - 1):
            break
        datalist3.append([post.author,post.created,post.id,post.subreddit,post.url])            
        
    df3 = pd.DataFrame(datalist3, columns=['author','created','id','subreddit','URL'])

    # print to csv
    df3.to_csv('output/'+full_filename+'.csv')

# Unknown choice or error
else:
    print("\nBye!")
    print("\nHelpful links:\nhttps://github.com/JustAnotherArchivist/snscrape\nhttps://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af\n")
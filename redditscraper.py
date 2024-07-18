import praw
import json

# Reddit API credentials
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')

# Subreddit and query
subreddit_name = 'Caldigit'
query = 'Caldigit TS3 Plus'

# Fetch posts from subreddit
subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.search(query, limit=100)

data = []

for post in posts:
    question = post.title
    # Assuming the top comment is the best answer (simplification)
    post.comments.replace_more(limit=0)
    if post.comments:
        answer = post.comments[0].body
        data.append({"Question": question, "Answer": answer})

# Save data to JSON file
with open('caldigit_support_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

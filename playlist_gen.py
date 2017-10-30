import praw
import config

def bot_login():
  return praw.Reddit(
    username = config.username,
    password = config.password,
    client_id = config.client_id,
    client_secret = config.client_secret,
    user_agent = "playlistGenv1.0"
  )

def is_valid_post(post):
  return not post.stickied

def run_bot(reddit):
  for submission in reddit.subreddit('listentothis').hot(limit = 3):
    print (is_valid_post(submission))

reddit = bot_login()
run_bot(reddit = reddit)

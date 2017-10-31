import praw
import config

import url_validation

def bot_login():
  return praw.Reddit(
      username=config.r_username,
      password=config.r_password,
      client_id=config.r_client_id,
      client_secret=config.r_client_secret,
      user_agent="playlistGenv1.0"
  )

def is_valid_post(post):
  return not post.stickied

def get_posts(reddit, subreddit="listentothis"):
  posts = []
  for submission in reddit.subreddit(subreddit).hot():
    if is_valid_post(submission) and url_validation.is_youtube(submission.url):
      posts.append(submission.url)
  return posts[:25]

REDDIT = bot_login()
get_posts(reddit=REDDIT)

import praw
import re
import config

def bot_login():
  return praw.Reddit(
      username=config.username,
      password=config.password,
      client_id=config.client_id,
      client_secret=config.client_secret,
      user_agent="playlistGenv1.0"
  )

def is_youtube(url):
  youtube_regex = re.compile(
      r'(https?://)?(www\.)?'
      r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
      r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
  return not not youtube_regex.match(url)

def is_valid_post(post):
  return not post.stickied

def get_posts(reddit, subreddit="listentothis"):
  posts = []
  for submission in reddit.subreddit(subreddit).hot():
    if is_valid_post(submission):
      posts.append(submission.url)
  print is_youtube(posts[0])
  return posts[:25]

REDDIT = bot_login()
# get_posts(reddit=REDDIT)

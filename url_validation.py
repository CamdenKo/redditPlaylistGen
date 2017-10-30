import re

def is_youtube(url):
  youtube_regex = re.compile(
      r'(https?://)?(www\.)?'
      r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
      r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
  return not not youtube_regex.match(url)

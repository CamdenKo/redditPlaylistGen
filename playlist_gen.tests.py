import unittest
import playlist_gen

class URLValidation(unittest.TestCase):
  def test_youtube(self):
    self.assertTrue(playlist_gen.is_youtube('https://www.youtube.com/watch?v=A6rTvlgLUWk'))
    self.assertTrue(playlist_gen.is_youtube('https://youtu.be/A6rTvlgLUWk'))
    self.assertFalse(playlist_gen.is_youtube('not youtube'))
    self.assertFalse(playlist_gen.is_youtube('https://soundcloud.com/noertheboy/half-tab-with-hapa'))


if __name__ == '__main__':
  unittest.main()

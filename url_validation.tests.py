import unittest
import url_validation

class URLValidation(unittest.TestCase):
  def test_youtube(self):
    self.assertTrue(url_validation.is_youtube('https://www.youtube.com/watch?v=A6rTvlgLUWk'))
    self.assertTrue(url_validation.is_youtube('https://youtu.be/A6rTvlgLUWk'))
    self.assertFalse(url_validation.is_youtube('not youtube'))
    self.assertFalse(url_validation.is_youtube('https://soundcloud.com/noertheboy/half-tab-with-hapa'))

if __name__ == '__main__':
  unittest.main()

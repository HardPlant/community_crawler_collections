import unittest
import dc_wordcloud
import dc_crawler

class test_unittest(unittest.TestCase):
    def setUp(self):
        self.kakaourl="http://tech.kakao.com/2018/10/23/kakao-blind-recruitment-round-2/"
    
    def test_simple(self):
        text = "A Simple Wordcloud"
        wordcloud = dc_wordcloud.make_wordcloud(text)
        self.assertIsNotNone(wordcloud)

unittest.main()
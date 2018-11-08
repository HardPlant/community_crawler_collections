import unittest
import datetime
import os
import dc_crawler
import crawl_logger

class test_module(unittest.TestCase):
    def setUp(self):
        self.url="http://tech.kakao.com/2018/10/23/kakao-blind-recruitment-round-2/"
        self.dcurl="http://gall.dcinside.com/mgallery/board/view/?id=theaterdays&no=1049953&page=1"
        if os.path.exists("theaterdays/1050143"):
            os.unlink("theaterdays/1050143")
        if os.path.exists("theaterdays/1050144"):
            os.unlink("theaterdays/1050144")
        if os.path.exists("theaterdays/1050145"):
            os.unlink("theaterdays/1050145")

    def test_read(self):
        self.text = dc_crawler.fetch(self.url)
        self.assertIsNotNone(self.text, msg="Parse")
        self.body = self.text.text
        self.content = self.body.find('2019 카카오')
        self.assertIsNotNone(self.content, msg="Fetch Failed")

    def test_parse(self):
        self.text = dc_crawler.crawl(self.url, dc_crawler.Kakao)
        self.assertIsNotNone(self.text, msg="Parse")
        self.assertTrue("2019" in self.text.title)
        self.assertTrue("작년 2차" in self.text.content)
        self.assertFalse("<p>" in self.text.content)

    def test_parse_dc(self):
        self.text = dc_crawler.crawl(self.dcurl, dc_crawler.DCWrites)
        self.assertIsNotNone(self.text, msg="Parse Failed")
        self.assertTrue("ㄴ 짤녀 앞으로 영원히 배없찐임ㅅㄱ ㅋㅋ" in self.text.title)
        self.assertTrue("ㅇㅇ" in self.text.author)
        self.assertTrue("ㅇ" in self.text.content)
        self.assertEqual(datetime.datetime(2018, 11, 8, 12, 15, 31), self.text.date)

    def test_parse_dc_log(self):
        self.text = dc_crawler.crawl(self.dcurl, dc_crawler.DCWrites, log=True)
        self.assertIsNotNone(self.text, msg="Parse Failed")
        self.assertTrue(os.path.exists("theaterdays/1049953"), msg="File Not Exists")
        crawl_logger.ready_parent_dir("theaterdays")
        content = crawl_logger.read("1049953")
        self.assertTrue("ㄴ 짤녀 앞으로 영원히 배없찐임ㅅㄱ ㅋㅋ" in content)
        self.assertTrue("ㅇㅇ" in content)
        self.assertTrue("ㅇ" in content)
    
    def tearDown(self):
        if os.path.exists("theaterdays/1049953"):
            os.unlink("theaterdays/1049953")

    def test_parse_sequel(self):
        for id in range(1050143, 1050146):
            text = dc_crawler.crawl(dc_crawler.get_dc_url("theaterdays", id),dc_crawler.DCWrites)
            if id == 1050143:
                self.assertEqual(1050143, text.wid)
                self.assertTrue("미래귀여운" in text.author)
            if id == 1050144:
                self.assertTrue("" in text.author)
            if id == 1050145:
                self.assertEqual("Ritalin", text.author)

unittest.main()
import requests
import datetime
import dateutil.parser
import time
import os
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

import crawl_logger

Kakao = 0
DCWrites = 1

def fetch(URL):
    host = urlparse(URL)
    print("[{}]Fetching {}".format(datetime.datetime.now(), URL))

    headers = {
        'Host': host.hostname,
        'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'Accept-Encoding':"gzip, deflate",
        'Connection':"keep-alive",
        'Upgrade-Insecure-Requests': "1"
    }

    req = requests.get(URL, headers)
    content = req
    time.sleep(0.05)
    return content

def crawl(URL, case, log=False):    
    if case == Kakao:
        res = fetch(URL)
        result = ''

        filename = "Kakao"
        result = parse_kakao(res)

        return result

    if case == DCWrites:
        queries = parse_qs(urlparse(URL).query)
        gall = queries['id'][0]
        no = queries['no'][0]

        if not os.path.exists("{}/{}".format(gall, no)):

            res = fetch(URL)
        
            result = parse_dc(res, no)

            if log and not os.path.exists("{}/{}".format(gall, no)):
                content = "{}\n{}\n{}\n{}\n{}"\
                        .format(result.wid,result.author, result.date \
                            , result.title, result.content)
                if crawl_logger.ready_parent_dir(gall):
                    crawl_logger.write(content, filename="{}".format(no))
        else:
            result = ""
        
        return result   

    raise NotImplementedError

def get_dc_url(gall_id, no):
    return "http://gall.dcinside.com/mgallery/board/view/?id={}&no={}"\
        .format(gall_id, no)

def get_dc_major_url(gall_id, no):
    return "http://gall.dcinside.com/board/view/?id={}&no={}"\
        .format(gall_id, no)


class KakaoText(object):
    """docstring for Text."""
    def __init__(self, title, content):
        super(KakaoText, self).__init__()
        self.title = title
        self.content = content
        
def parse_kakao(HTML):
    response = BeautifulSoup(HTML.content, 'html.parser')
    title = response.find('div', id="cover").get_text()
    
    content = response.find('div', id="post-content").get_text()
    
    return KakaoText(title, content)

class DCText(object):
    """docstring for ClassName."""
    def __init__(self, wid, title, author, content, date):
        self.wid = wid
        self.title = title
        self.author = author
        self.content = content
        self.date = date
        

def parse_dc(HTML, id):
    response = BeautifulSoup(HTML.content, 'html.parser')
    title = response.find('span', class_="title_subject")
    if title is None:
        title = "NoArticle"
    else:
        title = title.get_text()
        
    author = response.find('span', {'class':['nickname','in']})
    
    if author is None:
        author = ""
    else:
        author = author.get_text()
        
    content = response.find('div', class_="writing_view_box")
    if content is None:
        content = ""
    else:
        content = content.get_text()
    
    date = response.find('span', class_="gall_date")
    if date is None:
        date = str(datetime.datetime.now())
    else:
        date = date.get_text()
    
    return DCText(int(id), title, author, content, dateutil.parser.parse(date))
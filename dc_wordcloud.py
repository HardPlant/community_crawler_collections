from wordcloud import WordCloud
import matplotlib.pyplot as plt
import datetime
import os
import re
from PIL import Image
import numpy as np
from konlpy.tag import Kkma

kkma=Kkma()

import crawl_logger
from dc_crawler import DCText

def get_mask(logo):
    return np.array(Image.open(logo))

def make_wordcloud(text, logo):
    if logo:
        mask = get_mask(logo)
    
    return WordCloud(\
        font_path="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"\
        ,background_color="white" \
    ,width=1280, height=640, mask=mask).generate_from_text(text)

def plot(text, logo):
    wordcloud = make_wordcloud(text, logo)

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(str(datetime.datetime.now())+".png", quality=100, pad_inches=0, bbox_inches='tight')
    plt.show()

def filter_title(words):
    filters = ['NoArticle','근데','너무','진짜','시발','씨발','아니','이거',\
    '[ミリシタ]','PSTheater','씹타갤','시타갤','존나','현황','제일','씹타','그냥',\
    '그래서','무엇', '때문', '씨이바']

    for filt in filters:
        words = re.sub(filt, '', words)
    
    return words

def filter_content(words):

    words = re.sub('official', '', words)
    words = re.sub('App', '', words)   
    words = re.sub('dc', '', words)    
    words = re.sub('gall', '', words)    
    words = re.sub('inside', '', words)   
    words = re.sub('http', '', words)   
    words = re.sub('https', '', words)   
    words = re.sub('youtube', '', words)   
    words = re.sub('watch', '', words)   
    words = re.sub('타마키갤에', '', words)   
    words = re.sub('watch', '', words)   
    
    words = re.sub('@^(https?|ftp)://[^\s/$.?#].[^\s]*$@iS', '', words)
    
    return words

def filter_nouns(words):
    words = " ".join(kkma.nouns(words))
    return words

def filter_it(words):
    words = filter_nouns(words)
    words = filter_title(words)
    words = filter_content(words)

    return words

def main(path,is_DB=False, start=0, logo=None):
    words = ""
    for file in os.listdir(path):
        if start:
            if int(file) < start:
                continue
        
        with open(path+'/'+file, 'r') as f:
            wid = f.readline()
            author = f.readline()
            datetime = f.readline()
            title = f.readline()
            content = f.read()
            
            words += "{}".format(title)
    
    words = filter_it(words)

    plot(words, logo)

if __name__ == "__main__":
    main('theaterdays', start=1052000, logo="logo.jpg")
#    main('programming', 9204000)
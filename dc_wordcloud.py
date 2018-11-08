from wordcloud import WordCloud
import matplotlib.pyplot as plt
import datetime
import os
import re
from konlpy.tag import Kkma

kkma=Kkma()

import crawl_logger
from dc_crawler import DCText

def make_wordcloud(text):
    return WordCloud(\
        font_path="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"\
        ,background_color="white" \
    ).generate_from_text(text)

def plot(text):
    wordcloud = make_wordcloud(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(str(datetime.datetime.now())+".png", quality=100, pad_inches=0)
    plt.show()

def filter_title(words):
    words = re.sub('NoArticle', '', words)
    words = re.sub('근데', '', words)   
    words = re.sub('너무', '', words)   
    words = re.sub('진짜', '', words)   
    words = re.sub('시발', '', words)   
    words = re.sub('씨발', '', words)   
    words = re.sub('아니', '', words)   
    words = re.sub('이거', '', words)   
    words = re.sub('[ミリシタ]', '', words)   
    words = re.sub('PSTheater', '', words)   
    words = re.sub('씹타갤', '', words)   
    words = re.sub('시타갤', '', words)   
    words = re.sub('존나', '', words)   
    words = re.sub('현황', '', words)   
    words = re.sub('제일', '', words)   
    words = re.sub('씹타', '', words)
    words = re.sub('그냥', '', words)
    words = re.sub('그래서', '', words)
    words = re.sub('무엇', '', words)
    
    
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

def main(path,is_DB=False, start=0):
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

    plot(words)

if __name__ == "__main__":
#    main('theaterdays', start=1048461)
    main('programming', 9204000)
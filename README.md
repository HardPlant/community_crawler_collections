# 커뮤니티 크롤러 & 워드클라우드 생성기

커뮤니티 크롤러 
현재는 디시인사이드만 지원하며, 커뮤니티 리뉴얼 시 깨질 수 있음.

```
usage: main.py [-h] [--gallname gall_name] --start start_article_id --end
               end_article_id [--logs [LOG]] [--major [MAJOR]]

Crawls DC Writings.

optional arguments:
  -h, --help            show this help message and exit
  --gallname gall_name  갤러리 이름
  --start start_article_id
                        시작 게시글 번호
  --end end_article_id  끝 게시글 번호
  --logs [LOG]          파일로 남길 여부
  --major [MAJOR]       메이저 갤러리 여부
```
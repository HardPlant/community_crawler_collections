import argparse
import dc_crawler

parser = argparse.ArgumentParser(description="Crawls DC Writings.")
parser.add_argument('--gallname', dest="gall_name", metavar='gall_name', help="갤러리 이름", default="theaterdays")
parser.add_argument('--start', dest="start_article_id", metavar='start_article_id', type=int, help="시작 게시글 번호", required=True)
parser.add_argument('--end', dest="end_article_id", metavar='end_article_id',type=int, help="끝 게시글 번호", required=True)
parser.add_argument('--logs', dest="log", default=True, nargs='?', help="파일로 남길 여부")
parser.add_argument('--major', dest="major", type=bool, nargs='?', const=True, help="메이저 갤러리 여부")

def main(args):
    gall_name = args.gall_name
    start_article_id = args.start_article_id
    end_article_id = args.end_article_id
    log = args.log
    for index in range(start_article_id, end_article_id+1):
        if args.major:
            url = dc_crawler.get_dc_major_url(gall_name, index)
        else:
            url = dc_crawler.get_dc_url(gall_name, index)

        dc_crawler.crawl(url,dc_crawler.DCWrites, log)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
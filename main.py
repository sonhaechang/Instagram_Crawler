import sys
import argparse
import signal

from instagram_crawling.extract_instagram_tag import extract_hash_tag
from instagram_crawling.instagram_crawler import instagram_main
from instagram_crawling.meta_data import ECTRACT_NUM

def handler(signum, frame):
    sys.exit('프로그램을 종료했습니다.')


def get_arguments():
	parser = argparse.ArgumentParser(
		description='인스그램 해쉬태그 크롤러', 
		formatter_class=argparse.RawTextHelpFormatter
	)

	parser.add_argument(
		'--id', 
		required=True, 
		type=str, 
		help='인스타그램 아이디를 입력해주세요.'
	)

	parser.add_argument(
		'--password', 
		required=True, 
		type=str, 
		help='인스타그램 패스워드를 입력해주세요.'
	)

	parser.add_argument(
		'--hash_tag', 
		required=False, 
		type=str, 
		help='검색할 해쉬태그를 입력해주세요.'
	)

	parser.add_argument(
		'--crawling_option', 
		choices=[1, 2], 
		default=1, 
		type=int, 
		help='1 = 검색, 게시글 url 및 해쉬태그 저장 \n' '2 = 저장된 게시글 url로 해쉬태그만 저장' '기본값은 1 \n'
	)

	parser.add_argument(
		'--file_name', 
		required=False, 
		help='crawling option에서 2 선택시 게시글 url이 저장된 엑셀 파일명 입력 \n' '1 선택시 입력 불필요 \n'
	)

	parser.add_argument(
		'--ectract',
		default=ECTRACT_NUM, 
		type=int, 
		help='해쉬태그 추출 횟수를(1~300번) 입력해주세요. \n'
	)

	return parser.parse_args()

def main():
	args = get_arguments()

	print('\n')

	if args.ectract < 0 or args.ectract > 300:
		sys.exit('---------- 해쉬태그 추출 횟수를 1 ~ 300 범위 안에서 입력해주세요. ---------- \n')
	
	if args.crawling_option == 1:
		if args.hash_tag is None:
			sys.exit('error: 검색할 해쉬태그를 입력해주세요. \n')

		print('---------- 인스타그램 크롤링(게시글 url 저장 및 해쉬태그 저장)을 시작합니다. ---------- \n')

		instagram_main(args)

		print('---------- 인스타그램 크롤링(게시글 url 저장 및 해쉬태그 저장)이 완료되었습니다. ---------- \n')

	elif args.crawling_option == 2:
		if args.file_name is None:
			sys.exit('error: url이 저장된 엑셀 파일명을 입력해주세요. \n')

		print('---------- 인스타그램 크롤링(게시글 url을 이용한 해쉬태그 저장)을 시작합니다. ---------- \n')

		extract_hash_tag(args)

		print('---------- 인스타그램 크롤링(게시글 url 저장 및 해쉬태그 저장)이 완료되었습니다. ---------- \n')

if __name__ == "__main__": 
	signal.signal(signal.SIGINT, handler)
	
	main()
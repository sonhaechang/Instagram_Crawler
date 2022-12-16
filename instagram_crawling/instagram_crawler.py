import time
from datetime import timedelta

from instagram_crawling.utils import (
	make_chrome_driver, 
	instagram_login, 
	search_hash_tag,
)

from instagram_crawling.extract_instagram_post_url import scroll_to_extract_post_url
from instagram_crawling.extract_instagram_tag import extract_hash_tag
from instagram_crawling.meta_data import LOGIN_URL


def instagram_main(args):
	# 크롤링 시작 시간 저장
	start_time = time.time()

	# 드라이버 실행
	driver = make_chrome_driver()
	driver.implicitly_wait(3)
	driver.get(LOGIN_URL)

	# 로그인
	user_id, user_password = args.id, args.password
	instagram_login(driver, user_id, user_password)

	# 해쉬태그 검색
	hash_tag = args.hash_tag
	search_hash_tag(driver, hash_tag)

	time.sleep(5)

	# 마지막까지 스크롤후 post url 결과 및 스크롤 횟수 저장
	get_post_result = scroll_to_extract_post_url(driver, hash_tag)
	scroll_count = get_post_result['scroll_count']
	post_urls = get_post_result['post_urls']
	file_path = get_post_result['file_path']

	# #드라이브 종료
	# driver.quit()

	# # 개시글 url로 해쉬태그 추출 및 결과 저장
	# tag_count = extract_hash_tag(args, file_path)
	tag_count = extract_hash_tag(args, file_path, driver)

	#드라이브 종료
	driver.quit()
	
	print(f'소요시간: {timedelta(seconds=(time.time() - start_time))}') 
	print(f'스크롤 횟수: {format(int(scroll_count), ",")}')
	print(f'추출된 url 수: {format(len(post_urls), ",")}')
	print(f'추출된 해쉬태그 수: {format(int(tag_count), ",")}')
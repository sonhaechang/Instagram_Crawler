
import time
from instagram_crawling.utils import (
	get_post_a_tag,
	scroll_up, scroll_down, get_scroll_position,
)

def get_post_url(post_list):
	''' 게시글 a tag에서 url link 추출하는 함수 '''

	return [post['href'] for post in post_list]

def scroll_to_extract_post_url(driver):
	''' 전체 게시글을 가져올때까지 아래로 스크롤하는 함수 '''

	print('---------- 게시글 가져오기 스크롤을 시작합니다. ---------- \n')
	print('---------- 검색 결과에 따라 시간이 오래 걸릴 수 있습니다. ---------- \n')

	time.sleep(2)

	_is_scroll = True
	_total_scroll_count = 0
	_post_urls = list()

	while _is_scroll:
		# 스크롤후 로딩이나 마지막 게시글을 가져왔거나 다른 문제가 생겼을시 사용을 위한 변수들   
		_updown_scroll = True
		_scroll_count = 0

		# 아래로 스크롤 전 스크롤 위치
		_last_height = get_scroll_position(driver)
		
		# 스크롤 아래로 내리기
		scroll_down(driver)

		# 아래로 스크롤후 스크롤 위치
		_new_height = get_scroll_position(driver)
		
		time.sleep(5)

		# 스크롤을 했는데 버퍼링 때문엔 게시글이 안가져와질때
		if _last_height == _new_height:
			while _updown_scroll:
				# 스크롤 위로 올리기
				scroll_up(driver)

				# 스크롤 아래로 내리기
				scroll_down(driver)

				time.sleep(5)

				# 스크롤되어 게시글을 가져왔을때 while문 탈출
				if _last_height != get_scroll_position(driver):
					_updown_scroll = False

				# 업다운 스크롤 횟수가 30번이 넘었을시 더 이상의 게시글이 없다고 판단하여 스크롤 내리는 함수 종료 
				if _scroll_count >= 30:
					_updown_scroll = False
					_is_scroll = False

				# 스크롤 위아래로 올린 횟수 증가
				_scroll_count += 1

				time.sleep(3)
		
		# 스크롤 횟수 카운트
		_total_scroll_count += 1

		# 게시글 a tag 가져와 href attr에서 url 추출 및 중복제거
		_post_urls += get_post_url(get_post_a_tag(driver))
		_post_urls = list(set(_post_urls))

		# TODO: 스크롤 횟수 입력값이 있을때 입력받은 값으로 설정
		# if SCROLL_COUNT > 0 and _total_scroll_count == SCROLL_COUNT:
		if _total_scroll_count >= 500:
			_is_scroll = False

	print('---------- 게시글 가져오기 스크롤이 완료되었습니다. ---------- \n')

	# 결과, 횟수 반환
	return { 
		'scroll_count': _total_scroll_count,
		'post_urls': _post_urls
	}
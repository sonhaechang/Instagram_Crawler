import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from instagram_crawling.meta_data import (
	DRIVER_DIR,
	LOGIN_BTN, LOGIN_INFO_POPUP, NOTIFY_POPUP,
	SEARCH_INPUT ,FIRST_SEARCH_RESULT,
	TOTAL_POST_COUNT ,POST_A_TAG,
	SCROLL_UP, SCROLL_DOWN, SCROLL_POSITION,
)

def make_chrome_driver():
	return webdriver.Chrome(DRIVER_DIR)

def instagram_login(driver, user_id, user_password):
	''' 인스타그램 로그인 및 알림창 팝업 닫는 함수 '''

	time.sleep(2)

	# 아이디 비밀번호 입력
	# 'uglyfox@hanmail.net' 'mslove18iris'
	driver.find_elements_by_name('username')[0].send_keys(user_id)
	driver.find_elements_by_name('password')[0].send_keys(user_password)

	# 로그인 버튼 클릭
	driver.find_element_by_xpath(LOGIN_BTN).submit()

	time.sleep(2)

	# 로그인 정보 저장 알림팝업창 나중에 하기 버튼 클릭
	driver.find_element_by_xpath(LOGIN_INFO_POPUP).click()

	time.sleep(2)

	# 알림설정 팝업창 나중에 하기 버튼 클릭
	driver.find_element_by_css_selector(NOTIFY_POPUP).click()

def search_hash_tag(driver, hash_tag):
	''' 해쉬태그 검색 함수 '''

	time.sleep(2)

	# 검색 창에 처음 입력받은 해쉬태그를 검색
	driver.find_element_by_css_selector(SEARCH_INPUT).send_keys(hash_tag)

	time.sleep(2)

	# 검색결과에서 가장 첫번째 내용을 클릭
	driver.find_element_by_css_selector(FIRST_SEARCH_RESULT).click()

def get_total_post_count(driver):
	''' 개시글 수 가져오는 함수 '''

	time.sleep(5)

	_count = None

	try:
		# 총 개시물 수 가져오기
		_count = driver.find_element_by_css_selector(TOTAL_POST_COUNT).text

	except Exception:
		time.sleep(5)
		_count = driver.find_element_by_css_selector(TOTAL_POST_COUNT).text

	return int(_count.replace(',', ''))

def get_post_a_tag(driver):
	''' 로딩된 게시글 a tag들을 가져오는 함수 '''

	time.sleep(2)
	html = driver.page_source

	# TODO: lxml을 설치 가능하다면 pip install lxml 설치 후 bs(html, 'lxml')으로 변경하는 것을 추천
	soup = bs(html, 'html.parser')
	return soup.select(POST_A_TAG)

def scroll_up(driver):
	''' 현재 브라우저 창의 높이만큼 스크롤 올리는 함수 '''

	time.sleep(2)

	driver.execute_script(SCROLL_UP)

def scroll_down(driver):
	''' 스크롤 맨아래로 내리는 함수 '''

	time.sleep(2)

	driver.execute_script(SCROLL_DOWN)

def get_scroll_position(driver):
	''' 스크롤 위치 가져오는 함수 '''

	time.sleep(2)

	return driver.execute_script(SCROLL_POSITION)
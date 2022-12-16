import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRIVER_DIR = os.path.join(BASE_DIR, 'driver/chromedriver')
EXCEL_DIR = os.path.join(BASE_DIR, 'excel_result_files/')
BLACK_LIST_PATH = os.path.join(BASE_DIR, 'excel_black_list/black_list.xlsx')

BASE_URL = 'https://www.instagram.com'
LOGIN_URL = f'{BASE_URL}/accounts/login/'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'

ECTRACT_NUM = 300

# 로그인 버튼 
LOGIN_BTN = '//*[@id="loginForm"]/div/div[3]'

# 로그인 정보 저장 알림팝업창 나중에 하기 버튼
LOGIN_INFO_POPUP =  'button._acan._acao._acas._aj1-'

# 알림설정 팝업창 나중에 하기 버튼
NOTIFY_POPUP = 'button._a9--._a9_1'

# 검색창 버튼
SEARHC_BUTTON = 'div.xh8yej3.x1iyjqo2 div:nth-child(2) div.x1n2onr6 a'

# 검색 창
SEARCH_INPUT = 'input._aauy'

# 검색결과에서 가장 첫번째 내용
FIRST_SEARCH_RESULT = 'div.x6s0dn4.x1wzhzgj.x78zum5.xdt5ytf.x5yr21d.x1n2onr6.xh8yej3.xhtitgo div._abm4 a'

# 총 개시물 수
TOTAL_POST_COUNT = 'span._ac2a'

# 개시글들의 a 태그
POST_A_TAG = 'div._aabd._aa8k._aanf a'

# 해쉬태그가 들어있는 title 태그
HASH_TAG_TITLE_TAG = 'title'

# 스크롤 현재 브라우저 크기만큼 올리는 스크립트
SCROLL_UP = 'window.scrollTo(0, window.innerHeight || document.body.clientHeight)'

# 스크롤 맨아래로 내리는 스크립트
SCROLL_DOWN = 'window.scrollTo(0, document.body.scrollHeight);'

# 현재 스크롤 위치 가져오는 스크립트 
# 'return document.body.scrollHeight' not working is return 0
SCROLL_POSITION = 'return document.documentElement.scrollHeight'
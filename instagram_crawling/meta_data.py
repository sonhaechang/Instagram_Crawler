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
LOGIN_INFO_POPUP = 'div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1i0vuye.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37'

# 알림설정 팝업창 나중에 하기 버튼
NOTIFY_POPUP = 'button._a9--._a9_1'

# 검색창 버튼
SEARHC_BUTTON = 'div.x1iyjqo2.xh8yej3 > div:nth-child(2) > span > div > a > div'

# 검색 창
# SEARCH_INPUT = 'input._aauy'
SEARCH_INPUT = 'input.x1lugfcp.x19g9edo.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x5n08af.xl565be.x5yr21d.x1a2a7pz.xyqdw3p.x1pi30zi.xg8j3zb.x1swvt13.x1yc453h.xh8yej3.xhtitgo.xs3hnx8.x1dbmdqj.xoy4bel.x7xwk5j'

# 검색결과에서 가장 첫번째 내용
FIRST_SEARCH_RESULT = 'div.x6s0dn4.x78zum5.xdt5ytf.x5yr21d.x1n2onr6.xh8yej3.xhtitgo > div > div:nth-child(1) > a'

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
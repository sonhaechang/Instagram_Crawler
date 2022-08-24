import os
import re
import sys
import requests
import time

from datetime import datetime

from bs4 import BeautifulSoup as bs

from instagram_crawling.excel_import_export import (
	import_excel, export_excel, update_excel
)
from instagram_crawling.meta_data import (
	EXCEL_DIR, LOGIN_URL, USER_AGENT, HASH_TAG_TITLE_TAG
)

def instagram_login_session(user_id, user_password):
	''' requests를 이용한 로그인 및 session 정보 가져오는 함수 '''

	time = int(datetime.now().timestamp())
	
	# data에 실어서 보낼 인스타그램 로그인 정보 생성
	LOGIN_INFO = {
		'username': user_id,
		'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{user_password}',
		'queryParams': "{}"
	}
	
	# 세션 생성
	InstagramSession = requests.session()

	# cookies에 저장된 csrftoken 값 추출
	getCSRF = InstagramSession.get(LOGIN_URL, headers={'user-agent': USER_AGENT,})
	LoginCSRFtoken = getCSRF.cookies['csrftoken']
	
	# haeder 정보 생성
	RequestHeaders = {
		'user-agent': USER_AGENT,
		'x-csrftoken': LoginCSRFtoken,
	}

	# 인스타그램 로그인
	login = InstagramSession.post(f'{LOGIN_URL}ajax/', data=LOGIN_INFO, headers=RequestHeaders)

	return {'session': InstagramSession, 'login_status': login.status_code}

def duplicate_count_and_make_dict(data_list, data_dict):
	''' list 중복 카운트하여 결과 dict에 추가하는 함수 '''

	for i in data_list:
		try: data_dict[i] += 1
		except: data_dict[i] = 1

def extract_hash_tag(args, file_path=None):
	''' 게시글에서 해쉬태그 추출하는 함수 '''

	print('---------- 게시글에서 해쉬태그 추출 시작합니다. ---------- \n')
	print('---------- 게시글 양에 따라 시간이 오래 걸릴 수 있습니다. ---------- \n')

	try:
		# requests로 인스타그램 로그인후 session 유지 및 가져오기
		login_result = instagram_login_session(args.id, args.password)
		session = login_result['session']
		login_status = login_result['login_status']
		
		# 로그인 성공시 게시글에서 해쉬태그 추출 시작
		if login_status == 200:

			file_name = args.file_name

			# 파일 경로가 인자값으로 있으면 그냥 사용 없으면 파일명을 이용하여 파일 경로 생성
			post_url_file_path = os.path.join(EXCEL_DIR, file_name) \
				if file_path is None else file_path 

			# 게시글 url 엑셀파일명에서 해쉬태그, 날짜를 추출해서 태그 엑셀파일명 생성 및 파일 경로 생성
			file_name_params = post_url_file_path.split('/')[-1].split('_')
			hash_tag = file_name_params[0]
			file_date = file_name_params[1]

			tag_name_file_path = os.path.join(EXCEL_DIR, f'{hash_tag}_{file_date}_tag_name.xlsx')

			# url 주소가 저장된 엑셀 파일을 읽어서 추출시 필요한 값 변수에 저장
			excel_result = import_excel(post_url_file_path, 'post_url')
			extract_count = excel_result['extract_count'] if bool(excel_result) else 0
			post_urls = excel_result['results'] if bool(excel_result) else list()
			post_urls_num = len(post_urls)

			# 에러 발생시 확인시 True로 변경
			extract_error = False

			# 인스타 추출 블락 방지 (특정 갯수 이상일시 True로 변경)
			extract_safe = False

			if int(post_urls_num) == int(extract_count):
				print('---------- 해당 게시글 url 엑셀은 이미 추출이 완료되었습니다. ---------- \n')
				sys.exit('---------- 다시 추출을 원하시면 해당 엑셀 파일의 해쉬태그 추출 횟수를 0을 저장 후 다시 시도해주세요. ---------- \n')

			# 게시글 url에 갯수가 태그 추출 횟수가 같아질때까지 반복 (저장된 게시글 url 수만큼 반복)
			while int(post_urls_num) > int(extract_count):
				post_count = 0

				# 마지막으로 추출한 게시글 url 있으면 다음꺼부터 이어서 해쉬태그 추출 아니면 처음부터
				for post in post_urls[extract_count:]:
					time.sleep(5)

					# 결과값을 저장할 빈 list와 dict 선언
					tag_list = list()
					tag_dict = dict()

					# 해당 url에 게시글 상세 페이지 읽어오기
					url = post
					response = session.get(url)

					# 200 정상 응답이 오면 해쉬태그 추출해서 리스트에 추가
					if response.status_code == 200:
						html = response.content
						soup = bs(html, 'html.parser')
						title = soup.select_one(HASH_TAG_TITLE_TAG).string
						tag_list += re.findall('#[A-Za-z0-9가-힣]+', title)

						extract_count += 1
						post_count += 1

						# 게시글 url 엑셀 파일에 태그 추출 횃수 업데이트
						update_excel(post_url_file_path, 'post_url', extract_count)

						# 해쉬태그 결과 엑셀 파일에서 내용 읽어오기
						_excel_result = import_excel(tag_name_file_path, 'tag_name')

						# 엑셀 파일 있을시 (기존 해쉬태그 결과 엑셀 파일이 존재할떄)
						if bool(_excel_result):
							_tag_result = _excel_result['results']

							# 기존 해쉬태그 결과 추가하기
							tag_dict.update(_tag_result)

							# 해쉬태그 중복 카운트
							duplicate_count_and_make_dict(tag_list, tag_dict)

							# 엑셀에 결과 업데이트
							update_excel(tag_name_file_path, 'tag_name', len(tag_dict), tag_dict)

						# 엑셀 파일 없을시
						else:
							# 해쉬태그 중복 카운트
							duplicate_count_and_make_dict(tag_list, tag_dict)

							# 결과 엑셀로 생성
							export_excel(hash_tag, 'tag_name', tag_dict, file_date)
					else:
						# 정상 응답이 아니면 extract_error 변수값 True려 변경 후 for문 종료
						print('---------- 인스타그램 봇 차단에 의해서 해쉬태그 추출이 끊어졌습니다. 잠시 후 다시 시도해주세요. ---------- \n')
						print('---------- 문제가 지속된다면 개발자에게 문의해주세요. ---------- \n')

						extract_error = True
						break

					if int(args.ectract) >= 100 and post_count >= int(args.ectract):
						print(f'---------- 인스타그램 봇 차단 방지를 위해서 게시글 {args.ectract}개 까지만 확인합니다. ---------- \n')

						extract_safe = True
						break

				# extract_error 혹은 extract_safe 변수값 True이면 while문 종료
				if extract_error or extract_safe:
					break

			print('---------- 게시글에서 해쉬태그 추출이 완료 되었습니다. ---------- \n')
			return import_excel(tag_name_file_path, 'tag_name')['tag_count']
			
		else:
			print('error: 게시글 해쉬태그 추출을 위한 로그인에 실패했습니다. 잠시 후 다시 시도해주세요.\n')
			sys.exit('문제가 지속된다면 개발자에게 문의해주세요. \n')

	except Exception as e:
		return import_excel(tag_name_file_path, 'tag_name')['tag_count']
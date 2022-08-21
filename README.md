## <center>Description</center>
**Instagram Crawler**는 Instagram을 크롤링하여 해쉬태그 추출합니다.

## <center>Description</center>

인스타그램에서 일정 수 이상의 게시물에 접근하면 게시물이 더 이상 로드되지 않습니다. (약 100~300개의 게시물을 크롤링 가능)

따라서 검색된 모든 게시글에서 해쉬태그를 추출 가능하도록 2번의 과정을 걸쳐 크롤링을 진행하게 됩니다.

1. Selenium으로 해쉬태그를 검색하고 맨 아래까지 스크롤하여 모든 게시글의 url을 추출해 엑셀로 저장합니다.  
ex) [검색한 해쉬태그]_[날짜]_post_url.xlsx

2. 엑셀에 저장된 url을 list형식으로 가져와 Requests로 게시물에 하나씩 접근하여 해쉬태그를 추출, 엑셀로 저장합니다.  
이때 게시글 url에 접근할때마다 횟수를 카운트해 url 엑셀(1.에서 저장한 엑셀)에 업데이트하여 게시물이 더 이상 로드되지 않아 크롤링을 못하게 되더라도 이어서 해쉬태그를 추출이 가능합니다.  
ex) [검색한 해쉬태그]_[날짜]_tag_name.xlsx

한번에 해쉬태그를 크롤링 하는것이 아닌 2번에 걸쳐 크롤링을 하기에 시간이 좀 걸립니다.

## <center>Get Started</center>

`pip install -r requirements.txt` 로 패키지를 설치
(Python 3.9.12 사용)

본인이 사용하는 크롬 버전을 확인 후 동일한 버전의 크롬 드라이버를 설치 해서 driver 폴더에 추가해주세요.
[크롬 드라이버 다운로드](https://chromedriver.chromium.org/downloads)

그리고 2가지 방법중 하나를 선택해서 Instagram Crawler 실행합니다.

1. 게시물 url 추출부터 해쉬태그까지 추출하기  
`python main.py --id=[user_id] --password=[user-password --hash_tag=[hash_tag]`

2. 저장된 url에서 해쉬태그만 추출하기  
`python main.py --id=[user_id] --password=[user-password --file_name=[file_name]`

좀 더 자세한 실행 옵션 확인을 원하시면 `python main.py -h` 확인해주세요.# -Instagram_Crawler

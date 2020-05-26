
1. https://gitignore.io/ 로 가면 지워진 파일에 대해 구할 수가 있다. (macOS, Python, Jupyter)
* 복사 > 새로운 파일생성 > 붙여넣기 = 임의로 만들기
* .ignore 파일 생성을 안할 시, 필요없는 파일까지 다운받아버리게 됨 git status 확인하면 나옴 ( OS_store 같은 파일)

2. Branch 추가
* branch에 관련된 명령어는 git branch (git branch arm - arm이라는 branch가 생성)
* Git checkout arm (arm이라는 branch로 이동)
* git branch ( * 이랑 녹색불이 들어와야함, 그러면 그 branch가 작동되고 있다는 말)
* 만들어 놓은 python 파일 열어서 코딩 후 작동하는지 확인
* 추가 후 add, commit, push
            - arm이라는 branch위에서 추가된 내용이 나옴 
* Git checkout master 로 돌아가서 확인
            - 독립적으로 돌아간다는 것을 알 수 있음
* git status 에서 add한 파일이 변경된 상태면 branch를 변경할 수 없음
* commit 하는 파일마다 각각 올라가 있는 상태임
* master로 와서 arm branch에서 했던 작업을 master로 옮겨야함 (git merge arm - 땡길 branch명을 써주면 됨)
* git checkout —(대시대시)(띄고).(점) 을 하면 수정되고 있는 파일을 원래의 최신상태로 되돌릴 수 있음 (commit 단위)
* Git checkout -b ‘branch명'  (checkout을 하는데 만약에 그 branch가 없다면 만들고 추가해라)

3. branch conflict
* 취합을 해야하는 branch(master)가 땡길branch보다 앞서있는 경우
* vi 파일명을 통해 들어가면  ======= 을 통해 위에는 원래의 branch코드 아래는 땡길 branch코드
* 특수문자(head, ===== 등) 다 지우고 버릴 코드는 주석처리!
* 확인 > git add , commit

4. master branch 외 다른 branch를 추가하고자 할 때 그 branch로 checkout 후 git push -u origin branch명
5. branch 삭제
* 개발이 끝났을 때, 실패 했을때
* git branch -D branch명

6. git flow strategy
* Master branch에서는 개발x > conflict 문제, 그리고 최종 완성본을 올리는 곳 
* Master / Hoffix / Release / Develop / Feature
* 특징에 맞는 branch로 이동해서 작업 후 master에 merge하는 방법이 가장 conflict가 일어나지 않는 방법
* 윈도우 - gitforwindows.org / 맥OS - 구글에서 git flow 검색 후 https://danielkummer.github.io/git-flow-cheatsheet/ > setup mac부분
           - 설치 후 git flow feature start ’branch명’
           - git flow feature finish ‘branch명’

6. Collaborate with your co-worker 
* repo에 권한부여 (그러나 인원이 많아질수록 싸울 확률이 높아진다)
* Fork and Merge 방법
            - fork는 repo자체를 내꺼로 복사해서 가져오는 것 
            - 같은 방법으로 폴더 생성 (git clone ..) but 내꺼로 복사된 것이기 때문에 master밖에 존재하지 않고 작업하던 파일도 없음
            - 원본의 레포 clone
            - git remote add [구별할이름] 원본repo주소
            - git pull [구별할이름] develop[원본 branch이름]
* github 웹사이트에 issue 는 bug-writer 부문 (글 쓰는곳 - 내가 뭐 하겠다. 뭐가 잘못됐다 등등) #1 (issue넘버)를 solved : #1 식으로 넣어주면 식별하기 쉬움
* Pull request ( 내가 작업한 것을 원본의 branch에 적용시키고 싶다.)

-------------------------------------------------------------------------------
1. PM 레포를 만든다. Clone
2. PM - develop > fizzbuzz.py
3. Add, commit, push (develop)

DEV
1. Fork팀장의 레포 fork
2. 1-1 할 내용 issue 만들기
3. 뜬 레포를 clone 내주소rd
4. Branch > git remote add pmorigin (팀장주소)
5. Git branch develop > git pull pmorigin develop
6.  Work!!! > add commit push (your develop)

1. GitHub > create pull request ( 내 레포의 해당 branch 에서 pull request)

PM
1. merge

DEV & PM
1. Git pull pmorigin develop

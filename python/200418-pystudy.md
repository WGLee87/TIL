# 공부 내용

## 1. 프로그래머스 코딩테스트 실습예제 풀이 및 반복
- '''
# collections 라이브러리 활용
import collections
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())
solution(participant, completion)	
'''
- key, value값을 갖고 문제를 풀어나가야 했고, collections 라는 라이브러리를 알게 됐다.
- 이미 배운 것중에 알고 있는 것 zip함수로도 풀었으나, 최종 결과에는 조금 못미치는 결과를 얻었고 collection 라이브러리를 통해 문제를 해결하였다.


## 2. 2019k리그1 데이터를 가지고 pandas에서 데이터 전처리 작업 연습
- 데이터 로드
- 데이터 전처리 (groupby, size(), sum(), pivot_table(value, index, columns) 등)
- 상관관계분석을 통해 유효슈팅과 페널티에어리어안에서의 슈팅 중 어떤 것이 득점에 더 상관도가 높을까? 라는 궁금증을 갖고 진행.


## 3. AWS서버 세팅 및 가상환경에서 주피터 노트북 실행
- 며칠 전 처음 했을 때는 잘 되었고, 오늘 처음부터 다시 해보려고 가상환경에서 설치부터 서버 오픈까지 진행
- 안열림 큰일났음.
- 계속 해보고 도저히 안되면 강사님께 sos 요청 예정 

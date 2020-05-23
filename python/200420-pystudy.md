1. 프로그래머스 코딩테스트 연습
 - startswith()
   - '''

phone_book = ['119','97674223','1195524421','123','456','789','12','123','1235','567','88']

def solution(phone_book):
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
        return True

solution(phone_book)

'''

 - startswith란 앞의 변수와 value값이 뒤의 변수의 value중 같은 단어로 시작하는 것이 있으면 True or False를 반환하는 함수


2. k리그1 데이터 전처리작업
 - 선수 별 퍼포먼스 데이터의 누적합 연습
 - reduce, 반복문을 통해 코딩함 (실패)
 - numpy 나 pandas dataframe 의 function중 cumsum()이라는 누적합 기능이 있음
 - cumsum(). 좋은 것을 또 하나 찾았고, 공부했다.
 - def 함수를 만들어 apply 기능을 통해 적용시키는 방법은 조금 더 연습이 필요할듯 하다.


3. 가상환경에서의 주피터 실행
 - 계속적으로 실패중
 - 포트 등록까지 하고 열었는데 열리지 않음 계속적으로.
 - 강사님의 도움이 절실함

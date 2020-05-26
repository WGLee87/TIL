## 공부내용(DB)

1. 학습내용 복습
 - 데이터베이스 확인, 생성, 선택
 - 테이블 생성 및 데이터 생성 후 insert
 - Alter를 활용한 수정 및 삭제
 - Select, from, where를 활용한 조건에 대한 데이터 탐색


2. 엑셀파일 DB로 불러오기
 - 엑셀 csv파일을 DB로 불러오기
 - 불러올 때, 컬럼명 모두 삭제 (but DB 테이블에는 추가해줘야함)
 - 데이터 insert 명령어 (LOAD DATA LOCAL INFILE 'Users/wglee/Desktop/k2_league2.csv' INTO TABLE K_league_2019.k_league1 FIELDS TERMINATED BY ',')
 - 불러오기 전 encoding 상태 확인 및 utf8로 변경해야함

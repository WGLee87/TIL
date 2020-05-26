## 공부내용

# Server - Database - Table

# 1. CREATE

# 1-1 데이터베이스
SHOW DATABASES; # 현재의 데이터베이스 확인
# 생성
CREATE DATABASE test;
# 선택
USE test;
# 확인
SELECT DATABASE();

# 1-2 Table
CREATE TABLE user1(
    user_id INT,
    name VARCHAR(20),
    email VARCHAR(30),
    age INT(3),
    rdate DATE
);
CREATE TABLE user2(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(30) UNIQUE NOT NULL,
    age INT(3) DEFAULT 30,
    rdate TIMESTAMP
);


# 2. 수정(Alter)

# 2-1 데이터베이스
SHOW VARIABLES LIKE 'CHARACTER_SET_DATABASE';
ALTER DATABASE test CHARACTER SET = utf8
# 2-2 Table
ALTER TABLE user2 ADD tmp TEXT 
ALTER TABLE user2 MODIFY COLUMN tmp INT(3)
ALTER TABLE user2 DROP tmp


# 3. 삭제(DROP)

# 3-1 데이터베이스 삭제
CREATE DATABASE tmp
DROP DATABASE tmp
SHOW DATABASES
# 3-2 Table 삭제
DROP TABLE user3
SELECT DATABASE()


# 4. INSERT
INSERT INTO user1(user_id, name, email, age, rdate)
VALUE(1, 'GEON', 'wglee87@gmail.com', 32, now()),
(2, 'HYEON', 'hommeKD@gmail.com', 32, now()),
(3, 'SEOK', 'irelander-kai@gmail.com', 32, now()),
(4, 'MOK', 'dorazy61@gmail.com', 32, now()),
(5, 'GIL', 'jaegil@gmail.com', 32, now()),
(6, 'YEON', 'suyeon@gmail.com', 33, now()),
(7, 'GYU', 'daegyu@gmail.com', 32, now())


# 5. SELECT : 데이터 조회,선택
SELECT user_id, name, age # SELECT 필드명
FROM user1 # FROM 테이블명
# SELECT *
#FROM user1
# user1 테이블에 있는 모든 필드를 가져온다,
SELECT user_id as 'ID', name as 'UserName', age as 'AGES'.  # as는 alius(엘리어스)
FROM user1
# DISTINCT (중복제거)
SELECT DISTINCT(name)
FROM user1
# WHERE 조건검색
# 나이가 32세가 아닌 사용자를 검색해서 유니크한 이름의 갯수를 출력
SELECT COUNT(DISTINCT(name))
FROM user1
WHERE age > 32

SELECT *
FROM user1
WHERE 20 >= age AND age < 40

# BETWEEN A AND B
SELECT *
FROM user1
WHERE age BETWEEN 20 AND 40

# ORDER BY (정렬)
SELECT *
FROM user1
ORDER BY age ASC  #DESC -내림차순 / 안써도 오름차순이라 ASC 안써도됨

SELECT *
FROM user1
ORDER BY name, age DESC

## 연습문제 - 나이가 20세에서 40세사이에 있는 사용자를 이름순으로 내림차순으로 정렬하고, 중복데이터를 제거하고 출력
SELECT DISTINCT(name)
FROM user1
WHERE age between 20 and 39
ORDER BY name DESC

# concat
SELECT name, age, concat(name, '(',age,')') as 'name_age'
FROM user1

# like - where절에서 특정 문자열이 들어간 데이터를 조회
SELECT *
FROM user1
WHERE email like '%@gmail%'
WHERE email not like '%@gmail%' # not도 가능

# in - 여러개의 데이터를 조회할 때 사용
SELECT *
FROM user1
# WHERE name='geon' or name='seok'
WHERE name in('GEON','SEOK')

# LIMIT
SELECT *
FROM user1
LIMIT 3
#----------
SELECT *
FROM user1
LIMIT 3,5


# 6. 업데이트(UPDATE)
UPDATE user1 # UPDATE [테이블명]
SET age=20, rdate='2019.04.23'
WHERE age between 20 and 29

SELECT *
FROM user1
WHERE age between 20 and 29


# 7. DELETE
DELETE FROM user1
WHERE rdate > '2019-04-24'

SELECT *
FROM user1

_______________________________________________________

# 퀴즈1 country 테이블에서 중복을 제거한 continent를 조회하세요.
SELECT Distinct(continent)
FROM country


# 퀴즈2 한국 도시중에 인구가 100만이 넘는 도시를 조회하여 인구순으로 내림차순 하세요.
SELECT Name, population
FROM city
WHERE population > 1000000 and CountryCode = 'kor'
ORDER BY population DESC


# 퀴즈3 city테이블에서 population이 800만~1000만 사이의 도시 데이터를 인구순으로 내림차순 하세요.
SELECT Name, CountryCode, population
FROM city
WHERE population between 8000000 and 10000000
ORDER BY population DESC

# 퀴즈4 country 테이블에서 1940~1950년도 사이에 독립한 국가들을 조회하고 독립한 년도 순으로 오름차순 하세요.
SELECT code, Name, IndepYear, population
FROM country
WHERE IndepYear between 1940 and 1950
ORDER BY INdepYear DESC


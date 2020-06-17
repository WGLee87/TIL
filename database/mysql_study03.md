###### mysql 문법 공부


```python
select CountryCode as Code, Name, Population, concat(Name, '(', Population, ')') as NationPopulation

from city

-- where Population >= 5000000 and Population <= 8000000 or Code = 'CHN' 
where Population between 5000000 and 8000000
--  and CountryCode like "%R%" 
--  and CountryCode in ('BRA', 'GBR') 
--  and CountryCode = 'BRA' or CountryCode = 'GBR'
--  where절에서의 ()는 '그 안에 있는 조건 먼저 처리하겠다' 라는 의미

order by Code asc, Population desc

-- limit 숫자 는 위에서 그 숫자만큼 가져오는 방법 but 앞숫자, 뒤숫자 는 앞숫자 다음번째부터 뒤숫자만큼 이란 의미
limit 5,3


# group by
select CountryCode, count(CountryCode) as count, sum(Population), max(Population), avg(Population) as avg_population
from city
where Population >= 5000000
group by CountryCode
having avg_population > 8000000


# 연습문제
# 1. country 테이블에서 몇개의 대륙이 있는지 조회하세요.
select count(distinct(Continent)) as count
from country
# 2. 각 대륙별 몇개의 국가가 있는지 조회하세요.
select Continent, count(Continent) as count
from country
group by Continent
order by count desc
# 3. city 테이블에서 국가코드별로 총인구가 몇명인지 조회하고 총인구 순으로 내림차순하세요. (총인구가 5천만 이상인 국가코드만 출력)
select CountryCode, sum(Population) as sum
from city
group by CountryCode
having sum >= 50000000
order by sum desc
# 4. countrylanguage 테이블에서 언어별 사용하는 국가수를 조회하고 많이 사용하는 언어를 5위에서 10위까지 조회하세요.
select Language, count(Language) as count
from countrylanguage
group by Language
order by count desc
limit 4,6
# 5. countrylanguage 테이블에서 언어별 15개 국가 이상에서 사용되는 언어를 조회하고 언어별 국가수에 따라 내림차순하세요.
select Language, count(Language) as count
from countrylanguage
group by Language
having count >= 15
order by count desc
# 6. country 테이블에서 대륙별 전체 표면적 크기를 구하고 표면적 크기 순으로 내림차순하세요.
select Continent, sum(SurfaceArea) as sum
from country
group by Continent
order by sum desc



# 소수점 올림, 반올림, 버림 함수
select ceil(12.345)
select round(12.345, 2)
select truncat(12.345, 2)

# 예제
select Code, round(GNP / Population * 1000, 2)
from country

# 조건문
# IF : IF(조건, 참, 거짓)
# 도시의 인구가 100만 이상이면 big city, 100만 미만이면 small city 라고 출력하는 코드
# column : city_scale
select name, population, if(population >= 1000000, 'big city', 'small city') as city_scale
from city

# IFNULL(참, 거짓) - country테이블에서 독립년도가 없으면 0
select Name, IFNULL(IndepYear, 0) as Indepyear
from country

# CASE WHEN (조건) THEN (출력)
# CASE WHEN (조건) THEN (출력)
# CASE WHEN (조건) THEN (출력)
# END as (컬럼명)

# 나라별 10억 이상, 1억 이상, 1억 이하 조건을 출력
select name, population,
case
    when population > 100000000 then 'upper 1 bilion'
    when population > 10000000 then 'upper 100 milion'
    else 'below 100 milion'
end as result
from country

# date_format : 날짜 데이터의 포맷을 변경해주는 함수
# sakila
use sakila

# payment 에서 월별 총 매출 출력
select date_format(payment_date, '%W') as monthly, sum(amount), count(amount)
from payment
group by monthly

# JOIN : merge() - world db
use world
CREATE TABLE addr (
id int(11) unsigned NOT NULL AUTO_INCREMENT,
addr varchar(30) DEFAULT NULL,
user_id int(11) DEFAULT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE user (
user_id int(11) unsigned NOT NULL AUTO_INCREMENT,
name varchar(30) DEFAULT NULL,
PRIMARY KEY (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO user(name)
VALUES ("jin"),
("po"),
("alice"),
("petter");

INSERT INTO addr(addr, user_id)
VALUES ("seoul", 1),
("pusan", 2),
("deajeon", 3),
("deagu", 5),
("seoul", 6);

# inner join
select addr.addr, addr.user_id, user.name
from addr
join user
on addr.user_id = user.user_id

# world 도시이름, 국가이름을 출력
use world
select city.CountryCode, city.name, country.name, city.population
from city
join country
on city.CountryCode = country.code

# left join
select id, addr.addr, addr.user_id, ifnull(user.name, '-')
from addr
left join user
on addr.user_id = user.user_id

# right join
select id, addr.addr, addr.user_id, user.name
from addr
right join user
on addr.user_id = user.user_id

# union : select 문의 결과를 합쳐서 출력 - 자동으로 중복을 제거
select name
from user
union
select addr
from addr

select name
from user
union all
select addr
from addr

# outer join
select user.name, addr.addr, addr.user_id
from user
left join addr
on user.user_id = addr.user_id
union
select user.name, addr.addr, addr.user_id
from user
right join addr
on user.user_id = addr.user_id


# sub-query : 쿼리문 안에 쿼리가 있는 문법
# select, from, where 다 사용 가능

# 전체 나라수, 전체 도시수, 전체 언어수를 출력
select
(select count(*)
from country) as total_country,
(select count(*)
from city) as total_city,
(select count(distinct(language))
from countrylanguage) as total_language

# 800만 이상이 되는 도시의 국가코드, 도시이름, 국가이름, 도시인구수를 출력
select *
from 
    (select countrycode, name, population
    from city
    where population >= 8000000) as city
join
    (select code, name
    from country) as country
on city.countrycode = country.code

# 800만 이상 도시의 국가코드, 국가이름, 대통령이름 출력
select code, name, HeadOfState
from country
where code in(
    select distinct(countrycode)
    from city
    where population >= 8000000
    )
```


```python

```

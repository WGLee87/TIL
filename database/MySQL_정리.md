# QUIZ_1
# 퀴즈1 country 테이블에서 중복을 제거한 continent를 조회하세요.
select distinct(Continent)
from country

# 퀴즈2 한국 도시중에 인구가 100만이 넘는 도시를 조회하여 인구순으로 내림차순 하세요.
select name, population
from city
where population >= 1000000 and countrycode = 'kor'
order by population desc

# 퀴즈3 city테이블에서 population이 800만~1000만 사이의 도시 데이터를 인구순으로 내림차순 하세요.
select name, countrycode, population
from city
where population between 8000000 and 10000000
order by population desc

# 퀴즈4 country 테이블에서 1940~1950년도 사이에 독립한 국가들을 조회하고 독립한 년도 순으로 오름차순 하세요.
select code, concat(name, '(',indepyear,')'), continent, population
from country
where indepyear between 1940 and 1950
order by indepyear asc

# 퀴즈5 countrylanguage 테이블에서 스페인어, 한국어, 영어를 95%이상 사용하는 국가 코드를 Percentage로 내림차순하여 조회하기
select countrycode, language, percentage
from countrylanguage
where percentage >= 95 and language in ('korean', 'spanish', 'english')
order by percentage desc

# 퀴즈6 country테이블에서 code가 A로 시작하고 Governmentform 에 Repulic이 포함되는 데이터를 조회하기
select code, name, continent, governmentform, population
from country
where code like 'a%' and governmentform like '%republic%’


# QUIZ_2
# 퀴즈1 country 테이블에서 몇개의 대륙이 있는지 조회하세요.
select count(distinct(continent))
from country

# 퀴즈2 각 대륙별 몇개의 국가가 있는지 조회하세요.
select continent, count(name)
from country
group by continent
order by count(name) desc

# 퀴즈3 city 테이블에서 국가코드별로 총인구가 몇명인지 조회하고 총인구 순으로 내림차순하세요. (총인구가 5천만 이상인 국가코드만 출력)
select countrycode, sum(population)
from city
group by countrycode
having sum(population) >= 50000000
order by sum(population) desc

# 퀴즈4 countrylanguage 테이블에서 언어별 사용하는 국가수를 조회하고 많이 사용하는 언어를 5위에서 10위까지 조회하세요.
select language, count(language)
from countrylanguage
group by language
order by count(language) desc
limit 4,6

# 퀴즈5 countrylanguage 테이블에서 언어별 15개 국가 이상에서 사용되는 언어를 조회하고 언어별 국가수에 따라 내림차순하세요.
select language, count(language) as count
from countrylanguage
group by language
having count >= 15
order by count desc

# 퀴즈6 country 테이블에서 대륙별 전체 표면적 크기를 구하고 표면적 크기 순으로 내림차순하세요.
select continent, sum(surfacearea)
from country
group by continent
order by sum(surfacearea) desc


# QUIZ_3 : join & sub-query
# 1. 멕시코(Mexico)보다 인구가 많은 나라이름과 인구수를 조회하시고 인구수 순으로 내림차순하세요.
select name, population
from country
where population >
        (
            select population
            from country
            where name like 'mexico'
        )
order by population desc

# 2. 국가별 몇개의 도시가 있는지 조회하고 도시수 순으로 10위까지 내림차순하세요.
select countryname.Name, citycount.count
from (select countrycode, count(name) as count 
            from city 
            group by CountryCode 
            order by count(name) desc 
            limit 10) as citycount
join (select code, Name 
            from country) as countryname
on citycount.CountryCode = countryname.code

# 3. 언어별 사용인구를 출력하고 언어 사용인구 순으로 10위까지 내림차순하세요.
select lang.Language, round(sum((pop.Population * lang.Percentage)/100)) as count
from (select * from countrylanguage) as lang
join (select Code, Population from country) as pop
on lang.CountryCode = pop.Code
group by lang.Language
order by count desc
limit 10

# 4. 나라 전체 인구의 10%이상인 도시에서 도시인구가 500만이 넘는 도시를 아래와 같이 조회 하세요.
select city_p.name, city_p.countrycode, country_p.name, round(city_p.population/country_p.population*100, 2) as population_percentage
from (
    select countrycode, name, population
    from city
    ) as city_p
join (
    select code, name, population
    from country) as country_p
on city_p.countrycode = country_p.code
where round(city_p.population/country_p.population*100, 2) >= 10 and city_p.population >= 5000000
order by round(city_p.population/country_p.population*100, 2) desc

# 5. 면적이 10000km^2 이상인 국가의 인구밀도(1km^2 당 인구수)를 구하고 인구밀도가 200이상인 국가들의 사용하고 있는 언어수가 5가지 이상인 나라를 조회 하세요.
select name, (Population / SurfaceArea) as density 
from country
where surfacearea >= 10000 and (population / surfacearea) >= 200 
order by density desc

select con.Name, count(con.Name) as language_count
from 
    (select Code, Name, SurfaceArea, Population, round(Population / SurfaceArea) as density 
    from country
    where SurfaceArea >= 10000 and round(Population / SurfaceArea) >= 200 order by density desc
    ) as con
join (select CountryCode, Language from countrylanguage) as lan
on con.Code = lan.CountryCode
group by Name
having language_count >= 5
order by language_count desc;

# 6. 사용하는 언어가 3가지 이하인 국가 중 도시인구가 300만 이상인 도시를 조회
# TIP : GROUP_CONCAT(LANGUAGE)을 사용하면 GROUP BY 시 문자열을 합쳐서 볼 수 있음.
# VIEW를 이용하여 query 깔끔하게 수정하기

select countrycode, count(countrycode), group_concat(language)
from countrylanguage
group by countrycode
having count(countrycode) <= 3

select Name, CountryCode, Population 
from city 
where Population > 3000000;

select Code, Name 
from country;

create view q6 as
select lan.CountryCode, c.Name as city_name, c.Population, co.Name, lan.language_count, lan.languages
from (select CountryCode, count(CountryCode) as language_count, group_concat(Language) as languages 
            from countrylanguage
            group by CountryCode having language_count <= 3) as lan
            
join (select Name, CountryCode, Population from city where Population > 3000000) as c
on lan.CountryCode = c.CountryCode

join (select Code, Name from country) as co
on lan.CountryCode = co.Code
order by c.Population desc;

select * from q6


# QUIZ_4 : 
# 1. 가장 돈을 많이 지불한 상위 5명의 고객의 이름과 지불 금액 출력
select naming.customer_id, naming.full_name, paying.amounts
from(
    select customer_id,CONCAT(first_name, last_name) as full_name
    from customer) as naming
join(select customer_id, sum(amount) as amounts from payment group by customer_id) as paying
on naming.customer_id = paying.customer_id
order by amounts desc
limit 5

# 2. 배우별 영화 출연 횟수 출력 (상위 10개) - 컬럼 : 배우이름, 출연횟수 
# - 출연횟수 순으로 내림차순
select actors_name.actor_id, actors_name.full_name
from(
    select ids.actor_id, ids.film_id
    from(
        select actor_id, film_id
        from film_actor) as ids
    join(select film_id, title from film) as film_ids
    on ids.film_id = film_ids.film_id) as actors_id
join(select actor_id, concat    (first_name, ' ', last_name) as full_name from actor) as actors_name
on actors_id.actor_id = actors_name.actor_id [미완성]

# 3. 영화 카테고리별 수입 데이터를 내림차순으로 정렬
select category.name, sum(payment.amount) as amount
from payment, rental, inventory, film_category, category
where
    category.category_id = film_category.category_id
    and film_category.film_id = inventory.film_id
    and inventory.inventory_id = rental.inventory_id
    and rental.rental_id = payment.rental_id
group by category.name
order by amount desc



ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
[VIEW]
use world
create view city_language as (
select city.CountryCode, city.name, city.population, cl.language_count, cl.languages
from (
    select CountryCode
                    , count(Language) as language_count
                    , group_concat(language) as languages
    from countrylanguage
    group by CountryCode
    having language_count <= 3
    ) as cl
    join (
    select CountryCode, name, population
    from city
    where population >= 3000000
    ) as city
    on cl.CountryCode = city.CountryCode )
    

select cl.CountryCode, cl.name as city_name, cl.population, country.name, cl.language_count, cl.languages
from city_language as cl
join country
on cl.CountryCode = country.code
order by cl.population desc





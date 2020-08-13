## 20200813
# 날짜 및 시간 함수, join 함수

-- ADDDATE

CREATE TABLE `date` (
  `date` datetime NOT NULL,
  `date2` datetime NOT NULL,
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into date value (
	adddate('2020-08-12', interval 31 day), adddate('2020-08-12', interval 1 month),
	subdate('2020-08-12', interval 31 day), subdate('2020-08-12', interval 1 month)
);

-- addtime

select addtime('2020-08-12 16:11:00', '1:1:1')
select subtime('2020-08-12 16:11:00', '1:1:1');

-- curdate, curtime ......
select year(curdate()), month(curdate()), dayofmonth(curdate())
select hour(curtime()), minute(curtime()), second(curtime())
select date(curdate()), date(now()), time(curtime()), time(now())

-- datediff(날짜1, 날짜2)
select datediff('2020-08-12', '2019-04-05')
select timediff('16:24:40', '20:00:00')

-- dayofweek
select dayofweek(curdate()), monthname(curdate()), dayofyear(curdate())

-- last_day(날짜)
select last_day('2020-08-08');

-- makedate(연도, 정수) / maketime(시, 분, 초)
select makedate(2020, 177), maketime(12, 11, 10);

-- period_add(연월, 개월수), period_diff(연월1, 연월2)
select period_add(202001, 11), period_diff(202001, 201905);

-- quarter(날짜)
select quarter('2020-08-12');

-- time_to_sec(시간)
select time_to_sec('12:11:10');

# 시스템 정보 함수
select current_user(), datebase();
-- version()
select version()
-- sleep
select sleep(3), '3초 후 발사'
-- found_rows()
-- row_count()



use test

CREATE TABLE info (
	col1 longtext,
    col2 longtext
    ) engine=innodb default charset=utf8 collate=utf8_unicode_ci;

insert into info values (repeat('A', 10000000), repeat('가', 1000000));

select length(col1), length(col2)
from info

show variables like 'max%';

## 피벗의 구현
create table pivot_test (
	uName char(3),
    season char(2),
    amount int
)

insert into pivot_test values('김범수', '겨울', 10), ('윤종신', '여름', 15), ('김범수', '가을', 25), ('김범수', '봄', 3),
('김범수', '봄', 37), ('윤종신', '겨울', 40), ('성시경', '여름', 20), ('성시경', '가을', 40),('윤종신', '여름', 5), ('성시경', '가을', 30);

select *
from pivot_test

-- pivot
select uName,
	sum(if(season='봄', amount, 0)) as '봄',
    sum(if(season='여름', amount, 0)) as '여름',
    sum(if(season='가을', amount, 0)) as '가을',
    sum(if(season='겨울', amount, 0)) as '겨울',
	sum(amount) as '합계'
from pivot_test
group by uName;

-- pivot 연습문제
select season,
	sum(if(uName='김범수', amount, 0)) as '김범수',
    sum(if(uName='김범수', amount, 0)) as '윤종신',
    sum(if(uName='김범수', amount, 0)) as '성시경',
	sum(amount) as '합계'
from pivot_test
group by season


-- JSON 데이터
select *
from pivot_test;

select json_object('uName', uName, 'season', season, 'amount', amount) as 'json값'
from pivot_test
where amount >= 20

set @json='{"pivot_test" :
	[{"uName":"박효신", "season":"겨울", "amount":20}]}';
select json_valid(@json)
select json_search(@json, 'one', '박효신');
-- extract, insert, replace, remove 등이 존재

## 20200813
use test;

create table stdTbl(
	name varchar(10) not null primary key,
    addr varchar(10) not null
) charset='utf8'

create table clubTbl(
	clubName varchar(10) not null primary key,
    roomNo varchar(10) not null
) charset='utf8'

create table stdclubTbl(
	num int auto_increment not null primary key,
	name varchar(10) not null,
    clubName varchar(10) not null,
    foreign key(name) references stdTbl(name),
    foreign key(clubName) references clubTbl(clubName)
) charset='utf8'

insert into stdTbl values ('김범수','경남'), ('성시경','서울'), ('조용필','경기'), ('은지원','경북'), ('바비킴','서울')
insert into clubTbl values ('수영','101호'), ('바둑','102호'), ('축구','103호'), ('봉사','104호')
insert into stdclubTbl values (null,'김범수','바둑'), (null, '김범수','축구'), (null, '조용필','축구'), (null,'은지원','축구'),(null,'은지원','봉사'),(null,'바비킴','봉사')


select stdTbl.name, stdTbl.addr, clubTbl.clubName, clubTbl.roomNo
from stdTbl
	join stdclubTbl
    on stdTbl.name = stdclubTbl.name
	join clubTbl
	on stdclubTbl.clubName = clubTbl.clubName


select clubTbl.clubName, stdTbl.name, stdTbl.addr, clubTbl.roomNo
from stdTbl
	join stdclubTbl
    on stdTbl.name = stdclubTbl.name
	join clubTbl
	on stdclubTbl.clubName = clubTbl.clubName
    

select stdTbl.name, count(stdclubTbl.clubName) as club_count
from stdTbl
	join stdclubTbl
    on stdTbl.name = stdclubTbl.name
	join clubTbl
	on stdclubTbl.clubName = clubTbl.clubName
group by stdTbl.name
order by club_count desc

select stdTbl.name, stdTbl.addr, clubTbl.clubName, clubTbl.roomNo
from stdTbl
	left join stdclubTbl
    on stdTbl.name = stdclubTbl.name
	left join clubTbl
	on stdclubTbl.clubName = clubTbl.clubName
    
select *
from stdTbl
	cross join stdclubTbl

create table empTbl(
	emp char(3),
    manager char(3),
    empTel varchar(8)
);    

insert into empTbl values ('',null,'0000'), ('김전무','나사장','2222'), ('김부장','김전무','2222-1')


select A.emp as '부하직원', B.emp as '직속상사', B.empTel as '직속상사 연락처'
from empTbl as A
	join empTbl as B
    on A.manager =  B.emp
where A.emp = '김부장'

select name, addr from stdTbl
	union all
select clubname, roomNo from clubTbl
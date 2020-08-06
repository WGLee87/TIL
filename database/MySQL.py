create database test

# 변수 선언
set @myVal1 = 5;
set @myVal2 = 3;
set @myVal3 = 4.25;
set @myVal4 = 'name ==> ' ;

select @myVal1, @myVal2 + @myVal3 

select @myVal4, Name
from info
where age >= 30;

insert into info value('suzy', 27, 'suzy@gmail.com');
insert into info value('yoona', 31, 'yoona@daum.net');
insert into info value('yura', 29, 'yura@naver.com');
insert into info value('hyeri', 27, 'hyeri@yahoo.com');
insert into info value('sana', 25, 'sana@naver.com');
insert into info value('jennie', 22, 'jennie@gmail.com');


select @myVal4, Name
from info
where age >= 30;

set @myVar1 = 3;
prepare myquery
	from 'select name, age from info limit ?';
execute myquery using @myVar1


select '100'+'200' as 합계;
select concat('100','200') as 합계;
select concat(100, '200') as 합계;

select if(100>200, '참', '거짓');
select ifnull(null, '널값'), ifnull(100, '널값');
select nullif(100,100), nullif(100,200);

select case 12
			when 1 then '일'
			when 2 then '이'
			when 12 then '십이'
			else 'i dont know'
		end;
        
select char(65);


select bit_length('abc'), char_length('abc'), length('abd');

select format(123.357135, 2);

select left('dsbfsgd', 3), right('sdfsxscv', 3);

# 문자열 대문자/소문자 변경
select ucase('dsbfsDFGd'), lcase('sdfsxsBGFcv');
select upper('dsbfsDFGd'), lower('sdfsxsBGFcv');

# repeat(문자열 반복)
select repeat('hello mysql', 3);

# replace(문자열 대체)
select replace('이것이 mysql이다', '이것이', 'This is');

# reverse(문자열 거꾸로)
select reverse('MySQL');

# space(공백 길이)
select concat('이것이', space(10), 'MySQL이다');

# substring(문자열 시작위치 반환하기)
select substring('독도는 대한민국 영토입니다.', 4);

# substring_index
select substring_index('bhcboy100@naver.com', '@', 1), substring_index('bhcboy100@naver.com', '@', -1);

# 수학 함수(EXP, LOG, LOG2, LOG10, LN)
select log(100), exp(100), ln(100), log2(100), log10(100);

# 수합 함수(MOD)
select MOD(157, 10);

# 수학 함수(거듭제곱합)
select POW(2,3), SQRT(9);
-- POW() 와 POWER()는 동일

# rand() - 0에서 1사이의 실수를 추출
select rand(), floor(1 + (rand() * (6-1)));

# truncate() - 기준이 되는 위치까지 구하고 나머지는 버림
select truncate(12345.12345,2), truncate(12345.12345, -2);
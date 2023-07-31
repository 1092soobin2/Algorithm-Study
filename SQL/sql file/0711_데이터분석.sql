ㅈuse titanic;

CREATE TABLE titanic_data (
	passenger_id 	SMALLINT,
    survived		TINYINT,
    pclass			TINYINT,
    name			VARCHAR(100),
    sex				VARCHAR(6),
    age				FLOAT,
    sibsp			SMALLINT,
    parch			SMALLINT,
    ticket			VARCHAR(20),
    fare			FLOAT,
    cabin			VARCHAR(20),
    embarked		VARCHAR(20),
    PRIMARY KEY(passenger_id)
);

use sakila;


-- 아래의 각 컬럼을 출력 하시오.
-- 영화제목, 
-- 대여기간, 
-- 대여분류 : 조건1 대여기간이 3일 이하인 경우 ‘대여기간:S’
--                   조건2 대여기간이 7일 이하인 경우 ‘대여기간:M’
--                   아니면 ‘대여기간:L’

SELECT title, rental_duration, (CASE WHEN rental_duration <= 3 THEN 'S'
									WHEN rental_duration <= 7 THEN 'M'
                                    ELSE 'L'
								END) '대여분류'
FROM film;

-- COUNT()식을 사용하여 대여분류 별 총 갯수를  출력 하시오.
SELECT f.class, COUNT(*) AS '총 개수'
FROM (SELECT title, rental_duration, (CASE WHEN rental_duration <= 3 THEN 'S'
									WHEN rental_duration <= 7 THEN 'M'
                                    ELSE 'L'
								END) class
		FROM film) f
GROUP BY f.class;

SELECT
	COUNT(CASE WHEN rental_duration <= 3 THEN 1 END) '대여 기간 S',
	COUNT(CASE WHEN rental_duration <= 7 AND rental_duration > 3 THEN 1 END) '대여 기간 M',
    COUNT(CASE WHEN rental_duration > 7 THEN 1 END)'대여 기간 L'
FROM film;

-- 대여 기간에 따라 연체료를 계산하는 쿼리를 작성하시오.
-- 대여일은 DATEDIFF(return_date, rental_date)로 구하시오.
-- 3일 이하는 연체료 = 0
-- 7일 이하는 연체료 = 3일 이후로 매일 1.5$ (대여일 6일이면 4.5$)
-- 7일 이상은 연체료 = 3일 이후로 매일 2$ (대여일 10일이면 14$)
SELECT rental_id, DATEDIFF(return_date, rental_date) '연제일',
	CASE WHEN DATEDIFF(return_date, rental_date) <= 3 THEN 0
		WHEN DATEDIFF(return_date, rental_date) <= 7 THEN 1.5 * (DATEDIFF(return_date, rental_date) - 3)
		ELSE (DATEDIFF(return_date, rental_date) - 3) * 2
	END '연체료'                 
from rental;

-- 총 대여횟수 기준으로 고객의 등급을 나누는 쿼리를 작성하시오.
-- 대여횟수 50이상 골드
-- 대여횟수 30이상 실버
-- 이하는 브론즈
SELECT customer_id,
	COUNT(*) AS rental_cnt,
	(CASE WHEN COUNT(*) >= 50 THEN 'gold'
			WHEN COUNT(*) >= 30 THEN 'silver'
			ELSE 'bronze'
	END) rate
FROM customer c
	INNER JOIN rental r USING(customer_id)
GROUP BY c.customer_id;

### 결측치 처리 ### 
use titanic;

-- 결측값 개수를 출력하시오.
-- 결측비율을 출력하시오.
WITH missing_sum AS
	(SELECT 
		SUM(CASE WHEN passenger_id 	IS NULL THEN 1 ELSE 0 END) passenger_id,
		SUM(CASE WHEN survived 		IS NULL THEN 1 ELSE 0 END) survived,
		SUM(CASE WHEN pclass 		IS NULL THEN 1 ELSE 0 END) pclass,
		SUM(CASE WHEN name 			= ''	THEN 1 ELSE 0 END) name,
		SUM(CASE WHEN sex 			= ''	THEN 1 ELSE 0 END) sex,
		SUM(CASE WHEN age	 		IS NULL THEN 1 ELSE 0 END) age,
		SUM(CASE WHEN sibsp 		IS NULL THEN 1 ELSE 0 END) sibsp,
		SUM(CASE WHEN parch 		IS NULL THEN 1 ELSE 0 END) parch,
		SUM(CASE WHEN ticket 		IS NULL THEN 1 ELSE 0 END) ticketfare,
		SUM(CASE WHEN fare 			= ''	THEN 1 ELSE 0 END) fare,
		SUM(CASE WHEN cabin 		= '' 	THEN 1 ELSE 0 END) cabin,
		SUM(CASE WHEN embarked 		= ''	THEN 1 ELSE 0 END) embarked,
		COUNT(*)												total
	FROM titanic_data)
SELECT age/total * 100, cabin/total * 100, embarked/total * 100
FROM missing_sum;

-- 결측값이 많은 컬럼은 무엇인가?
-- 각 결측값들은 어떻게 처리하는 게 좋은가?

-- 대여 수가 많은 고객의 랭킹을 부여하고 고객ID, 이름, 랭킹을 출력 하시오.
-- customer_list view 를 사용해보자.
-- 모든 순위함수를 컬럼으로 출력해보자.
use sakila;

SELECT ID, name, COUNT(*) 'cnt',
	RANK() 			OVER(ORDER BY COUNT(r.rental_id) DESC) 'RANK',
    DENSE_RANK() 	OVER(ORDER BY COUNT(r.rental_id) DESC) 'DENSE_RANK',
    ROW_NUMBER() 	OVER(ORDER BY COUNT(r.rental_id) DESC) 'ROW_NUMBER'
FROM customer_list cl
	LEFT OUTER JOIN rental r ON cl.ID = r.customer_id
GROUP BY cl.ID;


-- 이상치가 있는 컬럼은 무엇인가?
-- 분석이 필요한 컬럼에 대해 MIN, MAX를 구해보자.
use titanic;

SELECT
	CONCAT(MIN(passenger_id), 	'/', MAX(passenger_id)) 	'passenger_id min, max',
    CONCAT(MIN(survived),		'/', MAX(survived)) 		'survived min, max',
    CONCAT(MIN(pclass),			'/', MAX(pclass)) 			'pclass min, max',
    CONCAT(MIN(age),			'/', MAX(age))		 		'age min, max',
    CONCAT(MIN(sibsp),			'/', MAX(sibsp))	 		'sibsp min, max',
    CONCAT(MIN(parch),			'/', MAX(parch))	 		'parch min, max',
    CONCAT(MIN(fare),			'/', MAX(fare))		 		'fare min, max'
FROM titanic_data;


-- 이상치가 있는 컬럼에 대해 소수점 데이터를 검색

-- 3가지 방식으로 검색
-- 1. ROUND( ) 함수 사용 -  ROUND(인자,자릿수) /자릿수 생략은 첫번째 자리 
-- 2. FLOOR( ) 함수 사용  -  소수점 아래 값 버림
SELECT age, ROUND(age) 'ROUND', FLOOR(age) 'FLOOR'
FROM titanic_data
WHERE ROUND(age) != age 
	OR FLOOR(age) != age;
    
-- 3. 정규 표현식 사용
SELECT age FROM titanic_data WHERE age REGEXP("\\.[0-9]+");


-- 이상치가 있는 컬럼들의 표준편차, 평균을 출력하는 쿼리를 작성하시오.
-- 표준편차는 stddev( ) 함수
SELECT age, (age - agg.avg_age) / agg.sd_age AS 'z-score'
FROM titanic_data, (SELECT AVG(age) avg_age, STDDEV(age) sd_age FROM titanic_data) agg
WHERE (age - agg.avg_age) / agg.sd_age > 2 
	OR (age - agg.avg_age) / agg.sd_age < -2;

-- 중요한 것은 도메인 지식! 이건 그냥 맛보기~	
SELECT fare, (fare - agg.avg_fare) / agg.sd_fare AS 'z-score'
FROM titanic_data, (SELECT AVG(fare) avg_fare, STDDEV(fare) sd_fare FROM titanic_data) agg
WHERE (fare - agg.avg_fare) / agg.sd_fare > 2 
	OR (fare - agg.avg_fare) / agg.sd_fare < -2;

-- survived 컬럼의 값을 [생존/사망]으로 
-- sex 컬럼의 값을 [남성/여성]으로 변경
-- embarked 컬럼의 값을[프랑스,아일랜드,영국]으로 변경
CREATE VIEW titanic_pre AS (
	SELECT
		passenger_id,
		CASE survived WHEN 1 THEN '생존' ELSE '사망' END 'survived',
		pclass, name,
		CASE sex WHEN 'male' THEN '남성' WHEN 'female' THEN '여성' ELSE NULL END 'sex',
		age, sibsp, parch, ticket, fare, cabin,
		CASE embarked WHEN 'C' THEN '프랑스' WHEN 'Q' THEN '아일랜드' WHEN 'S' THEN '영국' ELSE NULL END 'embarked',
        CASE WHEN name LIKE '%Master%' THEN 'Master'
			WHEN name LIKE '%Miss%' THEN 'Miss'
			WHEN name LIKE '%Mrs%' THEN 'Mrs'
            WHEN name LIKE '%Mr%' THEN 'Mr'
            WHEN name LIKE '%Ms%' THEN 'Ms'
		END AS 'title'
	FROM titanic_data);

SELECT passenger_id, title
FROM (
	SELECT passenger_id, SUBSTR(name FROM LOCATE(', ', name) + 2 FOR LOCATE('. ', name) - LOCATE(', ', name) - 2) title
	FROM titanic_data) t
WHERE t.title NOT IN ('Mr', 'Mrs', 'Master', 'Miss');

-- Pclass별 생존률과 평균 연령을 조회하시오.
SELECT pclass, AVG(age) '평균 연령', AVG(survived) '생존률'
FROM titanic_data
GROUP BY pclass;

SELECT pclass, survived, COUNT(*)
FROM titanic_data
GROUP BY pclass, survived;

-- 호칭(Title 컬럼)별 생존률과 평균 연령을 조회하시오.
SELECT title '호칭', AVG(CASE survived WHEN '생존' THEN 1 ELSE 0 END) '생존률', FLOOR(AVG(age)) avg_age
FROM titanic_pre
GROUP BY title;

-- age의 결측치는 무엇으로 채우는게 합리적인가? -> 호칭에 따른 각 연령의 평균값으로 채운다.
SELECT title, name, sex
FROM titanic_pre
WHERE (title IN('Mr', 'Master') AND sex = '여성')
	OR (title IN('Mrs', 'Ms', 'Miss') AND sex = '남성');

-- age의 이상치와 결측치를 제거하고 모든 컬럼을 포함시킨 데이터를 조회하는 쿼리를 작성하시오.
WITH avg_age_according_to_title AS (
	SELECT title, AVG(CASE survived WHEN '생존' THEN 1 ELSE 0 END) '생존률', FLOOR(AVG(age)) avg_age
	FROM titanic_pre
	GROUP BY title)
SELECT title, age, avg_age
FROM titanic_pre tp
	INNER JOIN avg_age_according_to_title USING(title);

WITH avg_age_according_to_title AS (
	SELECT title, FLOOR(AVG(age)) avg_age
	FROM titanic_pre
	GROUP BY title)
SELECT passenger_id, survived, pclass, name, sex,
	FLOOR(CASE WHEN age IS NULL THEN avg_age ELSE age END) 'age',
    sibsp, parch, ticket, fare, cabin, embarked, title
FROM titanic_pre
	INNER JOIN avg_age_according_to_title USING(title);
    
-- 내용이 이상 없다면 최종적으로 titanic_analysis 뷰를 생성하시오.
CREATE VIEW titanic_pro AS (
	WITH avg_age_according_to_title AS (
		SELECT title, FLOOR(AVG(age)) avg_age
		FROM titanic_pre
		GROUP BY title)
	SELECT passenger_id, CASE survived WHEN '생존' THEN 1 ELSE 0 END 'survived', pclass, name, sex,
		FLOOR(CASE WHEN age IS NULL THEN avg_age ELSE age END) 'age',
		sibsp, parch, ticket, fare, embarked, title
	FROM titanic_pre
		INNER JOIN avg_age_according_to_title USING(title)
);

-- 전체 생존률을 조회하시오.
SELECT AVG(survived) 'total 생존률'
FROM titanic_pro;

-- 성별에 따른 생존자 수와 생존률을 조회하시오.
SELECT sex, AVG(survived) '생존률'
FROM titanic_pro
GROUP BY sex;

-- 탑승항구별 생존자수 사망자수
SELECT embarked,
	COUNT(CASE survived WHEN 1 THEN 1 ELSE NULL END) '생존자 수',
    COUNT(CASE survived WHEN 0 THEN 1 ELSE NULL END) '사망자 수',
    COUNT(*)										'총 인원'
FROM titanic_pro
GROUP BY embarked;

-- 연령대별로 승객수, 생존자수, 생존률을 조회하시오.
	-- 18세 이하 미성년자, 
	-- 18세이상 65세이하 성인, 
	-- 65세 이상 노인으로 구분
SELECT age_range '연령대', COUNT(*) '승객수', COUNT(CASE survived WHEN 1 THEN 1 ELSE NULL END) '생존자수', AVG(survived) '생존률'
FROM titanic_pro
	INNER JOIN (SELECT passenger_id, 
					CASE WHEN age <= 18 THEN '미성년자'
						WHEN age <= 65 THEN '성인'
						ELSE '노인'
					END age_range
				FROM titanic_pro) range_table USING(passenger_id)
GROUP BY age_range;


-- 객실등급별 생존인원
SELECT pclass '객실등급', COUNT(CASE survived WHEN 1 THEN 1 ELSE NULL END) '생존인원', COUNT(*) '총인원'
FROM titanic_pro
GROUP BY pclass
ORDER BY pclass;

-- 호칭별 생존율 , 총인원
SELECT title '호칭', AVG(survived) '생존율', COUNT(*) '총인원'
FROM titanic_pro
GROUP BY title;

-- pclass 별 title, tile별 총 인원
SELECT pclass '객실등급', title '호칭', COUNT(*) '총인원'
FROM titanic_pro
GROUP BY pclass, title
ORDER BY pclass;

-- pclass, title 별 생존주 수와 사망자수
SELECT pclass '객실등급', title '호칭', COUNT(CASE survived WHEN 1 THEN 1 ELSE NULL END) '생존인원', COUNT(CASE survived WHEN 0 THEN 1 ELSE NULL END) '사망인원', count(*) '총인원'
FROM titanic_pro
GROUP BY pclass, title
ORDER BY pclass;

-- 생존자, 사망자 별 평균 요금 조회
SELECT CASE survived WHEN 1 THEN '생존자' ELSE '사망자' END '생존 여부', AVG(fare) '평균 요금'
FROM titanic_pro
GROUP BY survived;

-- 탑승항구, 객실등급에 따른 승객수, 생존자수
SELECT embarked '탑승항구', pclass '객실등급', COUNT(*) '승객수', COUNT(CASE survived WHEN 1 THEN 1 ELSE NULL END) '생존자수'
FROM titanic_pro
GROUP BY embarked, pclass
ORDER BY embarked;

-- 가족 동반 탑승객, 가족 미동반 승객들의 생존자 수, 사망자 수, 생존률
SELECT CASE family WHEN 1 THEN '가족 동반' ELSE '가족 미동반' END '가족동반여부',
	COUNT(CASE survived WHEN 1 THEN 1 ELSE NULL END) '생존자수',
	COUNT(CASE survived WHEN 0 THEN 1 ELSE NULL END) '사망자수',
	AVG(survived) '생존율'
FROM titanic_pro
	INNER JOIN (SELECT passenger_id,
						CASE WHEN sibsp + parch = 0 THEN 0 ELSE 1 END 'family'
				FROM titanic_pro) family_table USING(passenger_id)
GROUP BY family;

-- 보호자가 여자인 경우의 생존률 (성별이 여자이면서)



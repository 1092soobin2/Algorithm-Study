use sakila;


-- [Customer Table]
-- 전체 고객에 대한 customer_id, first_name, last_name, email 정보를 출력하시오.
SELECT customer_id, first_name, last_name, email FROM sakila.customer;

-- customer_id가 1인 고객만 모든 정보를 출력하시오.
SELECT * FROM customer WHERE customer_id = 1;

-- [film Table]
-- 영어로 된 영화	를 모두 출력하시오. 
-- PG-13등급의 영화를 모두 출력하시오.
SELECT *
FROM sakila.film
WHERE language_id = 1
	AND rating = 'PG-13';
    
-- [actor Table]
-- 성이 KILMER인 배우를 모두 출력하시오.
SELECT * FROM actor WHERE last_name = 'KILMER';

-- [film Table] 
-- 상영시간이 60분 이상인 영화의 title, length를 출력하시오.
SELECT title, length
FROM film
WHERE length >= 60;

-- NC-17 등급(rating) 외 모든 등급의 영화의 title, length, rating을 출력하시오.
SELECT title, length, rating
FROM film
WHERE rating != 'NC-17';

-- [film Table] 
-- 상영시간이 60분 이상이고,전체 관람(G)등급의 영화의 title, length, rating을 출력하시오.
SELECT title, length, rating
FROM film
WHERE length >= 60 
	AND rating = 'G';

-- [actor Table]
-- first name이 TOM, last name이 MCKELLEN인 배우를 출력하시오.
SELECT *
FROM actor
WHERE first_name = 'TOM'
	AND last_name = 'MCKELLEN';

-- [film Table] 
-- 관람등급이 G, PG, PG-13인 영화의 title, rating을 출력하시오.
SELECT title, rating
FROM film
WHERE rating IN('G', 'PG', 'PG-13');

-- 관람등급이 G, PG, PG-13가 아닌 영화의 title, rating을 출력하시오.
SELECT title, rating
FROM film
WHERE rating NOT IN('G', 'PG', 'PG-13');

-- [payment Table]
-- 2005년 7월 지출합계가 5$ 이상인 데이터를 출력하시오.
SELECT * 
FROM payment
WHERE payment_date >= '2005-07-01'
	AND payment_date < '2005-08-01'
	AND amount >= 5;


SELECT *
FROM payment
WHERE payment_date >= '2005-07-11'
	AND payment_date <= '2005-07-12';
    
-- [film Table] 
-- special_feature에 Trailer가 포함된 영화를 모두 출력하시오.
SELECT *
FROM film
WHERE special_features LIKE '%Trailer%';
-- WHERE FIND_IN_SET('Trailers', special_features) > 0;

-- [rental Table] 
-- 대여중인 DVD렌탈 데이터를 모두 출력하시오.
-- 반납이 완료된 DVD렌탈 데이터를 모두 출력하시오.
SELECT * FROM rental WHERE return_date IS NOT NULL;

-- [customer Table]
-- 주소별 고객 수를 출력하시오. (address_id 기준)
SELECT address_id, COUNT(*) as cnt FROM customer GROUP BY address_id;

-- [film Table] 
-- 각 등급별 영화 개수를 구하여 출력하시오.
SELECT rating, COUNT(*) FROM film GROUP BY rating;

-- 영화가 G또는 PG 등급인 영화 수를 출력하시오.
SELECT rating, COUNT(*) AS '등급별 영화 수' FROM film WHERE rating IN('G', 'PG') GROUP BY rating;

-- 각 등급별 영화 개수, 등급, 평균 대여 비용을 출력하시오.
SELECT rating, COUNT(*) '영화 개수', AVG(replacement_cost) '평균 대여 비용' FROM film GROUP BY rating;

-- [film Table] 
-- 대여 기간(rental_duration) 별 평균 보상금액(replacement_cost)을 출력하시오.
SELECT rental_duration, AVG(replacement_cost) '대여 기간 별 평균 보상 금액' FROM film GROUP BY rental_duration;

-- 대여 기간(rental_duration) 별 평균 보상금액(replacement_cost)이 20$ 이상인 데이터만 출력하시오.
SELECT rental_duration, AVG(replacement_cost) '대여 기간 별 평균 보상 금액' FROM film GROUP BY rental_duration HAVING AVG(replacement_cost) >= 20;

-- [film Table] 
-- 보상금액(replacement_cost)이 높은 순으로 영화 title, replacement_cost를 출력하시오.
SELECT title, replacement_cost AS r_cst FROM film ORDER BY r_cst DESC;
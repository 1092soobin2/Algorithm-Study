use sakila;

--  [staff, store, address table]
-- 각 직원이 속한 지점의 주소와 직원 정보(id, name)을 출력하시오.
SELECT staff.staff_id, staff.username, address.address
FROM staff
	INNER JOIN store ON staff.store_id = store.store_id
	INNER JOIN address ON address.address_id = store.address_id;

-- [customer, address table]
-- 모든 고객의 first name, last name, address를 출력하시오.
SELECT first_name, last_name, a.address FROM customer c LEFT OUTER JOIN address a ON c.address_id = a.address_id;

SELECT COUNT(*) FROM customer c LEFT OUTER JOIN address a ON c.address_id = a.address_id;
SELECT COUNT(*) FROM customer c RIGHT OUTER JOIN address a ON c.address_id = a.address_id;

-- [customer table]
-- last name이 다른 고객의 first name과 같은 결과를 모두 출력하시오.
SELECT c1.first_name AS first_1, c2.first_name AS first_2, c1.last_name AS last_1, c2.last_name AS last_2
FROM customer c1 INNER JOIN customer c2 ON c1.last_name = c2.first_name;

-- 암묵적으로 같은 필드를 기준으로 Join 수행
-- Customer table과 Rental table을 Natural join 하면?
SELECT * FROM customer NATURAL JOIN rental;


-- 도시별 고객 수를 모두 출력하시오. 
-- JOIN 해야할 테이블들은? address, city, customer
-- 결합기준?
-- 고객수? GROUP BY city_id
SELECT t.city_id, t.city, COUNT(*) '도시별 고객 수'
FROM customer c 
	INNER JOIN address a ON c.address_id = a.address_id
    INNER JOIN city t ON t.city_id = a.city_id
GROUP BY t.city_id;
    
-- LONDON 도시의 고객수를 출력하시오.
SELECT t.city_id, t.city, COUNT(*) '도시별 고객 수'
FROM customer c 
	INNER JOIN address a ON c.address_id = a.address_id
    INNER JOIN city t ON t.city_id = a.city_id
GROUP BY t.city_id
HAVING t.city = 'LONDON';

-- 대여 매출이 가장 높은 영화 5개를 출력 하시오.
SELECT inventory.film_id, film.title, sum(payment.amount) '대여 매출'
FROM rental
	INNER JOIN payment ON rental.rental_id = payment.rental_id
    INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id
    INNER JOIN film ON film.film_id = inventory.film_id
GROUP BY inventory.film_id
ORDER BY sum(payment.amount) DESC
LIMIT 5;
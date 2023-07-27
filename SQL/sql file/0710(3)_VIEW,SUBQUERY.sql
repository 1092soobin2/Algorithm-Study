use sakila;

-- [actor, film_actor table]
-- film_id가2인 영화에 출연한 영화배우를 모두 출력하시오.
SELECT *
FROM (SELECT DISTINCT actor_id
		FROM film_actor
        WHERe film_id = 2) AS fa
	INNER JOIN actor ON fa.actor_id = actor.actor_id;

SELECT * 
FROM actor
WHERE actor_id in (SELECT DISTINCT actor_id
			FROM film_actor
			WHERe film_id = 2);

-- [actor, film table]
-- ALONE TRIP에 출연한 영화배우를 모두 출력 하시오.
SELECT *
FROM actor 
WHERE actor_id in (
	SELECT actor_id
	FROM film_actor
	WHERE film_id = (
		SELECT film_id
		FROM film
		WHERE title LIKE 'ALONE TRIP'));

-- 이름이 “TOM”, “JULIA”인 영화배우가 출연하는 영화를 모두 출력 하시오. (732.33)
SELECT film_id, film.title
FROM film
WHERE film_id IN (SELECT film_id
					FROM film_actor
                    WHERE actor_id IN (SELECT actor_id
										FROM actor
                                        WHERE first_name IN ('TOM', 'JULIA')));

-- [staff, store, address table]
-- 각 직원이 속한 지점의 주소와 직원 정보(id, name)을 출력하시오.
SELECT staff.staff_id, staff.username, (SELECT address FROM address WHERE address_id = store.address_id) AS '주소'
FROM staff
	INNER JOIN store ON staff.store_id = store.store_id;

-- 액션 영화를 대여한 고객의 “풀네임”과 이메일 주소를 출력 하시오.
-- 풀네임은 CONCAT(문자열1, 문자열2,….) 함수를 사용하시오.
SELECT DISTINCT CONCAT(c.last_name, ' ', c.first_name) '풀네임', c.email
FROM rental r
	INNER JOIN inventory i ON r.inventory_id = i.inventory_id
    INNER JOIN film_list fl ON fl.FID = i.film_id
    INNER JOIN customer c USING(customer_id) -- ON r.customer_id = c.customer_id 
WHERE fl.category = 'Action';


-- 영화 제목, 카테고리, 해당 카테고리의 총 영화 수를 출력 하시오.
-- 2349.5
SELECT f.title, c.name, cc.cnt
FROM film_category fc
	INNER JOIN film f ON fc.film_id = f.film_id
    INNER JOIN category c ON c.category_id = fc.category_id
	INNER JOIN (SELECT category_id, COUNT(*) AS 'cnt'
				FROM film_category
                GROUP BY category_id) cc ON cc.category_id = c.category_id;

-- 19819.81
SELECT fl1.title, fl1.category, fl2.cnt
FROM film_list fl1
	INNER JOIN (SELECT category, COUNT(*) AS 'cnt'
				FROM film_list
                GROUP BY category) fl2 ON fl1.category = fl2.category;


-- 이름이 “TOM”, “JULIA”인 영화배우가 출연한 영화를 모두 출력 하시오.
-- 조인으로 하도록 쿼리를 수정하시오. 522.09
SELECT f.film_id, f.title
FROM film f
	INNER JOIN film_actor fa ON f.film_id = fa.film_id
    INNER JOIN actor a ON a.actor_id = fa.actor_id
WHERE a.first_name IN ('TOM', 'JULIA');

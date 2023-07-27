USE movielens;

CREATE TABLE user (
	user_id		INT 			PRIMARY KEY,
	gender		VARCHAR(1),
    age			TINYINT,
    occupation	INT,
    zipcode		VARCHAR(10)
);

CREATE TABLE movie (
	movie_id	INT				PRIMARY KEY,
    title		VARCHAR(100),
    genres		VARCHAR(100)
);

CREATE TABLE rating (
	user_id		INT,
    movie_id	INT,
    rating		TINYINT,
    `timestamp`	VARCHAR(20),
    PRIMARY KEY(user_id, movie_id),
    FOREIGN KEY(user_id) 	REFERENCES	user(user_id),
    FOREIGN KEY(movie_id)	REFERENCES	movie(movie_id)
);

--  [문제1] 각 사용자가 평가한 영화 개수를 조회하시오.
SELECT user.user_id, COUNT(*) '평가한 영화 개수'
FROM user
	LEFT OUTER JOIN rating USING(user_id)
GROUP BY user.user_id;

--  [문제2] 가장 많은 리뷰를 받은 영화 TOP 10조회하시오.
SELECT movie.*, COUNT(*) 'rating_cnt', RANK() OVER(ORDER BY COUNT(*) DESC) '순위'
FROM movie
	INNER JOIN rating USING(movie_id)
GROUP BY movie_id
LIMIT 10;

--  [문제3] 리뷰가 100개 이상인 영화들의 총 평점 횟수를 조회하시오.
SELECT SUM(rm.rating_cnt) '총 평점 횟수'
FROM (SELECT movie.movie_id, COUNT(*) 'rating_cnt'
		FROM movie
			INNER JOIN rating USING(movie_id)
		GROUP BY movie_id
        HAVING COUNT(*) >= 100) rm;

-- [문제4] Action장르의 영화를 평점순으로 조회하시오.
SELECT movie.*, AVG(rating.rating) '평점'
FROM movie
	LEFT OUTER JOIN rating USING(movie_id)
WHERE movie.genres LIKE '%Action%'
GROUP BY movie_id
ORDER BY AVG(rating.rating) DESC;


-- 중복 데이터 확인, id
SELECT movie_id, COUNT(*)
FROM movie
GROUP BY movie_id
HAVING COUNT(*) > 1;

SELECT COUNT(DISTINCT u.user_id) D_x1,
		COUNT(DISTINCT r.user_id) D_x2,
        COUNT(u.user_id) 'all'
FROM user u
	LEFT JOIN rating r USING(user_id);

SELECT COUNT(DISTINCT u.movie_id) D_x1,
		COUNT(DISTINCT r.movie_id) D_x2,
        COUNT(u.movie_id) 'all'
FROM movie u
	LEFT OUTER JOIN rating r USING(movie_id);
    
-- 년도를 추출하여 정규화 해보기
SELECT substring_index(title, '(', 1) 'title', substr(right(title, 6), 2, 4) 'release_year'
FROM movie;

CREATE TABLE movie2 AS (
	SELECT movie_id, substring_index(title, '(', 1) 'title', movie.genres, substr(right(title, 6), 2, 4) 'release_year'
	FROM movie
);


-- movie: 백업 테이블, movie2: movie로 만들기
ALTER TABLE movie RENAME movie_backup;
ALTER TABLE movie2 RENAME movie;

SELECT * FROM movie ORDER BY release_year;

-- 년도 추출
CREATE TABLE year_info AS (
	SELECT DISTINCT DENSE_RANK() OVER(ORDER BY release_year) year_id, release_year
	FROM movie
);
ALTER TABLE year_info ADD CONSTRAINT pk_year_info1 PRIMARY KEY (year_id);

-- 년도 id로 변환
CREATE TABLE new_movie (
	SELECT movie_id, title, genres, year_id
	FROM movie
		LEFT OUTER JOIN year_info USING(release_year)
);
ALTER TABLE movie RENAME movie_backup2;
ALTER TABLE new_movie RENAME movie;

-- 자료형 변경
ALTER TABLE year_info MODIFY year_id SMALLINT;
ALTER TABLE movie MODIFY year_id SMALLINT;

-- PK, FK 설정
ALTER TABLE movie ADD CONSTRAINT pk_moive_1 PRIMARY KEY (movie_id);
ALTER TABLE movie ADD CONSTRAINT fk_movie_1 FOREIGN KEY (year_id) REFERENCES year_info(year_id);

-- 조인으로 년도 출력
SELECT title, release_year
FROM movie
	LEFT OUTER JOIN year_info USING(year_id);


-- genres_info 테이블 생성
CREATE TABLE genres_info (
	SELECT DISTINCT DENSE_RANK() OVER(ORDER BY genres) 'genres_id', genres
	FROM movie
);
ALTER TABLE genres_info ADD PRIMARY KEY (genres_id);
ALTER TABLE genres_info MODIFY genres_id INT;

CREATE TABLE new_movie (
	SELECT movie_id, title, genres_id, year_id
    FROM movie
		LEFT OUTER JOIN genres_info USING(genres)
);

ALTER TABLE movie RENAME movie_backup3;
ALTER TABLE new_movie RENAME movie;
ALTER TABLE movie ADD PRIMARY KEY (movie_id);
ALTER TABLE movie ADD FOREIGN KEY (genres_id) REFERENCES genres_info(genres_id);
ALTER TABLE movie ADD FOREIGN KEY (year_id) REFERENCES year_info(year_id);
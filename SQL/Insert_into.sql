USE mydb;

-- department
ALTER TABLE department ADD name VARCHAR(45) NOT NULL;
INSERT INTO department VALUES
	(1, 'Computer Science'),
    (2, 'Buisiness Administration'),
    (3, 'Medicine'),
    (4, 'Mechanical Engineering'),
    (5, 'Music');



###########################
-- lecturer
ALTER TABLE lecturer CHANGE department_deparment_id department_id INT;
ALTER TABLE lecturer CHANGE name name VARCHAR(45);
ALTER TABLE lecturer CHANGE name name VARCHAR(45);
INSERT INTO lecturer VALUES
	(1, 'Michael Johnson'		, 1),
    (2, 'Emily Davis'			, 1),
    (3, 'Christopher Anderson'	, 2),
    (4, 'Olivia Martinez'		, 3),
    (5, 'Daniel Wilson'			, 4),
    (6, 'Matthew Brown'			, 4),
    (7, 'Emma Rodriguez'		, 4),
    (8, 'Andrew Thomas'			, 5);

-- PK 타입 변경
ALTER TABLE lecturer CHANGE lecturer_id lecturer_id INT;




###########################
-- subject
-- FK DELETE 옵션 추가
select * from information_schema.table_constraints where table_name='subject';
ALTER TABLE subject DROP FOREIGN KEY fk_Subject_lecturer1;
ALTER TABLE subject DROP lecturer_lecturer_id;
ALTER TABLE subject ADD lecturer_id INT;

ALTER TABLE subject
	ADD FOREIGN KEY (lecturer_id) REFERENCES lecturer (lecturer_id)
        ON DELETE CASCADE;
        
ALTER TABLE subject CHANGE lecturer_lecturer_id lecturer_id INT;
INSERT INTO subject VALUES
	(1, 'Object Oriented Programming',		'ABCDEF',	1),
    (2, 'Database System & Application',	'ABCDEF',	1);

INSERT INTO subject VALUES
	(3, 'Operating System',		'PF',	2);





############# 은행 예제
use bank;

INSERT INTO bank(name) VALUES
	('KB 증권'),
    ('국민은행'),
    ('신한은행'),
    ('우리은행');

INSERT INTO branch(branch_name, bank_id) VALUES
	('서울 강남 지점', 2),
    ('서울 성동 지점', 2),
    ('서울 양천 지점', 2);

INSERT INTO client(name) VALUES
	('Michael Johnson'),
    ('Emily Davis'),
    ('Christopher Anderson');

ALTER TABLE account AUTO_INCREMENT=10000000;
ALTER TABLE account ADD amount DOUBLE;
ALTER TABLE account DROP amound;
INSERT INTO account(branch_id, client_id, kind, amount) VALUES
	(2, 3, 'loan', 10000000),
    (2, 3, 'deposit', 200000),
    (1, 1, 'loan', 20000000),
    (3, 1, 'deposit', 30000000),
    (3, 3, 'loan', 100000000);


ALTER TABLE branch CHANGE branch_name name VARCHAR(45);
ALTER TABLE client ADD address VARCHAR(100);

-- 은행에 대하여 계좌를 가지고 있는 사람들의 이름과 주소를 조회하시오.
SELECT DISTINCT client.name '고객명', client.address '고객 주소'
FROM account
	LEFT OUTER JOIN branch ON branch.id = account.branch_id
    INNER JOIN client ON client.id = account.client_id
    INNER JOIN bank ON bank.id = branch.bank_id;

-- 국민은행에서 개설한 지점명들을 조회하시오.
-- 고객별 평균 대출 금액, 최고 대출금액, 대출금액 합계를 조회하시오.



################################# 쇼핑몰
USE shopping_mall;

INSERT INTO product(product_name) VALUES
	('저칼로리 라뗴'),
    ('후렌치 파이'),
    ('초코파이'),
    ('참 붕어빵'),
    ('새우깡');

INSERT INTO customer(customer_name) VALUES
	('이수빈'),
    ('이채현');

INSERT INTO address(address, customer_id) VALUES
	('서울시 강남구 봉은사로', 1),
    ('서울시 양천구 목동동로', 1),
    ('서울시 성동구 사근동길', 1),
    ('서울시 양천구 목동동로', 2);

INSERT INTO cart VALUES
	(1, 1),
    (2, 2);

ALTER TABLE cart_has_product DROP customer_id;
INSERT INTO cart_has_product VALUES
	(1, 1),
    (3, 1),
    (4, 1),
    (1, 2),
    (2, 2);

ALTER TABLE shopping_mall.order DROP FOREIGN KEY fk_order_customer1;
ALTER TABLE shopping_mall.order DROP customer_id;

INSERT INTO shopping_mall.order(detail, paid, address_id) VALUES
	('', 1, 1),
    ('', 0, 4);




-- address customer product cart cart_has_product order


-- , , , , order_has_product, , review





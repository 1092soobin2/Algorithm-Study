-- 코드를 입력하세요 25m

-- CAR_RENTAL_COMPANY_CAR               : 대여 중 정보
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY    : 대여 기록 정보
-- CAR_RENTAL_COMPANY_DISCOUNT_PLAN     : 종류별, 기간별 할인정책 정보

-- 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중
-- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
-- 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서

-- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 
-- 대여 금액 DESC, 자동차 종류 ASC, 자동차 ID DESC

SELECT CAR_ID, CAR_TYPE, c.DAILY_FEE * 30 * (1 - p.DISCOUNT_RATE / 100) 'FEE'
FROM CAR_RENTAL_COMPANY_CAR c
    LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p USING(CAR_TYPE)
WHERE c.CAR_TYPE IN ('세단', 'SUV')
    AND p.duration_type = '30일 이상'
    AND c.DAILY_FEE * 30 * (1 - p.DISCOUNT_RATE / 100) >= 500000
    AND c.DAILY_FEE * 30 * (1 - p.DISCOUNT_RATE / 100) < 2000000
    AND c.CAR_ID NOT IN (   
            SELECT CAR_ID
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE CAR_ID NOT IN (SELECT CAR_ID
                                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                WHERE END_DATE < "2022-11-01 00:00:00"
                                    OR START_DATE >= "2022-12-01 00:00:00"))
ORDER BY c.DAILY_FEE * 30 * (1 - p.DISCOUNT_RATE / 100) DESC,
        c.CAR_TYPE ASC, c.CAR_ID DESC
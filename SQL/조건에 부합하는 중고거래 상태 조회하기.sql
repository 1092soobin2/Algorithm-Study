-- 조건에 부합하는 중고거래 상태 조회하기
-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
        CASE STATUS
            WHEN 'SALE' THEN '판매중'
            WHEN 'RESERVED' THEN '예약중'
            WHEN 'DONE' THEN '거래완료'
            ELSE NULL
        END
FROM USED_GOODS_BOARD
WHERE TO_CHAR(CREATED_DATE, 'YYYY-MM-DD') = '2022-10-05'
ORDER BY BOARD_ID DESC
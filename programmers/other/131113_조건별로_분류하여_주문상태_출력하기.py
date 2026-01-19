# 조건별로 분류하여 주문상태 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131113
# 작성자: 최영탁
# 작성일: 2026. 01. 19. 10:08:38

SELECT ORDER_ID,
PRODUCT_ID,
date_format(out_date,'%Y-%m-%d') as OUT_DATE,
case 
when out_date <= "2022-05-01" then "출고완료"
when out_date > "2022-05-01" then "출고대기"
else "출고미정" end as '출고여부'
from food_order
order by order_id asc
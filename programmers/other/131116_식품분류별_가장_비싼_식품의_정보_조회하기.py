# 식품분류별 가장 비싼 식품의 정보 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131116
# 작성자: 최영탁
# 작성일: 2026. 01. 25. 20:15:22

SELECT CATEGORY,
max(price) as MAX_PRICE,
PRODUCT_NAME
from food_product
where (category,price) in (
select category,
max(price)
from food_product
group by category) 
and category in ('과자','국','김치','식용유')
group by category
order by price desc
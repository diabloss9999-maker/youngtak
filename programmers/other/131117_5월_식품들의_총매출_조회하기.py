# 5월 식품들의 총매출 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131117
# 작성자: 최영탁
# 작성일: 2026. 01. 27. 10:09:36

select o.product_id,
p.product_name,
sum(p.price * o.amount) as total_sales
from food_order o inner join food_product p on o.product_id = p.product_id
where produce_date like '2022-05%'
group by p.product_name
order by total_sales desc,product_id



#생산일자 2022년 5월인 식품들 결과는 총매출 기준으로 내림차순 정렬 총매출 같다면 식품 id로 오름차순
# 조건에 맞는 사용자와 총 거래금액 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164668
# 작성자: 최영탁
# 작성일: 2026. 01. 20. 11:29:56

SELECT user_id,
nickname,
sum(price) as total_sales
from used_goods_board us left join used_goods_user go on us.writer_id = go.user_id  
where status = 'DONE'
group by  user_id
having total_sales >= 700000
order by total_sales
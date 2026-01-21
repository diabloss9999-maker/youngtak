# 즐겨찾기가 가장 많은 식당 정보 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131123
# 작성자: 최영탁
# 작성일: 2026. 01. 21. 09:40:50

SELECT FOOD_TYPE,
REST_ID,
REST_NAME,
FAVORITES
from REST_INFO
WHERE (FOOD_TYPE,FAVORITES) IN(
SELECT FOOD_TYPE,MAX(FAVORITES)
FROM REST_INFO
group by food_type
) 
order by FOOD_TYPE desc
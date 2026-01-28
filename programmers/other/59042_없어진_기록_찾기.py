# 없어진 기록 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59042
# 작성자: 최영탁
# 작성일: 2026. 01. 28. 09:28:34

SELECT o.animal_id,
o.name
FROM animal_ins i right join animal_outs o on i.animal_id = o.animal_id
where i.animal_id is null
order by o.animal_id
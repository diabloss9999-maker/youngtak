# 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157340
# 작성자: 최영탁
# 작성일: 2026. 02. 10. 09:42:01

SELECT CAR_ID,
CASE WHEN
MAX(START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16') THEN '대여중'
ELSE '대여 가능'
END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID 
ORDER BY CAR_ID DESC

#1.2022년 10월 16에 자동차 대여중인것은 대여중 이라고 표시 
#2.대여중이지 않은 자동차는 대여가능 AVAILABILITY 라고 컬럼 추가
#3.반납 날짜가 2022년 10월 16일인경우 대여중으로 표시  
#4. 결과는 자동차 ID를 기준으로 내림차순
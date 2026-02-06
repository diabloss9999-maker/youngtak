# 취소되지 않은 진료 예약 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132204
# 작성자: 최영탁
# 작성일: 2026. 02. 06. 20:30:43

SELECT A.APNT_NO,
P.PT_NAME,
P.PT_NO,
D.MCDP_CD,
D.DR_NAME,
A.APNT_YMD
from PATIENT P JOIN APPOINTMENT A ON P.PT_NO = A.PT_NO JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE A.APNT_YMD LIKE '2022-04-13%' AND D.MCDP_CD LIKE 'CS' AND A.APNT_CNCL_YMD IS NULL
ORDER BY A.APNT_YMD
# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 최영탁
# 작성일: 2026. 01. 21. 10:07:17


def solution(angle):
    result = 0
    if 0 < angle < 90 :
        result = 1
    elif angle == 90 :
        result = 2
    elif 90 < angle < 180 :
        result = 3
    else:
        result = 4
    return result
     
print(solution(70))

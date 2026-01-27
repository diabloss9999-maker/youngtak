# 짝수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 알고리즘: 기초
# 작성자: 최영탁
# 작성일: 2026. 01. 27. 11:12:12



def solution(num) :
    return sum(range(2,num+1,2))

print(solution(30))

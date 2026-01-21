# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 최영탁
# 작성일: 2026. 01. 21. 11:55:27

def solution(n, k):
    result = 0
    n2 =n * 12000
    k2 =k * 2000
    sbs = n//10 * 2000
    food_money = n2 + k2   # 10개먹으면 음료 1개 제공
    result = food_money - sbs
    return result

print(solution(10,3))


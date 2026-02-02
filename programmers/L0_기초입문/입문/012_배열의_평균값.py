# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 최영탁
# 작성일: 2026. 02. 02. 09:27:40

def solution(numbers):
    result = sum(numbers) / len(numbers)
    return result


print(solution([1,2,3,4,5,6,7,8,9,10]))
# 조건에 맞는 사용자 정보 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164670
# 작성자: 최영탁
# 작성일: 2026. 02. 06. 09:10:06

SELECT u.USER_ID,
u.NICKNAME,
concat(u.city," ",u.street_address1," ",u.street_address2) as "전체주소",
concat( 
    substr(u.tlno,1,3) ,'-', 
substr(u.tlno,4,4) ,'-',
substr(u.tlno,8,4)) as "전화번호"
from used_goods_board b join used_goods_user u on b.writer_id = u.user_id
group by u.user_id,u.nickname,u.street_address1,u.street_address2,u.tlno
having count(b.board_id) >= 3
order by u.user_id desc

#3건 이상 등록 사용자 아이디 닉네임 전체주소 전화번호 전체주소는 시 도로명 주소 상세주소 함께 출력
#전화번호의 경우 -을 삽입하여 출력 회원 id 내림차순
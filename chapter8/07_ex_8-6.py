'''
    작성일 : 2023년 11월 08일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 심화문제 8-3
    1. 3명의 학번, 이름, 전화 번호의 3쌍의 요소를 가지는 student_tuple라는 튜플이 존재한다
    2. 이를 이용하여 (학번:이름)의 딕셔너리를 만들어 출력하라.
    3. 이를 이용하여 학번으로 조회를 할 경우 다음과 같이 학번, 이름과 전화번호가 출력되도록 하여라.
'''
# student_tuple 튜플 생성
student_tuple = [('202095001','홍길동','010-1234-5678'), ('202095002','김철수','010-4567-7890'), ('202095100','강민서','01055686383')]

student_dict = {}
# 딕셔너리에 추가
for id_num, name, phone in student_tuple :
    student_dict[id_num] = [name, phone]

# 딕셔너리 내용 출력
for key, value in student_dict.items() :
    print(key, ":", value[0])

# 학번을 입력 받아 이름, 연락처 출력
number = input("학번을 입력하시오: ")
if number in student_dict:
    name, phone = student_dict[number]
    print(f"{number} 학생은 {name}이며, 전화번호는 {phone}입니다.")
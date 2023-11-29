'''
    작성일 : 2023년 11월 08일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 심화문제 8-3
    1. 3명의 학번, 이름, 전화 번호의 3쌍의 요소를 가지는 student_tuple라는 튜플이 존재한다
    2. 이 튜플을 수정하여 {학번 : [이름, 전화번호]}의 쌍으로 이루어진 딕셔너리를 만들어 출력하시오.
    3. 이 정보를 이용하여 학생의 학번을 입력받아 이름과 전화번호를 출력하는 학사정보 프로그램을 작성
    4. student_tuple의 마지막 항목으로 학점을 추가한다. 이 정보를 바탕으로 딕셔너리를 만들어 출력하시오.
    5. 학생의 학점 평균을 출력하시오.
'''
# student_tuple 튜플 생성
student_tuple = [('202095001','홍길동','010-1234-5678'), ('202095002','김철수','010-4567-7890'), ('202095100','강민서','01055686383')]

student_dict = {}
# 딕셔너리에 추가
for id_num, name, phone in student_tuple :
    student_dict[id_num] = [name, phone]
    
# 딕셔너리 내용 출력
for key, value in student_dict.items() :
    print(key, ":", value)

# 학번을 입력 받아 이름, 연락처 출력
number = input("학번을 입력하시오 : ")
print('이름 : ', student_dict[number][0])
print('연락처 : ', student_dict[number][1])

# student_tuple의 마지막 항목으로 학점을 추가한다.
student_dict['202095001'].append(4.5)
student_dict['202095100'].append(3.5)
student_dict['202095002'].append(2.5)

for key, value in student_dict.items() :
    print(key, ":", value)

# 학생의 평균 학점 출력
# total_grades = 0
# count = 0

# for key, value in student_dict.items():
#     if len(value) > 2:  # 학점 정보가 있는 경우
#         total_grades += value[2]
#         count += 1

# if count > 0:
#     average_grade = total_grades / count
#     print('학생들의 평균 학점은:', average_grade)
# else:
#     print('학점 정보가 없습니다.')

print("전체 학생 평균 학점")
sum=0
for key, value in student_dict.items() :
    sum = sum + value[2]

print(f"평균 : {(sum/3):.2f}")
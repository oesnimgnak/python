'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 :  선택문 if
            성적을 입력 받아 60점 이상이면 "합격입니다."를 출력
'''
# 1. 성적을 입력 받는다.  -> 입력 받아 정수로 변환 후 변수에 저장. 
score = int(input("성적을 입력하시오 : "))

# 2. 만약에 성적이 60점 이상이면 "합격"을 출력
if score > 60 : 
    print("합격입니다.")

'''
자동차의 속도를 입력받아 속도를 출력하고, (현재 속도 : 00km/h)
속도가 30km/h이면 "과속입니다. 속도를 줄이세요."를 출력하고,
속도와 상관없이 "안전 운전하세요"를 출력
'''

# 1. 속도를 입력 받는다.  -> 입력 받아 정수로 변환 후 변수에 저장. 
km = int(input("자동차의 속도를 입력하세요 :"))

# 2. 현재 속도 출력
print('현재 속도 {}km/h' .format(km))
print("현재 속도 : ", km , "km/h")
print("현재 속도 : {speed} km/h")

# 3. 만약에 속도가 30km/h 이상이면 "과속입니다. 속도를 줄이세요."을 출력
if km > 30 :
    print("과속입니다. 속도를 줄이세요.")

# 4. 속도와 상관없이 "안전 운전하세요"를 출력
print("안전 운전하세요")
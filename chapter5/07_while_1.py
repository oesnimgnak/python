'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 조건에 따라 반복하는 while 문
'''
'''
while 조건식 : => :(콜론) 반드시 사용.
        들여쓰기로 반복하면서 할일 작성.
반복문에서는 반드시 종료 조건이 있어야 한다.
While True : 무한 반복
'''

under_construcion = True # 공사중.

# True일 동안 계속 반복
while under_construcion :
    response = input("공사가 완료 되었습니까?")
    if response == "예" :
        under_construcion =False    # 공사 완료.
print("루프 탈출!!!")

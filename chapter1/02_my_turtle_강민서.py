'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 :  그림 그리기
'''

import turtle as t  # 터틀 모듈을 사용하기 위한 준비
                    # turtle 클래스 객체를 t로 생성.(별명)

t.shape('turtle')
t.speed(2)
# 선그리기
#t.forward(200) #픽셀 이동.

#삼각형 그리기
#세변의 길이, 크기가 같다 60도
#내각 기준이라 120으로 해야함
# t.forward(200) # 200픽셀 만큼 이동.
# t.left(120) # 왼쪽으로 120도 회전
# t.forward(200) # 200픽셀 만큼 이동.
# t.left(120) # 왼쪽으로 120도 회전
# t.forward(200) # 200픽셀 만큼 이동.
# t.left(120) # 왼쪽으로 120도 회전

#반복문으로 작성
for i in range(5) :
    t.forward(200) # 200픽셀 만큼 이동.
    t.left(144) # 왼쪽으로 120도 회전

#12각형

t.mainloop() #그림판 사라지지 않음.
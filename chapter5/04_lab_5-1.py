'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 터틀 그래픽으로 여러 개의 원을 그려보자
'''

import turtle as t
# 원 하나 그리기
#t.circle(100)   #반지름이 100인 원을 그린다.

for count in range(10) :
    t.circle(100)
    t.left(360/10)

t.mainloop()    #종료
#t.done()    #종료

#t.left(60)
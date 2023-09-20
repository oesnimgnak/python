'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 :  선택문 if~else
            random을 이용한 가위바위보 게임

            random 함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보
'''

import random       # random 함수 가져오기.(포함 시기키)

print("가위 바위 보 게임을 시작합니다.")
game = random.randrange(3)  # 랜덤으로 0,1,2 생성하여 변수에 저장.

# 가위 바위 보 출력
if game == 0 : 
    print("가위입니다.")
elif game == 1 :
    print("바위입니다.")
else :
    print("보입니다.")

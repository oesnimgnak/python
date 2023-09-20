'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 :  선택문 if~else
            random을 이용한 가위바위보 게임

            random 함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보

            두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''

import random       # random 함수 가져오기.(포함 시기키)

print("가위 바위 보 게임을 시작합니다.")

player1 = input("player1의 이름 :")
player2 = input("player2의 이름 :")

num1 = random.randrange(3)  # player1의 랜덤함수
num2 = random.randrange(3)  # player2의 랜덤함수

# player1의 가위 바위 보 출력
print(player1, " : ", end='')
if num1 == 0 : 
    print("가위입니다.")
if num1 == 1 :
    print("바위입니다.")
if num1 == 2:
    print("보입니다.")

print(player2, " : ", end='')
# player2의 가위 바위 보 출력
if num2 == 0 : 
    print("가위입니다.")
elif num2 == 1 :
    print("바위입니다.")
else :
    print("보입니다.")

# 누가 이겼는지 판단.
if num1 == num2:
    print("무승부입니다!")
elif (num1 == 0 and num2 == 2) or (num1 == 1 and num2 == 0) or (num1 == 2 and num2 == 1):
    # player1이 이길 조건
    print(player1 + "이(가) 이겼습니다!")
else:
    # player2가 이길 조건 (나머지 경우)
    print(player2 + "이(가) 이겼습니다!")




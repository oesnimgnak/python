'''
    작성일: 2023년 10월 11일
    작성자: 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.

    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력 받아 최대, 최소값을 찾아 돌려주는 함수.

    (함수)
            5) 두 값을 전달 받아 매개 변수를 저장.
            6) 최대값, 최소값을 찾는다.
            7) 값을 돌려준다.

    (메인)
        1. 무한반복
            1) 랜덤으로 10~99까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은지 최소 값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 max or min
            4) 입력받은 max or min과 생성된 리스트를 가지고 함수를 호출한다.
    
'''
import random

def getMinMax(mylist, method) : #두 값을 전달 받아 매개 변수를 저장.
        if method == 'max' :    # 만약 method가 max일 경우
            return max(mylist)  # 값을 돌려준다.
        elif method == 'min' :  # 만약 method가 min일 경우
            return min(mylist)  # 값을 돌려준다.

while True: # 무한 반복
    mylist = [random.randint(10, 99) for _ in range(10)]    # 랜덤으로 10~99까지 10개의 수를 리스트로 생성
    print("생성된 목록:", mylist)       # 생성된 리스트를 출력

    choice = input("max or min을 입력해 주세요 : ") # 사용자로부터 최대값을 알고 싶은지 최소 값을 알고 싶은지 묻는다.
    
    if choice in ['max', 'min']:    # 만약 max or min을 선택했을 경우 
        result = getMinMax(mylist, choice)  # 입력받은 max or min과 생성된 리스트를 가지고 함수를 호출한다.
        print(f"목록에서 {choice} 값은: {result}")  # 사용자가 선택한 max or min 값을 출력해준다
    else:  # 만약 max or min을 하지 않았을 경우 출력
        print("잘못된 선택입니다. 'max' 또는 'min'을 입력해주세요.")    
'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 단을 입력 받아 해당 단의 구구단을 출력하시오.
            130p

            문제 분석 : 입력 받는 단은 고정이다.
                        곱하는 수는 1~9까지다.
                        곱하는 수 시작값 :  1
                        곱하는 수 종료값 : 9
                        곱하는 수 증가 값 : 1             
            필요한 변수  : dan, i, result
'''

# 1. 단을 입력받아 변수에 저장.
dan = int(input("원하는 단은 : "))

# 2. 곱하는 수는 1부터이다.
i = 1
# 3. 곱하는 수를 9까지 반복하면서
while i <= 9 :
    # 1) 곱셈을 계산하여 result에 저장
    result = dan * i
    # 2) 해당 구구단을 출력
    print("%s*%s=%s" % (dan, i, result))
    # 3) 곱하는 수를 1 증가한다.
    i = i + 1
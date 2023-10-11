'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 사용자가 입력하는 숫자의 합을 계산하자.
            133p

            문제 분석 : total을 0으로 설정한다.
                        answer를 'yes'로 설정한다.
                        answer가 'yes'인 동안에 다음을 반복한다.
                            * 숫자를 입력받는다
                            * 숫자를 total에 더한다.
                            * '계속(yes, no)' 을 묻는다.
                        total의 값을 출력한다.
        
            필요한 변수  : total, answer, num
'''
# 1. total을 0으로 설정한다.
total = 0;
# 2. answer를 'yes'로 설정한다.
answer = 'yes'
# 3. answer가 'yes'인 동안에 다음을 반복한다.
while answer == 'yes' : # yes가 아니면 종료
    # 1) 숫자를 입력받는다
    num = int(input("숫자를 입력하세요 :"))
    # 2) 숫자를 total에 더한다.
    total = total + num
    # 3) '계속(yes, no)' 을 묻는다.
    answer = input("계속(yes, no) : ")
# 4. total의 값을 출력한다.
print("숫자의 합은", total)
'''
total = 0  # 합계 초기화

while True:  # 무한 루프 시작
    num = int(input("숫자를 입력하세요: "))  # 사용자로부터 숫자 입력 받음
    total += num  # 숫자를 합계에 더함
    answer = input("더 숫자를 입력하시겠습니까? (yes/no): ")  # 계속 여부 물어봄
    if answer.lower() == 'no':  # 사용자가 'no'를 입력하면
        break  # 루프를 종료함

print("숫자의 합은", total)  # 합계를 출력
'''
'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 :  선택문 if~else
            교통 카드의 종류로 '청소년', '성인' 카드가 있다고 하자.
            사용자에게 카드의 종류를 입력받아 청소년이면 '청소년입니다.'
            '성인'이면 '성인입니다.'를 출력하자.
'''
# 1. 카드의 종류를 입력 받는다.  -> 입력 받아 정수로 변환 후 변수에 저장. 
card = input("카드의 종류를 입력해주세요: ex) 청소년 or 성인")

# 2. 교통 카드의 종류로 '청소년', '성인' 카드를 판별
# 성인 또는 청소년을 입력했을 경우
if card == '성인' and '청소년' :
    if card == '성인' : #입력받은 card가 성인 일 경우 출력
        print("성인입니다.") 
    else : # 입력받은 card가 성인이 아닐 경우 출력
        print("청소년입니다.")
else :  # 성인 또는 청소년을 입력하지 않았을 경우
    print("성인 또는 청소년을 바르게 입력해주세요.") 


if card == '성인' : #입력받은 card가 성인 일 경우 출력
        print("성인입니다.") 
elif card == '청소년' : # 입력받은 card가 성인이 아닐 경우 출력
        print("청소년입니다.")
else :
     print("성인 또는 청소년을 바르게 입력해주세요.") 
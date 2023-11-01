'''
    작성일: 2023년 10월 11일
    작성자: 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 함수의 디폴드 인자.
'''

def order(num, pickle, onion) :
    print("햄버거 {}개 - 피클 {}, 양파 {}".format(num, pickle, onion))

#order(1) # 오류 발생. 인자는 1개인데 매개변수는 3개이다.

# 인자가 부족한 경우 기본값을 넣어 주는 것 => 디폴트 인자
def order2(num, pickle='기본', onion='기본') :
    print("햄버거 {}개 - 피클 {}, 양파 {}".format(num, pickle, onion))

order2(2)
order2(2, pickle='뺌', onion='기본')
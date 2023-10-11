'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 반복을 제어하는 break, continue
            137p

    test word : programming
'''

word = input("단어를 입력하세요 : ")

print(":: break1 ::")
for i in word :
    if i == 'a' or i == 'e'or i == 'i' or i == 'o' or i == 'u' :    #모음을 만나면 반복 중지
        break   # 포함된 반복이 종료(for)
    else :
        print(i, end = '')  #결과 pr

print()

print(":: break2 ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U']:    #모음을 만나면 반복 중지
        break   # 포함된 반복이 종료(for)
    else :
        print(i, end = '')  #결과 pr

print()

print(":: continue ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        continue    #반복의 시작으로 돌아간다. 아래 문장을 만날 수 없다.
    else :
        print(i, end = '')  #결과 prgrmmng

print()
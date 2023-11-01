'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : LAB 8-1  편의점 재고 관리 프로그램
'''
# 물건의 목록 정의
items = {"커피음료" : 7 , "펜" : 3, "종이컵" : 2, "우유" : 2, "콜라" : 4, "책": 5}

# 물건의 목록을 출력한다
print("물건의 목록:", ", ".join(items.keys()))

# 물건의 이름을 입력받아 재고를 출력한다.
name = input("물건의 이름을 입력하시오 : ")
if name in items:
    print('재고 :', items[name])
else:
    print('해당 물건이 목록에 없습니다.')

print('제품 목록', end=' ')
for key in items.keys() :
    print(key, end=' ')
print()
# 물건의 이름을 입력받아 재고를 출력한다.
name = input("물건의 이름을 입력하시오 : ")
print('재고 : ', items[name])

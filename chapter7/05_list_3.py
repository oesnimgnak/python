'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 리스트 객체 생성과 참조
'''
fruits1 = ['딸기','수발','바나나']

# 실제 값을 복사하는 것이 아니라 리스트이 저장 위치(주소)가 복사된다.
fruits2 = fruits1
print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)

fruits2[1] = '망고' # fruits2의 [1]번지 과일을 망고로 바꾸면...

print("fruits1 : ", fruits1)    # 모두 1번지 내용이 망고로 바뀐다.
print("fruits2 : ", fruits2)    # 주소를 참조하기 때문(같은 주소)

# 주소 확인 => 메모리 위치 정보 알아보기 id() 함수
print("fruits1의 id : ", id(fruits1))
print("fruits2의 id : ", id(fruits2))   # 두 리스트의 id정보가 같다.

'''
    리스트 내용 복제하기 list() 함수
'''
fruits2 = list(fruits1)     # 내용 복제(배정)
print(":: 내용 복제 후 1 ::")
print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)

print("fruits1의 id : ", id(fruits1))
print("fruits2의 id : ", id(fruits2))

# 내용 복제 2
fruits3 = fruits1[:]    # 처음부터 끝까지 복제하세요
print(":: 내용 복제 후 2 ::")
print("fruits1 : ", fruits1)
print("fruits3 : ", fruits3)

print("fruits1의 id : ", id(fruits1))   # id 정보가 다르다
print("fruits2의 id : ", id(fruits3))

fruits3[0] = '수박'     # 0번지 내용을 수박으로 바꾼다.
print(":: fruits3의 0번지에 수박으로내용 바꾼 후 ::")
print("fruits1 : ", fruits1)
print("fruits3 : ", fruits3)
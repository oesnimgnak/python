'''
    작성일 : 2023년 11월 08일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 집합의 연산
'''

partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print(partyA.intersection(partyB))

print("파티 A, 파티 B에 참석한 사람들 :", partyA.union(partyB))
print("파티 A, 파티 B에 중복 없이 참석한 사람 :", partyA.symmetric_difference(partyB))
print("파티 A에만 참석한 사람 :", partyA.difference(partyB))
'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 도시의 인구 자료에 대한 슬라이싱
'''
# 리스트 생성
population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]
# 이 리스트에서 서울의 인구인 두 번째 요소를 출력
print("서울 인구 : ",population[1] )
# 이 리스트에서 마지막 요소인 인천의 인구를 출력 (음수로 된 인덱스 사용)
print("인천 인구 : ", population[-1])


# 각 도시의 이름 출력
cities = population[0::2]
print("도시 lsit : ", cities)
# 각 도시의 인구 출력
pops = population[1::2]
# 합 구하기
print("인구의 합 : ", sum(pops))
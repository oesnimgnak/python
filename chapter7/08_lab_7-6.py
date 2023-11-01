'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자
'''
# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울', 9765), ('부산',3441),('인천',2954), ('광주',1510),('대전',1531)]

# 최대 인구와 최소 인구를 초기값으로 설정
#max_pop = 0
#min_pop = 99999999999999999
total_pop = 0
max_pop = city_info[0][1]   # 첫번째 항목이 기준.
min_pop = city_info[0][1]   # 첫번째 항목이 기준.

# 최대 인구를 가진 도시와 최소 인구를 가진 도시를 초기값으로 설정
#max_city = None
#min_city = None
max_city = city_info[0][1]   # 첫번째 항목이 기준.
min_city = city_info[0][1]   # 첫번째 항목이 기준.

# 리스트 city_info의 각 도시 정보를 순회
for city, pop in city_info : # for 안에 변수가 하나 이상이여도 가능
    # 전체 인구 합산
    total_pop += pop
    if pop > max_pop :  # 만약에 city[1]가 max_pop보다 크다면
        max_pop = pop  # 최대 인구 업데이트
        max_city = city     # 최대 인구를 가진 도시 업데이트
    if pop < min_pop :  # 만약에 city[1]가 min_pop보다 작다면
        min_pop = pop   # 최소 인구 업데이트
        min_city = city     # 최소 인구를 가진 도시 업데이트

# 출력
print('최대인구 : {0}, 인구 : {1}천명'.format(max_city, max_pop))
print('최소인구 : {0}, 인구 : {1}천명'.format(min_city, min_pop))
print('리스트 도시 평균 인구 : {0} 천명'.format(total_pop/len(city_info)))
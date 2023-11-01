'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 리스트에서 사용 가능한
'''
# 리스트 생성 
num_list = [1,2,3,4,5,6,7,8,9]

print("num_list 길이 : " , len(num_list))   #len() print() input()
print("num_list 최댓값 : " , max(num_list))
print("num_list 최소값 : " , min(num_list))
print("num_list 항목의 합계 : " , sum(num_list))
print("num_list 항목의 평균 : " , sum(num_list) / len(num_list))
print("num_list 항목 중 0이 아닌 원소가 있는가? : " , any(num_list))
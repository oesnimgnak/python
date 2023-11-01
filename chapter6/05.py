def print_counter():
    print('counter = ', counter)

counter = 100
print_counter()

# 출력 결과? counter = 100

def print_counter():
    counter = 200   # 지역 변수
    print('counter = ', counter)

counter = 100      # 전역 변수
print_counter()

# 출력 결과? counter = 100

def order(num, pickle, onion) :
    print("햄버거 {0}개 - 피클 {1}, 양파 {2}".format(num, pickle, onion))

order()
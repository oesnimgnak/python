'''
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터소프트웨어공학부 202095103 강민서
    설명 : 문자열
'''
# 문자열 슬라이싱
s = 'Happy Day!'
print(s[0])
print(s[6:10])  #6 ~9
print(s[:-2])   # 0~ 뒤에서 2번째 앞까지

# 문자열 분리  : split()
s = 'Welcome to Python'
print(s.split())    # 공백을 기준으로 분리

s = '2023.11.15'
print(s.split('.')) # 분리 기준은 . 이다.

s = 'Hello, World!'
print(s.split(','))

s = 'Hello, World!'
print(s.split(', '))

# 공백 제거 : strip()
s = 'Welcome, to, Python, and , bla, bla      '
print(s.strip())
print([x.strip() for x in s.split(',')])

print(list('Hello, World!'))


# 문자열 연결 : join()
print(','.join(['apple','grape','banana']))  # ,를 붙여서 연결하라.
print('-'.join('010.1234.5678'.split('.')))  # .으로 구분된 번호를 -로 고친다.

# . 을 -로 바꾸기
print('010.1234.5678'.replace('.','-'))

s = 'hello world!'
print(s)
# s에 저장된 문자열을 리스트로 문자열 분리 시켜 slist에 저장.
slist = list(s)
print(slist)
# 분리된 문자를 다시 합치기
print(''.join(slist))

# 줄바꿈과 탭이 포함된 문자열 그대로 출력
a_string = 'Today as well, \n\t Have a Happy Day.'
print(a_string)

# 문자열 자르기 word_list에 저장.
word_list = a_string.split()
print(word_list)

# 다시 합치기 : 문자열을 자르고 다시 합치면 줄바꿈과 탭이 삭제됨.
refined_string = " ".join(word_list)
print(refined_string)

# 대소문자 변환과 문자열 삭제
s = 'Helle, World!'
print(s)
print(s.lower())
print(s.upper())

# 공백 제거  strip()
s = '      Helle, World!      ' 
print(s.strip())   # 왼쪽, 오른쪽 모든 공백 제거
print(s.lstrip())
print(s.rstrip())

s = '########Helle, World!#########'
print(s)
print(s.lstrip('#'))

# 문자열 찾기
s = 'www.silla.ac.kr'
# .kr 찾기
print(s.find('.kr'))  # 12번지 출력
print(s.find('x'))      # -1 (문자열이 없다)

# . 이 몇 개 인가?
print(s.count('.'))
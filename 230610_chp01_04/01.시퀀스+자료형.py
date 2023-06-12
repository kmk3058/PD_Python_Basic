# 시퀀스 자료형

# 리스트, 튜플, 문자열, range. -> 공통점. -> 값이 연속적(sequence)으로 이어져 있다
# 값이 연손적으로 이어진 자료형(자료의 형태, 자료가 저장된 방식)을 시퀀스 자료형(sequence type)

print('파이썬', '파', '이', '썬') # 단어들이 합쳐진 것 -> 문자열

# 시퀀스 자료형이 공통 기능(특징)
## 검색 기능

## 특정한 값이 (안에) 있는지 확인
## -> 요소(element) -> 묶음 안에 존재하는지를 확인
## 값 in 시퀀스객체 : 있다
## 값 not in 시퀀스객체 : 없다
## 객체 : 특정한 자료형타입에 속하는 것들 -> 객체

shoes = ["아디다스", "나이키", "뉴발란스"]
print("shoes", shoes)
print("'아디다스' in shoes :", '아디다스' in shoes)  # in도 일종의 연산자, 있으면 True...
print("'프로스펙스' in shoes :", '프로스펙스' in shoes) # 없으면? False
print("'푸마' not in shoes :", '푸마' not in shoes, not '푸마' in shoes)  # in이 먼저 연산 처리 -> not. not in. not ~ in.

# 시퀀스 타입(자료형)의 속하는 시퀀스 객체들의 공통적인 기능.
# 시퀀스 타입 ⊃ (문자열, 리스트, 튜플, 레인지)
t = ("마제소바", "토리동", "부타동", "점보부타동", "반숙계란")
print("t :", t) # 튜플
print("'쌀국수' in t :", '쌀국수' in t)
r = range(500, 100, -25)
print("r :", list(r))
print("200 not in r :", 200 not in r)
print("(225, 200) not in r :", (225, 200) not in r)
# 문자열 검색
phone_number = "010-9999-9999"
print('"0" in phone_number', "0" in phone_number)
print('"010" in phone_number', "010" in phone_number)
print('"011" in phone_number', "011" in phone_number)
# 문자열은 연속된 부분집합의 형태로 단어들을 검색 (다른 시퀀스는 안됨)

## 연결(concatenate)
# 시퀀스 객체는 + 연산자를 이용하여서 객체를 서로 연결하여 새 객체를 만들 수 있음
# 시퀀스 객체 1 + 시퀀스 객체 2 (웬만하면 동일 타입... 그런데 강제로 붙이면 연결되기도 함...)
# a = [0, 1, 2, 3] ~ 100단위가 넘어가면?
# a = list(range(4))
a = list(range(100))
# b = [4, 5, 6, 7]
# b = list(range(4, 8))
b = list(range(40, 80, 7))
# c = [0, 1, 2, 3, 4, 5, 6, 7]
print("a + b :", a + b)
# 튜플
# a = ("a", "b", "c", "d")
a = tuple("abcd") # list("abcd")
# b = ("e", "f", "g", "h")
b = tuple("efgh") # list("efgh")
print("a + b :", a + b)

# 시퀀스 자료형 중에 연결 안되는 것 : range가 연결이 안됨.
# 잘 연결되는지 검사할 바에야 아예 막자
# print(range(10) + range(10, 20)) : unsupported operand type(s) for +: 'range' and 'range'
# range(7, 10) + range(100, 20, -1)
print(list(range(10)) + list(range(10, 20)))

# 문자열도 시퀀스도 -> 연결(+)
# greeting = "안녕하세요! "
# my_name = input("당신의 이름 : ")
# print(greeting + my_name)

# 문자열과 숫자 연결
# money = input("받고 싶은 돈 : ")
# print(type(money))
# money = int(input("받고 싶은 돈 : "))
# print(type(money))
# # print("당신의 계좌에 " + money + "만원이 입금 되었습니다!")
# # can only concatenate str (not "int") to str -> 문자열은 문자열 끼리만 연결할 수 있다 (int는 str 아님)
# print("당신의 계좌에 " + str(money) + "만원이 입금 되었습니다!")

## 반복

# * 연산자는 시퀀스 객체를 특정 횟수만큼 반복하여 시퀀스 객체를 만듭니다 (0이나 음수를 넣으면 빈 것이 나옴)
'''
- 시퀀스객체 * 정수
- 정수 * 시퀀스객체
'''
k = [0, 10, 20, 30]
print("k를 3번 반복한다", k + k + k)
print("k를 3번 반복한다", k * 3)
print("k를 0번 반복한다", k * 0) # 음수는 빈 시퀀스.
# 튜플도 유사...
k *= 3
print(k) # 산술할당연산자 됨 (연결도 똑같이 됨)
# range는 안 됨 -> list 또는 tuple로 변환해서...
# print(range(10) * 3)
print(tuple(range(10)) * 3)

hello = "안녕"
print(hello * 100) # 문자열도 *을 통해서 반복 가능

## 길이 구하기
## 시퀀스 객체의 요소(element) 개수 구하기
## len -> length의 약자. 파이썬의 len은 함수. len(....)
## 길이 -> 객체에 딸린 메소드/함수 -> length, size... (다른 언어)
## len(시퀀스객체)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] # 피보나치 수열
print(len(a))
b = ("a", 1, True, 1.5) # 4개
print(len(b)) # 원소는 각각 1개로 무조건 카운팅

# range : range에 len 함수를 사용하면 숫자가 생성되는 개수를 구합니다
print(len(range(75, 20, -4)))

# 문자열 : len -> 포함된 '문자' 개개의 갯수
s = '오늘은 "점심"으로 \'마제소바\'를 먹을 것이다' # 작은따옴표, 큰따옴표는 세지 X. (감싼). 공백(스페이스)는 1길이.
# 파이썬은 숫자, 영어, 한글의 길이 구분 X -> 똑같이 길이 1씩.
print(s)
print(len(s)) # 25?

# 인덱스
# 시퀀스 객체 -> 여러 개의 데이터들이 묶여있는 형태. -> 순서가 정해져있음 (요소들간의)
# -> 시퀀스 객체 내에 요소들의 위치 = 인덱스 (index)
# 시퀀스_객체[인덱스번호] -> 시퀀스 개체에 [](대괄호)를 붙이고 [] 안에 각 요소의 인덱스(번호)를 지정하면 해당 요소에 접근(호출)
a = [100, 200, 300, 400, 500]
print(a[1]) # 200
# 컴퓨터 프로그래밍에서는 모든 숫자 세기를 0부터 시작합니다.
print(a[0]) # 100 -> 0이 순서 세기의 첫 번째.
# 인덱스를 통해서 내가 원하는 값(특정한 순서에 있는 값)을 불러오는 것 : 인덱싱(indexing)
print(a[2], a[4])
print("len(a)", len(a))

# print(a[5]) # IndexError: list index out of range -> index를 생각할 때 len보다 1 작은 것까지.

b = (5, 13, 21, 34, 55)
print("b[0]", b[0])
print("b[3]", b[3])

# range
r = range(2, 5) # 2, 3, 4
print("r[2]", r[2])

# 문자열 (string) -> 요소가 문자 한 개씩 끊긴 개념 -> 인덱스로 접근 -> 문자.
s = "오늘의 날씨를 알려드리겠습니다" # 8번째 요소를 출력한다
print(s[8]) # 인덱스상 8 -> 9번째. ("알"
print(s[7]) # 인덱스 7. (" ")

print(s) # 인덱스 없이 호출 -> 그 자체 (전체 값)
# 해당 객체 전체

# 음수 인덱스
# - 인덱스 => 0 이상의 정수.
# -> 음수 인덱스 (정수인데 -N)
a = [38, 21, 3, 62, 19]
print("a[-1]", a[-1]) # 맨 뒤에 있는 값
print("a[-3]", a[-3])
# -n 이라는 인덱스를 주면, 뒤에서부터 세서 위치
# print("a[-6]", a[-6])
print(a[len(a)-1]) # len보다 음수 인덱스가 커지면 에러
# 튜플, 레인지...
s = "마제소바"
print(s[-1])
sn = "991111-1234567"
print(sn[-7])

# 인덱스를 통해 요소에 값 할당(대입) == 수정
print(a)
print(a[0]) # 시퀀스객체[인덱스] <- 그 값을 불러오는 기능 / 그 값의 위치를 확인.

b = [0] * 5
print("b", b)
b[0] = 137
b[1] = 44
b[2] = 9
b[3] = 13
b[4] = 88
# b[5] = 11231231 # IndexError: list assignment index out of range
print("b", b)

# 인덱스를 통해서 요소의 값을 재할당 -> 리스트.
# 튜플, range, 문자열은 재할당 X - read-only
t = (1, 2, 3)
# t[1] = 5 # 2 -> 5
# print(t)

r = range(10)
# r[0] = 9 # TypeError: 'range' object does not support item assignment

s = "문자열"
# s[0] = "곰" # 'str' object does not support item assignment

# 요소 삭제 (요소 수정과 삭제 모두 리스트 전용 기능)

a = ["바나나", "키위", "콩"] # 0, 1, 2 -> '2'
print(a)
del a[2]
print(a)
# 튜플, 레인지, 문자열 -> 안먹힘.
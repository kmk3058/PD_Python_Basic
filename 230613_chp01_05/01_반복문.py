# for ... in : 반복문을 위한 문법
# # for 변수명 in range(횟수) : # range 안에(in) 있는 요소들을
#
# # '변수명'으로 하나씩 꺼내와서 들여쓰기 안에 사용해주겠다
# # 반복할 코드 (들여쓰기)
#
#
# # 10번 반복하는 코드
# for i in range(10) : # range(N)번 반복하는 코드 # for (i = 0; i < 10; i++) {...} 다른 언어에서의 for.
#      # 0 ~ 9
#     print("자니?", i) # range에서 요소들을 하나씩 꺼내서 i에 넣고 사용
#
# '''
# 반복문의 변수 i : 루프 인덱스 -> loop index -> i
# '''
#
# # for in + range 반복
# # range의 특성? : range(끝점), range(시작점, 끝점), range(시작점, 끝점, 증가폭)
# # for 변수명(i) in range(시작점, 끝점) :
# # 반복할 코드
#
# # 5부터 10까지 합해주는 코드
# a = 0 # 모든 합을 기록할 변수 (반복문 밖에 둠)
# for i in range(5, 11):
#     # print(i) # 5 ~ 10 <- 순서대로 대입
#     # i는 순회할 때마다 새로운 값으로 변화
#     # a = a + i
#     # a += i
#     # i가 홀수 일때만 더한다면?
#     # if i % 2 == 1 :
#     if i % 2 :
#         a += i
#         print(i, a)
# print(i, a)
#
#
# # 증가폭
# # for 변수명 in range(시작, 끝, 증가폭):
# for i in range(1, 10, 2):
#     print(i)
# # 뒤집기
# for i in range(10, 1, -2): # rang(1, 10, -1) -> 빈 range. -> 음수 증가폭 -> 시작점 >
#     print(i)
#
# # reversed -> 시퀀스형태의 자료형을 뒤집어주는 기능
# '''
# - for 변수 in reversed(range(횟수))
# - for 변수 in reversed(range(시작, 끝))
# - for 변수 in reversed(range(시작, 끝, 증가폭))
# '''
#
# # 뒤집기 방법 1
# for i in range(9, -1, -1):
#     print(i, end=" ")
#
# # 뒤집기 방법 2
# for i in reversed(range(10)):
#     print(i, end=" ")
#
# # 뒤집기 방법 3
# for i in range(10)[::-1]:
#     print(i, end=" ")
#
# # 뒤집기 부수적인 방법
#
# for i in range(10):
#     print(9 - i, end=" ")

# 시퀀스 객체로 반복하기 (리스트, 튜플, 문자열...)

a = ["아무1", "아무2", "아무3"]

for v in a : # value - > v.
    print(v, end = '\n')

fruits = ["사과", "배", "포도"]

for fruit in fruits : # 리스트, 튜플 -> 시퀀스(복수형) => for 를 통해서 반복 호출하는 변수명 -> 단수.
    print('-' * 10)
    print(fruit, end = '\n')

text = "작은 것들을 위한 시"

for c in text: # c : character
    print(c)

for c in reversed(text): # c : character
    print(c)

for c in text[::-1]: # c : character
    print(c)

# 인덱스를 사용한 조회
for i in range(len(text)):
    # range(len(text)) -> text의 정수 인덱스 목록
    # -> text[i] : 반복문으로 조회를 하면... -> 요소 하나하나를 검색.
    print(i, text[i]) # text가 가지고 있는 인덱스의 목록.

for i in range(len(text)): # 시퀀스의 길이를 바탕으로 인덱스 목록을 만들어서
    print(text[i]) # 해당 인덱스로 호출할 수 있는 값들을 출력한 코드
for t in text: # 시퀀스 안에 있는 요소들을 하나씩 호출해서
    print(t) # 출력한 코드

for i in range(len(text))[::-1]: # 시퀀스의 길이를 바탕으로 인덱스 목록을 만들어서
    print(text[i]) # 해당 인덱스로 호출할 수 있는 값들을 출력한 코드
for t in text[::-1]: # 시퀀스 안에 있는 요소들을 하나씩 호출해서
    print(t) # 출력한 코드

# enumerate - 인덱스, 값 -> 튜플쌍을 만들어주는 함수
for i in enumerate(fruits):
    print(i) # (인덱스, 요소의 값)
for i in enumerate(fruits): # for -> in을 통해서 시퀀스 객체에서 뽑아낸 요소를 => 변수에 '할당'
    a, b = i  # 튜플. -> 왼쪽에 자리수를 맞춰서 변수를 둬서 해체 => 튜플 언팩킹
    print("a", a, "b", b) # (인덱스, 요소의 값)
print("for a, b in enumerate(fruits):")
for a, b in enumerate(fruits):
    print("a", a, "b", b)  # (인덱스, 요소의 값)
    # for에서부터 언팩킹으로 할당이 가능.

for i, v in enumerate(fruits):
    print("i", i, "v", v)  # (인덱스, 요소의 값)
    # for에서부터 언팩킹으로 할당이 가능.
# 조건문
# 조건문 -> 특정 조건을 만족시켰을 때 실행시키는 문법
# -> 특정 조건을 만족시킨다? -> True가 나오면.(계산, 실행 => 그 결과가 True다 => 만족시켰다)
# -> bool, 비교연산자, 논리연산자...

'''
# if 조건문. ~ 3.7? 3.9? => if조건문.
if 조건식:
    조건을 만족시켰을 때 실행할 코드
'''

# my_age = int(input("당신의 나이는? : "))
# if my_age > 20: # my_age > 20 : 비교연산자 (True)
#     # 들여쓰기 된 내부의 코드를 실행 (if와 :(콜론) 사이의 특정한 조건을 만족시키면...)
#     print("술과 담배가 가능합니다!")

# if my_age > 20:
# print("술과 담배가 가능합니다!") # IndentationError: expected an indented block after 'if' statement on line 17


# 중첩 if문
# if my_age < 20:
#     print("학생입니다!")
#     if my_age >= 17: # 새로운 if문을 열면 -> 새로운 들여쓰기
#         print("고등학생입니다!")
#     if my_age < 17 and my_age >= 14: # 논리연산자를 통해서
#         print("중학생입니다!")

# else
'''
if A: # 이것을 만족(True <-> False)시킬 때 <- 이 전화는 광고전화인가?
    ... (A - 나이가 성인인가?)
    끊고, 차단한다
else:
    ...? (성인이 아니라면?)
    받고 이야기를 나눈다
'''
'''
if <조건식>:
    코드1
else: # 단독으로 올 수 없음?
    코드2
'''

# if my_age > 20:
#     print("복권을 구입할 수 있습니다")
# else:
#     print("복권을 구입할 수 없습니다") # 들여쓰기 주의!!!

# 조건문에 다양한 자료형 넣어보기

# 불(bool) -> 숫자는 0이 아니면 -> True. (0만 False) - 정수, 실수.
# 글자는 ""가 아니면 -> True. -> len(시퀀스) == 0 -> False, len(시퀀스) != 0 -> True
print("bool(1)", bool(1))
print("bool(0)", bool(0))
print("bool(-1)", bool(-1))
print("bool('False')", bool('False')) # 시퀀스 -> len -> 빈 문자열 -> len(문자열) == 0
print("bool('')", bool('')) # False => len(문자열) != 0
print("bool([])", bool([]))
print("bool([False])", bool([False]))

if 1: # bool로 알아서 바꿔줌 -> bool(...) 씌운 효과
# if True:
    print("??????")
if 0:
    print("000000")
if '':
    print("빈 문자열")
if ' ':
    print("공백 문자열")
if []:
    print("빈 리스트")
if [False]:
    print("길이가 있는 리스트")


# elif

# if : 단순히 조건을 만족시키는 지 여부
# if ... else : 만족할 때 / 만족하지 않을 때를 구분해서 배치.
# 만약에 조건이 여러개면?
menu = input("마시고 싶은 음료 : (아메리카노, 제로콜라, 물) ")
# # ---
# if menu == "아메리카노": # 각각 별도의 if문
#     print("아메리카노 나왔습니다")
# # ---
# if menu == "제로콜라": # 각각 별도의 if문
#     print("제로콜라 나왔습니다")
# # ---
# if menu == "물": # 각각 별도의 if문
#     print("물 나왔습니다")
# else:
#     print("주문할 수 없는 음료입니다")
# # ---
# ---
if menu == "아메리카노": # 각각 별도의 if문
    print("아메리카노 나왔습니다")
elif menu == "제로콜라": # 각각 별도의 if문
    print("제로콜라 나왔습니다")
elif menu == "물": # 각각 별도의 if문
    print("물 나왔습니다") # 실행문
else:
    print("주문할 수 없는 음료입니다")
# ---
# elif는 단독으로 사용할 수 있다? 없다 => 맨 처음 if문이 있어야 elif가 붙을 수 있기 때문에.
# elif는 추가적으로 들여쓰기할 필요가 있다? => 없다. 기본적인 코드블록의 들여쓰기만 하면 된다.
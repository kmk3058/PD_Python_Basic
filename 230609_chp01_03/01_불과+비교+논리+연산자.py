# 불(Bool)과 비교, 논리 연산자
## 불과 비교 연산자 사용하기
'''
* 프로그래밍 -> 참, 거짓 판단 -> 참(True) : 어떠한 조건이나 수식을 만족시키는가? / 거짓(False) : 만족시키지 못한다
* 불(Bool) 혹은 불리언(Boolean) : 참 과 거짓으로 구성된 자료형. <- 조건이나 수식들이 존재하게 됨.
* 두 값의 관계를 판단하는 비교 연산자 / 두 값의 논리적 관계를 판단하는 논리 연산자
* if, while.. 구문을 작성.
'''
print(True, False)  # 다른 언어들은 대개 true,false
print(int(True), int(False))  # 1, 0

# 비교 연산자 - 판단 결과
## 등호(같다, 다르다)와 부등호(크다, 작다). -> 비교하는 식이 맞으면 True 아니면 False
print('10 > 5', '10이 5보다 크다, 10은 5를 초과한다', 10 > 5)  # 초과
print('10 < 5', '10이 5보다 작다, 10은 5의 미만이다', 10 < 5)  # 미만

## 숫자가 같은지 다른지 비교
'''
* 일반적 수학에서는 =(등호)로 쓰는데, 파이썬 등 프로그래밍에서는 ==을 등호(동등 연산자, equal)로 쓴다
* =은 파이썬 뭐에요? -> 대입 연산자 -> 특정한 변수에 값을 할당해주는 연산자
* 다를 때 !=(not equal)을 사용
'''
print("1 == 1 :", 1 == 1)
print("2 == 1 :", 2 == 1)
print("1 != 1 :", 1 != 1)

## 문자열 동등 여부 비교 (only)
print("'python' == 'python'", "python" == "python")  # java == X. equals -> 주소값을 비교하니까.
print("'Python' == 'python'", "Python" == "python")  # 대소문자가 다르면 다른 문자!!!!
print("'Python' != 'python'", "Python" != "python")  # 대소문자가 다르면 다른 문자!!!!

# 숫자 비교 : 부등호
print("10 > 20", 10 > 20)  # 초과 (왼쪽 값 기준으로 생각)
print("10 < 20", 10 < 20)  # 미만
print("10 >= 20", 10 >= 20)  # 이상
print("10 <= 20", 10 <= 20)  # 이하

# 객체가 같은지 다른지 비교하기
'''
* is, is not -> 연산자. ==, !=. 왜 is(~이다), is not(~는 ~가 아니다)?
* ==, != : 값 자체를 비교한다
* is, is not -> 객체를 비교한다, 객체 주소를 비교한다(타입) 
'''
# 정수 1과 실수 1.0은 까다롭게 생각하면 다른 애들.
print("1 == 1.0 :", 1 == 1.0)  # 1이라고 하는 '값'은 같아요 (상호 변환이 가능) - 같은 숫자형일 경우에는 같다고 침
print("'1' == 1 :", '1' == 1)  # 문자열과 숫자의 비교이므로 성립 안함
# a = 1 is 1.0 # 비교 연산의 결과값을 변수에 담을 수 있음
# print("1 is 1.0 :", a)
# b = (1 is not 1.0)
# print("1 is not 1.0 :")
# print(b)

# 논리 연산자 사용하기
## 논리 연산자는 and, or, not. (연산자가 꼭 특수문자나 기호일 필요는 없음)
'''
내가 알고 있던 and는 &? &&? 내가 알고 있던 or은 |? ||? 내가 알고 있는 not은 !인데??
'''
## 그리고(and) 연산 (&)
have_car = True
have_money = True
can_drive = have_car and have_money
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
print()
have_car = False
have_money = True
can_drive = have_car and have_money # 하나라도 False면은 다 False 틀린다
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
print()
have_car = True
have_money = False
can_drive = have_car and have_money # 하나라도 False면은 다 False / 틀린다
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
print()
have_car = False
have_money = False
can_drive = have_car and have_money # 하나라도 False면은 다 False / 틀린다
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)

print("have_car & have_money", have_car & have_money)
# print("have_car && have_money", have_car && have_money) # 문법 오류

# or (또는) / a or b : or로 묶인 것들 중에 하나가 True라면 결과값 True (a | b)
hungry = True
study = True
eat_lunch = hungry or study
print("hungry?", hungry)
print("study?", study)
print("eat_lunch?", eat_lunch)
print()
hungry = False
study = True
eat_lunch = hungry or study
print("hungry?", hungry)
print("study?", study)
print("eat_lunch?", eat_lunch)
print()
hungry = True
study = False
eat_lunch = hungry or study
print("hungry?", hungry) # <-> 배부르다
print("study?", study)
print("eat_lunch?", eat_lunch)
print()
hungry = False
study = False
eat_lunch = hungry or study # 여기서 계산이 끝남
print("hungry?", hungry)
print("study?", study)
print("eat_lunch?", eat_lunch) # 하나라도 True라면 결과가 True -> OR
print()
print("hungry | study", hungry | study)

# not (논리값 -> bool) True -> False / False -> True
sleepy = True
print("sleepy", sleepy)
print("not sleepy", not sleepy) # 안 졸리다, 깨어있다~
boring = False
print("boring", boring)
print("not boring", not boring)
# print("not boring", !boring) -> ! 연산자 없음...

# and, or, not -> not (1), and (2), or (3) <- 우선순위 외우면 좋음.

print("not True and False or not False", not True and False or not False)
print("(not True) and False or (not False)", False and False or True)
print("((not True) and False) or (not False)", False or True)
# 논리 연산도 ()를 통해서 강제로 우선순위를 정해줄 수 있음.
# 논리 연산을 복잡하게 하는 것에 익숙하지 않다 / 못하겠다
# 1. 괄호 사용하기 2. 변수로 끊어서 연산하기

# 논리 연산자 + 비교 연산자 (무조건 비교 연산자가 먼저임)
# 비교 연산자를 통해서 값을 비교하고 이것을 통해 True 또는 False 결과값(Bool 값이 나옴)
# 그 후에 논리 연산자가 그것을 받아서 처리함
# 산술 -> 비교 -> 논리 연산자 순. (그래도 괄호와 변수로 표현된 건 먼저 처리가 된 상태임)
print("10 == 10 and 10 != 5 :", 10 == 10 and 10 != 5)
print("(10 == 10) and (10 != 5) :", True and True)  # True.
print("10 > 5 or 10 < 3", 10 > 5 or 10 < 3) # True
print("5 + 5 > 8 and 3 - 2 < 0", 5 + 5 > 8 and 3 - 2 < 0)
print("(5 + 5) > 8 and (3 - 2) < 0", 5 + 5 > 8 and 3 - 2 < 0)
print("not 10 > 5", not 10 > 5)
print("not 7 + 3 > 5", not 7 + 3 > 5)

# 정수, 실수, 문자열을 불(참,거짓)으로 만들기 / 판별
'''
정수, 실수, 문자열 -> 불(bool) => bool(1)
'''
print("bool(1)", bool(1))
print("bool(0)", bool(0))
print("bool(-1)", bool(-1)) # 정수, 실수나 => 숫자에서는 True/False 기준은 0이면 False. 0이 아니면 True
print("bool(0.1)", bool(0.1))
# number -> bool ???? number != 0

# 문자열
print("bool('아무거나')", bool("아무거나")) # True
print("bool('abadfafa')", bool("abadfafa")) # True
print("bool('')", bool("")) # False => 큰따옴표 혹은 작은따옴표로 감싸진 것만 있을 때
# string -> bool ???? len(string) > 0 # length(길이)
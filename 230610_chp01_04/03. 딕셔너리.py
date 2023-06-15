# 딕셔너리 (Dictionary)
warrior = [500, 100, 10.5, 27]  # 인덱스? -> 특정한 값에 대해서 설명? X -> 그저 위치
print(warrior)
# 해시맵, 맵, 오브젝트, 딕셔너리 ... -> 값들 묶음에서 -> 그 값이 어떠한 특징 혹은 속성인지에 대한 설명.
warrior = {
    "hp": 500,
    "mp": 100,
    "atk": 10.5,
    "def": 27,
} # 사전을 찾듯이 어떠한 키(찾는 단어) -> 대응되는 값.
print(warrior)

# 딕셔너리 만들기
'''
* 딕셔너리 = {키1: 값1, 키2: 값2...} # 키는 겹치면 X. 수정할 수 없는 값. 각 키와 값 쌍 콤마(,)로 구분 
'''
kim = {
    "name": "춘식", # key:value,
    "age": 25, # key:value,
    "marry": False, # ...
}
# 키에는 값을 하나만 지정할 수 있음 -. 키-값 쌍(key-value pair)
lee = {
    "name": "봉식",
    "name": "봉구", # 같은 딕셔너리 안에서 마지막으로 key에 대입된 값이 최종 값.
}
print(lee)

print(lee['name']) # 각각의 키가 value를 불러낼 수 있는 열쇠.

# 딕셔너리 키의 자료형
# key -> 문자열. 이 외에도 '수정되지 않는 값'은 모두 key로 쓸 수 있음.
# (1) 리스트 (2) 딕셔너리 -> 나머지 웬만한 기본적인 자료형들은 key로 쓸 수 있음
# bool, int, float, tuple, range, 문자열... -> key로 쓸 수 있음.
# 굳이 리스트를 key로 쓰고 싶다 tuple로 감싸서 튜플화시켜서 쓰면 됨.

# 딕셔너리 키에 접근 및 할당
# 리스트의 경우 -> 리스트[인덱스] -> 값. 리스트[인덱스] = 새로운 값 => 할당.
# 리스트-인덱스, 딕셔너리-키. => 호출 시 리스트의 원소를 인덱스로 호출 하는 것 처럼, 딕셔너리의 값은 키로 호출할 수 있다 + 할당.
park = {
    "address": "여의도"
}
print("park[\"address\"]", park["address"])
park['address'] = "일산" # 할당 연산자 -> 새로운 값을 대입(할당) -> 변수, 리스트[인덱스] = 새로운 값...
print("park[\"address\"]", park["address"])
# 키를 지정하지 않고 그냥 dictionary를 호출하면?
print(park) # key-value 쌍이 들어있는 딕셔너리 자체

# 빈 딕셔너리 만들기
# 빈 리스트 -> list() 혹은 [] -> 변수.
x = {} # {}를 넣어서 혹은
x = dict() # dict()를 통해서 만들어주게 됨
print(x)

# print(park['car']) # 없는 키를 호출하게 되면? # KeyError: 'car' -> 없어서 에러가 남
# key라고 하는 거는, 딕셔너리를 만들 때 넣어주거나, 아니면 할당할 때 쉽게 넣고 할 수 있는데...
# 아예 할당되지 않은 키는 조회시 에러가 발생
x['car'] = '모닝' # 할당 -> 문제 없음 (<-> 리스트는 없는 인덱스에는 추가하면서 생성 X)s
print(x)


# 딕셔너리에 키가 있는지 확인
# 시퀀스 -> '안'에 특정한 요소/값이 있는지 확인하려면? in.
# 딕셔너리도 같은 걸 쓰는데... 키만 확인.
data = {
    "kim": 200,
    "park": 300,
}
print(data)
print('"kim" in data', "kim" in data) # 특정한 Key가 존재하는지
'''
* 키 in 딕셔너리
'''
print('"lee" in data', "lee" in data) # 특정한 Key가 존재하는지
print('not "lee" in data', not "lee" in data) # 특정한 Key가 존재하는지 -> not을 통해서 뒤집기
print('"lee" not in data', "lee" not in data) # 특정한 Key가 존재하지 않는지

d = {
    "scores": [1, 2 ,3], # 키-값 : 1씩
    "money": 100 # 키-값 : 1씩
}
d['hello'] = True
print(d)
print(len(d)) # 키의 갯수를 세어줌 근데 키-값은 1:1 대응이니까, 값의 갯수를 세주는 겸.
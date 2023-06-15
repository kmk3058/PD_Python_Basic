l = list(range(0, 10, 2))
print(l)
l.append(100) # 맨 끝에 요소를 추가 -> 1개의 요소
print(l) # l += [100]
l.extend([200, 1000]) # 새롭게 추가하려는 리스트를 '한 개씩' 반복적으로 끝에 추가
print(l) # l += [200, 1000]
l.insert(0, 500) # 인덱스, 값
print(l)
l.insert(3, 500)
print(l)

print(f"l : {l}")  # f-string => {} 특수한 기능 => 변수나 특정한 값을 문자화.
l.pop()  # 맨 끝의 값 -> 삭제 -> 그 값을 반환.
print(f"l : {l}")
print(l.pop())  # del l[-1] 과는 다름.
print(f"l : {l}")
last = l.pop() # 값이 외부로 튀어나왔다
print(f"l : {l}, last : {last}")




"""그러면 원하는 인덱스의 요소를 삭제할 수는 없을까요? 이때는 pop에 인덱스를 지정하면 됩니다."""
print(f"l.pop(2) : {l.pop(2)}")
print(f"l : {l}, l[2] : {l[2]}")
# pop(인덱스)는 해당 인덱스의 요소를 삭제한 뒤 삭제한 요소를 반환합니다.

print(f"l : {l}")
# l.remove(100)  # 별도로 인덱스를 주지 않아도...
print(f"l : {l}")
# 같은 값이 2개 이상 있을 때?
l.remove(500)  # 인덱스가 큰 것을 먼저 지운다
print(f"l : {l}")
# 2개 이상의 것을 모두 지우고 싶으면?
# while -> value in ... -> 계속 반복.
# for -> 전수 조사 -> 인덱스를 기록해놨다가 -> 삭제.

"""### 리스트에서 특정 값의 인덱스 구하기"""

# index(값)은 리스트에서 특정 값의 인덱스를 구합니다.
# 이때 같은 값이 여러 개일 경우 처음 찾은 인덱스를 구합니다(가장 작은 인덱스).
print(f"l.index(6) : {l.index(6)}")
print(f"l[3] : {l[3]}")
print(f"l[l.index(6)] : {l[l.index(6)]}")

"""### 특정 값의 개수 구하기"""

# count(값)은 리스트에서 특정 값의 개수를 구합니다.
l2 = [10, 100, 10, 200, 30, 10]
print(f"l2.count(10) : {l2.count(10)}")
import random
r = random.choices(range(5), k=100)
print(r)
print(f"r.count(4) : {r.count(4)}")

print(f"l : {l}")
print(f"l[::-1] : {l[::-1]}")
print(f"reversed(l) : {list(reversed(l))}")  # 얕은 복사를 통해서 새로운 사본을 만드는 방법
# 원본 영향을 바로?
print(l.reverse())  # 반환 값
print(f"l : {l}")

print(f"r : {r}")
print(f"sorted(r) : {sorted(r)}")  # 안 끼치는 거다 => r = sorted(r)
print(f"r : {r}")
print(r.sort())  # 원본에 영향을 미치는데... 그 대신? 별도의 결과값은 없다.
print(f"r : {r}")

print(f"r : {r}")
print(f"min(r) : {min(r)}")
print(f"max(r) : {max(r)}")
print(f"sum(r) : {sum(r)}")
print(f"len(r) : {len(r)}")
print(f"(산술)평균 : sum(r) / len(r) : {sum(r) / len(r)}")

s = "아메리카노 2샷추가(ice)"
s.replace("2", "3")  # 메소드를 사용하면 -> 새로운 사본. 복사본.
print(f"s : {s}")
print(f"s.replace(\"2\", \"3\") : {s.replace('2', '3')}")
s2 = s.replace("2", "3")
print(f"s2 : {s2}")

"""만약 바뀐 결과를 유지하고 싶다면 문자열이 저장된 변수에 replace를 사용한 뒤 다시 변수에 할당해주면 됩니다."""



"""### 문자열 분리하기

이제 문자열을 분리하는 방법입니다.

split()은 공백을 기준으로 문자열을 분리하여 리스트로 만듭니다. 지금까지 input으로 문자열을 입력받은 뒤 리스트로 만든 메서드가 바로 이 split입니다.
"""

s = "5시 53분의 하늘에서 발견한 너와 나"
s2 = "9와 4분의 3 승강장에서 너를 기다려 (Run Away)"
print(s.split())
print(s2.split("승강장에서"))

"""split('기준문자열')과 같이 기준 문자열을 지정하면 기준 문자열로 문자열을 분리합니다. 즉, 문자열에서 각 단어가 ,(콤마)와 공백으로 구분되어 있을 때 ', '으로 문자열을 분리하면 단어만 리스트로 만듭니다."""



"""### 구분자 문자열과 문자열 리스트 연결하기

문자열을 분리하여 리스트로 만들었으니 다시 연결하는 방법도 있겠죠?

join(리스트)는 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만듭니다. 
다음은 공백 ' '에 join을 사용하여 각 문자열 사이에 공백이 들어가도록 만듭니다.
"""

r = [str(i) for i in range(10)]
print(r)
print(f'"".join(r): {"".join(r)}')
print(f'",".join(r): {",".join(r)}')

print(f"s2 : {s2}")
print(f"s2.find('너') : {s2.find('너')}")
print(f"s2.find('나') : {s2.find('나')}")
print(f"s2.find('승강장') : {s2.find('승강장')}")


"""### 문자열 개수 세기

count('문자열')은 현재 문자열에서 특정 문자열이 몇 번 나오는지 알아냅니다.
"""
s3 = "짜리짜리짜리짜리몽땅"
print("짜리짜리짜리짜리몽땅")
print("짜리짜리짜리짜리몽땅".count("짜리"))

d = {"name" : "투바투", "company" : "하이브"}
print(f"d : {d}")
d['name'] = "TXT"
print(f"d : {d}")
d.update(company="HIVE")
print(f"d : {d}")
d.update(name="투모로우바이투게더", company="HYBE")
print(f"d : {d}")

name = d.pop("name")
print(name)
print(d)

print(d.get("name")) # 없으면 None으로 반환
print(d.get("name", "UNTITLED")) # 기본값을 지정하면 (해당 키가 없을 때) 해당 값을 표현


d = {"name" : "투바투", "company" : "하이브"}
# keys()는 키를 모두 가져옵니다.
print(f"d.keys() : {d.keys()}")
# values()는 값을 모두 가져옵니다.
print(f"d.values() : {d.values()}")

print(f"d.items() : {d.items()}")

# 반복문

for i in d.items():
    print(f"i : {i}")

for key,value in d.items():
    print(f"key : {key}, value : {value}")

for index, (key, value) in enumerate(d.items()):
    print(f"index : {index}, key : {key}, value : {value} ")

d1 = {}
d2 = {"d1" : d1}
d2['d1']['number'] = 1
print(f"d1 : {d1}")
print(f"d2 : {d2}")

country = {}
country['korea'] = {"money" : 1000}
country['japan'] = {"money" : 2000}
print(country)
print(country['korea']['money'])
print(country['japan']['money'])

# 딕셔너리의 할당, 얕은복사, 깊은복사
# 딕셔너리 컴프리헨션
# 자주 활용되는 기능은 아님.


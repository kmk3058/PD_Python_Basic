# 문자열
# "" 혹은 ''로 묶여진 글자들의 묶음 (0자 이상의 글자들의 집합)

text = "hello playdata!"
print(text) # 출력

# 한글 문자열
korean = "먹어도 먹어도 배고프다"
print(korean)

# 문자열 만들기 : " "(큰따옴표)로 묶기
double_quotation = "my name is python"
print(double_quotation)  # ctrl + space (자동완성 or 기능 추천)

# ' '(작은따옴표)로 묶기
single_quotation = 'your name is python'
print(single_quotation)

#  '''...'''로 묶거나 """..."""로 묶기
t1 = '''hello guys'''
t2 = """good lunch"""
print(t1, t2)

# 여러 줄로 된 문자열 사용
m1 = '''green red
red green
hello buy'''
print(m1)
print("green red\nred green\nhello buy")
m2 = """chicken pork
beef salad
desert""" # 큰따옴표도 똑같은 역할
print(m2)
# 여러 줄로 된 문자열은 큰따옴표나 작은따옴표 3개로 시작해서 3개로 마쳐주면 된다.
# 변수만 지우면? -> 무슨 모양?
"""chicken pork
beef salad
desert""" # 여러줄 주석 <- 실제로는 여러 줄 문자열인데... => 이걸 저장하는 변수나 실행하는 구문 없으므로 주석처럼 쓸 수 있는 것

# 큰따옴표로 묶었을 때, 중간에 큰 따옴표가 들어가면?
# text = "안녕" 안녕" # 따옴표들은 직전 따옴표와 직후 따옴표 간의 문자열을 묶는다고 인식
# text = '이름하여 '파이썬'!' # 2개의 문자열이 있다고 인식
text = "이름하여 '파이썬!'" # 전체적으로 큰따옴표로 묶였기 때문에, 안에 있는 작은 따옴표는 문자열 그 자체로 인식
print(text)
text2 = '큰따옴표("")'
print(text2)
text = "\"" # \" <- 큰따옴표이긴 큰따옴표인데... 큰따옴표 자체가 가지고 있는 문자열을 감싸주는 특수 기능 제거 (이스케이프)
print(text)
# 여러 줄 문자열에서는 작은따옴표나 큰 따옴표가 섞여서 들어가도 상관 없어요
t1 = '''
작은따옴표(')
큰따옴표(")
'''
print(t1)
t2 = """
작은따옴표(')
큰따옴표(")
"""
print(t2)
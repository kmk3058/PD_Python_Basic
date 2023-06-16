import streamlit as st


def hotel_information(name, img, star, desc, map, link):
    return dict(name=name, img=img, star=star, desc=desc, map=map, link=link)


# 마크다운
# https://heropy.blog/2017/09/30/markdown/

# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정 => 마크다운
# st.markdwon -> 명백하게 마크다운을 사용하겠다.

st.write("""
# 가장 큰 제목 텍스트 (h1 - headlline1 - st.title)
## 그 다음 큰 제목 (h2 - hedline2 - st.headeer)
### 그것보단 작은 제목 (h3 - headline3 - st.subheader)
#### 좀 더 작은 제목 
##### 더더더더더 작은 제목
###### #6까지 사용이 가능하다. 하지만 일반적으로 #3까지 사용한다 
""")

# 서식
text = """
기울임 : *별표* 또는 _언더바_ 하나씩 써주면 
진하게(bold) : **별표** 또는 __언더바__두개씩 써주면
기울임 + 진하게 : ***별표*** 세개씩 써주면
취소선 : ~물결표~
밑줄 : <u>밑줄</u>
형광펜 : <mark>형광펜</mark>
"""

# st.write(text)
st.markdown(text, unsafe_allow_html=True)

# 레이이웃
st.divider()
st.subheader("레이아웃")
st.write("""
    #### 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        * 들여쓰기1
            * 들여쓰기2
                * 들여쓰기 3
""")

st.write("""
    #### 순서가 있는 리스트
    1. 순서가
    2. 있는
    4. 리스트 - 숫자를 건너 뛰어도 무시하고 순서를 따름
        1. 들여쓰기1
            1. 들여쓰기2 # 1로 시작하지 않으면 들여쓰기는 무시
                1. 들여쓰기3
    1. 순서가
    1. 1로 넣어도
    1. 증가됨
    ### 가로줄
    ---
    (---)
    ___
    (___)
    ### 테이블(표)
    |이름|직업|
    |-----|---|
    |파이썬|백수|
    |자바|일잘러|
""")

# 링크
st.divider()
st.subheader("링크")
l1 = "https://naver.com"
l2 = "https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg"
st.write(f"""
    * [표시할 텍스트](https://naver.com)
    * [표시할 텍스트]({l1})
    * ![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)
    * ![이미지에 대한 설명]({l2})
    * [![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)](https://naver.com)
""")

# 인용
st.divider()
st.subheader("인용")
st.write(f"""
    > 무언가 멋진 말 - 유명한 사람


    > 진입장벽은 수익이다 - 어느 코딩 강사 

    책이나, 사람말 인용할 때...
    > 인용 첫줄 
    >> 인용문 안에 인용임

    #### 코드
    `코드를 나타낼 때 주로 쓰이는 묶음 표시`
    ```
    SELECT *
    FROM celeb
    WHERE age = 24 and agency like "%엔터테이먼_'
    ORDER BY age desc name asc ; 
    ```
""")

exp = st.expander("Surprise!!!", expanded=False)
exp.image("https://i.namu.wiki/i/5lWwYGj-VC8ZqJxug7Exm5-7rHE97fdZui3DWEAjm0zdLiBCbcdw4mLyGhcbZ_KecZOQr4rtwNJSFs63Rsdd_Q.webp")
# with exp: ...

# 입력
st.title("입력")
name = st.text_input("나의 이름은")  # 변수로 받을 수 있음
name2 = st.text_input("너의 이름은")  # 변수로 받을 수 있음
# st.text_input("")
# st.write(name)
# st.write(name2)
st.write(f"신랑 {name}과 신부 {name2}는...")
# number = st.number_input("당신의 나이는?")
age = st.number_input("당신의 나이는?", step=1)
st.write(f"나의 나이는 {age}세")
height = st.number_input("당신의 키는?", step=0.1)
st.write(f"나의 키는 {height}cm")
# https://docs.streamlit.io/library/api-reference/widgets

st.divider()
mode = st.checkbox("강사님 잔소리모드")  # bool (T/F)
col1, col2, col3 = st.columns(3)
r = col1.radio("잔소리 내용 선택", ["취업", "코딩", "지각"])
s = col2.slider("잔소리 강도 선택", min_value=1, max_value=10)
b = col3.selectbox("잔소리 말투 선택", ["친절하게", "반말", "모욕적"])
if mode:
    # r -> 취업, 코딩, 지각
    format = None
    if b == "친절하게":
        format = lambda x: f"여러분~ {x}"
    elif b == "반말":
        format = lambda x: f"야! {x}"
    elif b == "모욕적":
        format = lambda x: f"XXXXXX! {x}"
    if r == "취업":
        for i in range(s):
            st.write(format("8월에는 자소서 넣어야겠죠?"))
    elif r == "코딩":
        st.write(format("저보다 파이썬 잘해요?"))
    elif r == "지각":
        st.write(format("9시랑 9시 1분은 다른 거에요."))


cols = st.columns(2)  # 컬럼 리스트
cols[0].write("👨🏿‍🔬")
cols[1].write("👨🏿‍🔬")
cols = st.columns(3)
# 🐦 -> n등분 -> 3등분
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")
cols = cols[0].columns(3) # 열의 열인 거임
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")
col1, col2 = st.columns(2) # 리스트 언패킹
col1.write("왼쪽 열")
col2.write("오른쪽 열")

with col1: # col1을 기준으로 streamlit을 써주겠다
    # 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col1에 종속
    st.write("왼쪽")
with col2: # col2을 기준으로 streamlit을 써주겠다
    # 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col2에 종속
    st.write("오른쪽")
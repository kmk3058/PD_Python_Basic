import streamlit as st

import streamlit as st

st.title("워커힐 호텔")
st.divider()
st.write("## 호텔 전경")
st.image("https://www.walkerhill.com/assets/hub/global/images/etc/pic_aboutVisual01.jpg")

# 위-아래로 한 줄로만....
st.write(
    "## 결정 등급 : ⭐⭐⭐⭐⭐")
grade_image = "https://blog.kakaocdn.net/dn/qYROA/btrSnWRFZZq/k52hvOghfcJlPZoN2fHKHk/img.jpg"
st.image(grade_image)

# tabs = st.tabs(["김치찌개", "된장찌개", "로제마라어묵찌개"])
st.write("### 호텔 리뷰 ")
tab_review = ["브이로그1", "브이로그2", "브이로그3"]
tab1, tab2, tab3 = st.tabs(tab_review)
with tab1 :
    video1 = "https://www.youtube.com/watch?v=UjgIed4Sp-M"
    tab1.video(video1)
with tab2 :
    video2 = "https://www.youtube.com/watch?v=mrwBbF4MH6s"
    tab2.video(video2)
with tab3 :
    video3 = "https://www.youtube.com/watch?v=OyJ7gQ7gEvk"
    tab3.video(video3)

# 호텔 월별 데이터 현황

import pandas as pd

st.title('2023 워커힐 호텔 월별 데이터 현황')

df = pd.read_csv("./hotel_data/WALKERHILL_HOTEL.csv")

st.subheader('호텔 데이터')
option = st.selectbox(
    'Select Data',
    (df['INDEX']))

station_data = df.loc[(df['INDEX'] == option)]
station_data = station_data
s_index = station_data.index.tolist()
st.line_chart(station_data.loc[s_index[0]], use_container_width=True
)


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

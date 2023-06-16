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



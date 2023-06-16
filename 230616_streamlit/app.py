import streamlit as st

st.title("서울 5성급 호텔 ")
st.header("수업 8일차에 만들었습니다.")
st.subheader("그래도 잘 만들었죠?")
st.write("내가 만든 streamlit 페이지, 너를 위해 구었지")

# streamlit run app.py -> 터미널에 입력하면 지금까지의 현황 파악할 수 있음.

# local URL : 나만 볼 수 있는 네트워크

# 기능이 실행되는 순서대로 화면에서 표현된다.
st.video("https://www.youtube.com/watch?v=m8tMMaN6hGA")
st.image("https://cdn.pixabay.com/photo/2013/03/21/15/52/basketball-95607_1280.jpg")
st.image("img/img.jpg", width=500, use_column_width=True)
# https://imgur.com


# 컴포넌트
st.title("컴포넌트")
# 위 아래로 한 줄로만...
st.write("👩‍🌾")
cols = st.columns(2) # 컬럼 리스트
cols[0].write("👩‍🌾")
cols[1].write("👩‍🏫")
cols = st.columns(3) # 컬럼 리스트
# 🐷 -> n 등분 -> 3등분
cols[0].write("🐷 돼지 1마리")
cols[1].write("🐷 돼지 2마리")
cols[-1].write("🐷 돼지 3마리")
cols1 = cols[0].columns(3) # 열의 열인 거임
cols1[0].write("🐦 새")
cols1[1].write("🐦 새")
cols1[-1].write("🐦새")
cols2 = cols[1].columns(3) # 열의 열인 거임
cols2[0].write("🐦 새")
cols2[1].write("🐦 새")
cols2[-1].write("🐦새")
cols3 = cols[2].columns(3) # 열의 열인 거임
cols3[0].write("🐦 새")
cols3[1].write("🐦 새")
cols3[-1].write("🐦새")
col1, col2 = st.columns(2)
col1.write("왼쪽 열 ")
col2.write("오른쪽 열 ")

with col1: # col1을 기준으로 streamlit을 써주겠다
    # 블록(:) 을 열면 -> 이 안에서 streamlit
    # 기능 실행시 col1에 종속
    st.write("왼쪽")
    st.write("주간 뉴스")

with col2: # col2을 기준으로 streamlit을 써주겠다
    # 블록(:) 을 열면 -> 이 안에서 streamlit
    # 기능 실행시 col2에 종속
    st.write("오른쪽")
    st.write("월간 뉴스")

tab_menus = ["김치찌개", "된장찌개", "로제마라어묵찌개"]
tab1, tab2, tab3 = st.tabs(tab_menus)
tab1.image("https://i.namu.wiki/i/8drgvI-cQLUfJDC00zbl2ZolK4W3o4ZkVSpR-zM5FZk_QzT58vYnx_7ohk0qwGYYiSLPiZgwccyIEFUtYKDjUQ.webp")

with tab2:
    img2 = "https://img-cf.kurly.com/shop/data/goodsview/20220428/gv40000308045_1.jpg"
    st.image(img2)

with tab3:
    st.write("해당 메뉴는 없습니다.")
exp1 = st.expander("Surprise!!!", expanded=False)
exp1.write("선물")

with exp1:
    st.image("https://i0.wp.com/blog.bungee.work/wp-content/uploads/2023/02/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%86%A1%EC%84%A0%EB%AC%BC%ED%95%98%EA%B8%B0%EC%9E%85%EC%A0%90_%EB%B2%88%EC%A7%80_2.png?resize=1024%2C533&ssl=1")

# 입력
st.title("입력")
name1 = st.text_input("나의 이름은") # 변수로 받을 수 있음.
st.write(name1)

name2 = st.text_input("너의 이름은") # 변수로 받을 수 있음.
st.write(name2)

st.write(f"오늘의 언어 {name1}과 신부 {name2}는...")

age = st.number_input("당신의 나이는?", min_value=0, max_value=100, step=1)

st.write(f"나의 나이는 {age}살 입니다.")

weight = st.number_input("당신의 몸무게는?")
st.write(f"나의 몸무게는 {weight} KG 입니다.")
import streamlit as st

st.title("나의 파이썬 웹 페이지")
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


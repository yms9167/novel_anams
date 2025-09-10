import streamlit as st
import os

# Streamlit 앱의 기본 설정
st.set_page_config(layout="wide", page_title="정보과제연구")

# CSS를 사용하여 Streamlit의 기본 여백 제거
st.markdown("""
<style>
.reportview-container .main .block-container{
    padding-top: 0rem;
    padding-right: 0rem;
    padding-left: 0rem;
    padding-bottom: 0rem;
}
</style>
""", unsafe_allow_html=True)

# 페이지 선택을 위한 사이드바
page_options = {
    "연구 계획서": "index.html",
    "팀 분배기": "index2.html"
}

# 사이드바에서 페이지를 선택
selected_page = st.sidebar.selectbox("페이지를 선택하세요", list(page_options.keys()))
selected_file = page_options[selected_page]

# 현재 스크립트 파일의 디렉토리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
# 선택된 HTML 파일의 절대 경로를 지정합니다.
html_file_path = os.path.join(current_dir, "htmls", selected_file)

try:
    # HTML 파일을 읽어와 변수에 저장합니다.
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_code = f.read()

    # Streamlit에 HTML 코드를 렌더링합니다.
    st.components.v1.html(html_code, height=1200, scrolling=True)

except FileNotFoundError:
    st.error(f"오류: '{html_file_path}' 파일을 찾을 수 없습니다.")
    st.warning(f"Streamlit 앱을 실행하기 전에 'htmls' 폴더 안에 '{selected_file}' 파일이 있는지 확인해주세요.")
except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")

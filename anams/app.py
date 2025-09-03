import streamlit as st
import os.path as path

# Streamlit 앱의 기본 설정
st.set_page_config(layout="wide", page_title="AI 소설과 독자의 감정 연구")

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

# HTML 파일의 경로를 지정합니다.
# 이 파일은 'htmls' 폴더 안에 'index.html'이라는 이름으로 있어야 합니다.
html_file_path = path.join("htmls", "index.html")

try:
    # HTML 파일을 읽어와 변수에 저장합니다.
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_code = f.read()

    # Streamlit에 HTML 코드를 렌더링합니다.
    st.components.v1.html(html_code, height=1200, scrolling=True)

except FileNotFoundError:
    st.error(f"오류: '{html_file_path}' 파일을 찾을 수 없습니다.")
    st.warning("Streamlit 앱을 실행하기 전에 'htmls' 폴더 안에 'index.html' 파일이 있는지 확인해주세요.")
except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")

import streamlit as st
import os
from streamlit.components.v1 import html

# --- 설정 및 파일 경로 정의 ---
# Streamlit 앱이 실행되는 위치를 기준으로 'anams' 폴더를 지정합니다.
FOLDER_PATH = "anams"
HTML_FILES = ["index.html", "index2.html", "index3.html", "index4.html"]

# 파일에 대한 사용자 친화적인 제목을 정의합니다.
FILE_TITLES = {
    "index.html": "1. AI 소설과 독자의 감정 연구 (연구계획)",
    "index2.html": "2. 팀 밸런스 분배기 (도구)",
    "index3.html": "3. 알고리즘 성능 비교기 (도구)",
    "index4.html": "4. 정보과제연구 계획서 (DAG 정리)",
}

# Streamlit 페이지 설정
st.set_page_config(
    page_title="Anams HTML 프로젝트 뷰어",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- HTML 파일 로드 함수 ---
def load_html(filepath):
    """지정된 경로에서 HTML 파일의 내용을 읽어옵니다."""
    try:
        if os.path.exists(filepath):
            # 한글 인코딩 문제 방지를 위해 'utf-8'로 읽습니다.
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return f"오류: 파일을 찾을 수 없습니다. 경로: {filepath}"
    except Exception as e:
        return f"파일 읽기 오류: {e}"

# --- Streamlit UI 구성 ---

# 제목
st.title("Anams HTML 프로젝트 뷰어")
st.markdown("---")

# 사이드바에서 표시할 파일 선택
selected_file_name = st.sidebar.selectbox(
    "표시할 HTML 파일을 선택하세요:",
    options=HTML_FILES,
    # selectbox에 표시될 이름은 FILE_TITLES 딕셔너리를 사용하여 사용자 친화적으로 변경합니다.
    format_func=lambda x: FILE_TITLES.get(x, x)
)

# 선택된 파일의 경로와 내용 로드
full_filepath = os.path.join(FOLDER_PATH, selected_file_name)
html_content = load_html(full_filepath)

# --- HTML 내용 표시 ---

# 현재 선택된 파일의 제목을 메인 화면에 표시
st.header(FILE_TITLES.get(selected_file_name, selected_file_name))
st.markdown("---")

# 파일 로드 오류 체크
if html_content.startswith("오류: 파일을 찾을 수 없습니다."):
    st.error(html_content)
    st.warning(
        f"""
        **🚨 파일 위치 확인 필요!**
        앱이 실행되는 위치에 **`{FOLDER_PATH}`** 폴더를 생성하고,
        그 안에 **`{selected_file_name}`** 파일이 있는지 확인해주세요.
        """
    )
    # 로드되지 않은 경우, 파일 목록도 함께 표시
    st.markdown("---")
    st.subheader("예상 파일 목록:")
    st.markdown(f"- `{FOLDER_PATH}/index.html`")
    st.markdown(f"- `{FOLDER_PATH}/index2.html`")
    st.markdown(f"- `{FOLDER_PATH}/index3.html`")
    st.markdown(f"- `{FOLDER_PATH}/index4.html`")

else:
    # streamlit.components.v1.html을 사용하여 HTML 코드를 렌더링합니다.
    # height와 scrolling=True를 설정하여 긴 HTML 문서도 스크롤하여 볼 수 있게 합니다.
    html(html_content, height=800, scrolling=True)

    # 디버깅을 위해 현재 로드된 파일 경로를 표시합니다.
    st.caption(f"현재 로드된 파일: `{full_filepath}`")

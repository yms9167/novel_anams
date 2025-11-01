import streamlit as st
import streamlit.components.v1 as components
import os

# 💡 수정: os.path 모듈을 사용하여 현재 파일(__file__)의 디렉토리를 가져옵니다.
# 이는 'app2.py' 파일이 어디에 있든, 그 파일의 실제 디렉토리를 기준으로 경로를 찾게 합니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# HTML_FILE_PATH를 절대 경로로 조합합니다.
# 'app2.py'가 있는 디렉토리/htmls2/index6.html
HTML_FILE_PATH = os.path.join(BASE_DIR, "htmls2", "index6.html")

def load_html_content(filepath):
    """지정된 HTML 파일의 내용을 읽어옵니다."""
    try:
        # 파일이 존재하는지 확인 (이제 절대 경로를 사용하므로 더 안정적입니다)
        if not os.path.exists(filepath):
            # 오류 메시지에 찾으려는 전체 경로를 포함하여 디버깅을 돕습니다.
            return f"오류: HTML 파일을 찾을 수 없습니다. 경로: {filepath}"
        
        # UTF-8 인코딩으로 파일 내용을 읽기
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except Exception as e:
        return f"파일을 읽는 중 오류가 발생했습니다: {e}"

# Streamlit 앱 시작
st.set_page_config(layout="wide", page_title="업무 우선순위 정리기") # 페이지 제목도 수정했습니다.
st.title("Streamlit으로 HTML 렌더링")

# HTML 파일 내용 로드
html_content = load_html_content(HTML_FILE_PATH)

if html_content.startswith("오류"):
    # 오류 메시지 표시
    st.error(html_content)
    # 현재 작업 디렉토리도 확인용으로 표시하면 좋습니다.
    st.markdown(f"**현재 작업 디렉토리 (CWD):** `{os.getcwd()}`")
    st.markdown(f"**시도된 절대 경로:** `{HTML_FILE_PATH}`")
else:
    # 렌더링
    components.html(html_content, height=800, scrolling=True) # 충분한 높이를 지정합니다.

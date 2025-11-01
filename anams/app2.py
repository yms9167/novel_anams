import streamlit as st
import streamlit.components.v1 as components
import os

# 파일 경로 설정 (app2.py와 동일한 디렉토리에서 실행된다고 가정)
HTML_FILE_PATH = "htmls2/index6.html"

def load_html_content(filepath):
    """지정된 HTML 파일의 내용을 읽어옵니다."""
    try:
        # 파일이 존재하는지 확인
        if not os.path.exists(filepath):
            return f"오류: HTML 파일을 찾을 수 없습니다. 경로: {filepath}"
        
        # UTF-8 인코딩으로 파일 내용을 읽기
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content
    except Exception as e:
        return f"파일을 읽는 중 오류가 발생했습니다: {e}"

# Streamlit 앱 시작
st.set_page_config(layout="wide", page_title="HTML Renderer")
st.title("Streamlit으로 HTML 렌더링")

# HTML 파일 내용 로드
html_content = load_html_content(HTML_FILE_PATH)

if html_content.startswith("오류"):
    # 오류 메시지 표시
    st.error(html_content)
    st.markdown(f"**현재 예상되는 HTML 파일 경로:** `{HTML_FILE_PATH}`")
    st.markdown("스크린샷에 따르면, `app2.py`는 루트 폴더에 있고, HTML 파일은 `htmls2/index6.html`에 있어야 합니다.")
else:
    # 성공적으로 로드된 HTML 콘텐츠를 Streamlit 컴포넌트로 렌더링
    # height와 scrolling=True를 설정하여 콘텐츠가 iframe 내에서 잘 보이도록 합니다.
    st.subheader(f"파일: {HTML_FILE_PATH}")
    components.html(html_content, height=800, scrolling=True)

# Streamlit 앱을 실행하려면 터미널에서 다음 명령을 실행하세요:
# streamlit run app2.py

import streamlit as st
import streamlit.components.v1 as components
import os

# 파일 경로 및 표시 이름 정의 (파일이 'htmls' 폴더 안에 있다고 가정)
HTML_FILES = {
    "AI 소설과 독자의 감정 연구": "htmls/index.html",
    "팀 밸런스 분배기": "htmls/index2.html",
    "알고리즘 성능 비교기": "htmls/index3.html",
    "DAG 기반 순차 정리 프로그램": "htmls/index4.html",
}

def load_html_content(filepath):
    """지정된 경로에서 HTML 파일 내용을 읽어옵니다."""
    try:
        # 파일이 실제로 존재하는지 확인
        if not os.path.exists(filepath):
            return f"<div style='padding: 20px; color: red; background-color: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px;'>오류: 파일을 찾을 수 없습니다. 경로를 확인해주세요: <strong>{filepath}</strong></div>"
        
        # UTF-8 인코딩으로 파일 내용을 읽어옴
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        # 파일 읽기 중 발생할 수 있는 기타 오류 처리
        return f"<div style='padding: 20px; color: red; background-color: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px;'>파일을 읽는 중 오류가 발생했습니다: {e}</div>"

# Streamlit 앱 설정
st.set_page_config(
    page_title="HTML 파일 뷰어",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.divider()

# --- 1. 사이드바 네비게이션 ---
st.sidebar.title("HTML 문서 목록")

# 사용자가 선택할 수 있도록 파일 목록 표시
page_selection = st.sidebar.selectbox(
    "문서를 선택하세요:",
    list(HTML_FILES.keys())
)

# --- 2. HTML 렌더링 ---
if page_selection:
    # 선택된 파일의 경로를 가져옴
    filepath_to_load = HTML_FILES[page_selection]
    
    # 파일 내용을 불러옴
    html_content = load_html_content(filepath_to_load)
    
    st.subheader(f"📄 {page_selection} 미리보기")
    
    # st.components.v1.html을 사용하여 HTML 내용을 Streamlit 앱에 임베드합니다.
    # height를 충분히 주어 스크롤이 가능하도록 설정
    components.html(
        html_content,
        height=900, 
        width=None,
        scrolling=True
    )


st.sidebar.markdown("---")


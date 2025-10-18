import streamlit as st
import streamlit.components.v1 as components
import os

# 파일 경로 및 표시 이름 정의 
# app.py와 htmls 폴더가 모두 'anams' 폴더 안에 있으므로, 
# app.py 기준으로 'htmls/'를 사용하여 상대 경로를 지정합니다.
HTML_FILES = {
    "AI 소설과 독자의 감정 연구 (index.html)": "htmls/index.html",
    "팀 밸런스 분배기 (index2.html)": "htmls/index2.html",
    "알고리즘 성능 비교기 (index3.html)": "htmls/index3.html",
    "DAG 기반 순차 정리 프로그램 (index4.html)": "htmls/index4.html",
    "데이터 패킷 최단 경로 보고서 (index5.html)": "htmls/index5.html",
}

def load_html_content(filepath):
    """지정된 경로에서 HTML 파일 내용을 읽어옵니다."""
    try:
        # 파일이 실제로 존재하는지 확인
        if not os.path.exists(filepath):
            return f"""
            <div style='padding: 20px; color: #991b1b; background-color: #fca5a5; border: 1px solid #dc2626; border-radius: 8px; font-family: sans-serif;'>
                <h2>파일 오류: 경로를 찾을 수 없습니다!</h2>
                <p>경로를 확인해주세요: <strong>{filepath}</strong></p>
                <p><strong>조치:</strong> HTML 파일을 'htmls' 폴더 안에 넣었는지 확인해주세요.</p>
            </div>"""
        
        # UTF-8 인코딩으로 파일 내용을 읽어옴
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        # 파일 읽기 중 발생할 수 있는 기타 오류 처리
        return f"""
        <div style='padding: 20px; color: #991b1b; background-color: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; font-family: sans-serif;'>
            <h2>파일 읽기 중 오류 발생</h2>
            <p>오류 내용: {e}</p>
        </div>"""

# Streamlit 앱 설정
st.set_page_config(
    page_title="HTML 파일 뷰어",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Streamlit HTML 파일 뷰어")
st.markdown("왼쪽 사이드바에서 표시할 HTML 문서를 선택하세요.")
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
    
    # Streamlit 컴포넌트를 사용하여 HTML 내용을 렌더링 (높이 설정 필수)
    components.html(html_content, height=800, scrolling=True)
else:
    st.info("사이드바에서 문서를 선택하여 내용을 확인하세요.")

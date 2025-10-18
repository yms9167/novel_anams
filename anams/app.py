import streamlit as st
import streamlit.components.v1 as components
import os
import sys # sys 모듈 추가

# --- 경로 설정: app.py 파일이 어디서 실행되든 항상 같은 경로를 참조하도록 수정 ---
# 1. 현재 app.py 파일이 위치한 디렉토리의 절대 경로를 가져옵니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
# 2. HTML 파일들이 있는 폴더의 절대 경로를 계산합니다.
HTML_FOLDER_PATH = os.path.join(BASE_DIR, "htmls")
# -------------------------------------------------------------------------

# 파일 경로 및 표시 이름 정의 
# 이제 경로는 HTML_FOLDER_PATH를 기준으로 하므로 'htmls/' 접두사를 제거합니다.
HTML_FILES = {
    "AI 소설과 독자의 감정 연구": "index.html",
    "팀 밸런스 분배기": "index2.html",
    "알고리즘 성능 비교기": "index3.html",
    "DAG 기반 순차 정리 프로그램": "index4.html",
    "데이터 패킷 최단 경로 보고서": "index5.html",
}

def load_html_content(filename):
    """지정된 파일 이름에 BASE_DIR/htmls 경로를 결합하여 파일 내용을 읽어옵니다."""
    
    # --- 실제 파일 경로 계산 ---
    filepath = os.path.join(HTML_FOLDER_PATH, filename)
    # -------------------------

    # --- 파일 경로 문제 진단을 위한 코드 ---
    current_working_directory = os.getcwd()
    absolute_path_attempted = filepath # 이제 filepath 자체가 절대 경로를 포함합니다.
    
    # Streamlit 사이드바에 진단 정보 표시 (사용자 디버깅용)
    st.sidebar.markdown("---")
    st.sidebar.caption("🔍 **경로 진단 정보** (절대 경로 기준)")
    st.sidebar.caption(f"1. 현재 작업 디렉토리 (CWD): `{current_working_directory}`")
    st.sidebar.caption(f"2. 파일을 찾고 있는 절대 경로: `{absolute_path_attempted}`")
    # ---------------------------------------------
    
    try:
        # 파일이 실제로 존재하는지 확인
        if not os.path.exists(filepath):
            # 파일을 찾지 못했을 때 사용자에게 안내
            return f"""
            <div style='padding: 20px; color: red; background-color: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px;'>
                <h3>⚠️ 오류: 파일을 찾을 수 없습니다.</h3>
                <p><strong>스크립트가 찾은 위치:</strong> <code>{absolute_path_attempted}</code></p>
                <p>✅ <strong>해결 방법:</strong> <code>htmls</code> 폴더 내에 해당 파일(`{filename}`)이 존재하는지 확인해 주세요.</p>
            </div>
            """
        
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
    # 선택된 파일의 이름을 가져옴
    filename_to_load = HTML_FILES[page_selection]
    
    # 파일 내용을 불러옴
    html_content = load_html_content(filename_to_load)
    
    st.subheader(f"📄 {page_selection} 미리보기")
    
    # st.components.v1.html을 사용하여 HTML 내용을 Streamlit 앱에 임베드합니다.
    # height를 충분히 주어 스크롤이 가능하도록 설정
    components.html(
        html_content,
        height=900, 
        width=None,
        scrolling=True
    )
else:
    st.info("왼쪽 사이드바에서 표시할 HTML 파일을 선택해주세요.")

# 기존 참고사항 업데이트
st.sidebar.markdown(
    """
    **참고:** 이 앱은 **`app.py` 파일의 절대 경로를 기준**으로 파일을 읽어오도록 수정되었습니다. 이제 실행 위치에 관계없이 파일을 찾을 수 있습니다.
    """
)

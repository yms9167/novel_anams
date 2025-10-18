import streamlit as st
import streamlit.components.v1 as components
import os

# 파일 경로 및 표시 이름 정의 
# app.py와 htmls 폴더가 모두 'anams' 폴더 안에 있으므로, 
# app.py 기준으로 'htmls/'를 사용하여 상대 경로를 지정합니다.
HTML_FILES = {
    "AI 소설과 독자의 감정 연구": "htmls/index.html",
    "팀 밸런스 분배기": "htmls/index2.html",
    "알고리즘 성능 비교기": "htmls/index3.html",
    "DAG 기반 순차 정리 프로그램": "htmls/index4.html",
    "데이터 패킷 최단 경로 보고서": "htmls/index5.html", # 새로운 파일 추가
}

def load_html_content(filepath):
    """지정된 경로에서 HTML 파일 내용을 읽어옵니다."""
    
    # --- 파일 경로 문제 진단을 위한 코드 추가 ---
    current_working_directory = os.getcwd()
    absolute_path_attempted = os.path.abspath(filepath)
    
    # Streamlit 사이드바에 진단 정보 표시 (사용자 디버깅용)
    st.sidebar.markdown("---")
    st.sidebar.caption("🔍 **경로 진단 정보**")
    st.sidebar.caption(f"1. 현재 작업 디렉토리 (CWD): `{current_working_directory}`")
    st.sidebar.caption(f"2. 시도 중인 절대 경로: `{absolute_path_attempted}`")
    # ---------------------------------------------
    
    try:
        # 파일이 실제로 존재하는지 확인
        if not os.path.exists(filepath):
            # 파일을 찾지 못했을 때 사용자에게도 절대 경로 정보를 제공하여 디버깅을 돕습니다.
            return f"""
            <div style='padding: 20px; color: red; background-color: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px;'>
                <h3>⚠️ 오류: 파일을 찾을 수 없습니다.</h3>
                <p><strong>시도된 상대 경로:</strong> <code>{filepath}</code></p>
                <p><strong>스크립트가 찾은 위치:</strong> <code>{absolute_path_attempted}</code></p>
                <p>✅ <strong>해결 방법:</strong> <code>streamlit run app.py</code> 명령을 <code>htmls</code> 폴더의 한 단계 위 폴더(최상위 프로젝트 폴더)에서 실행해 보세요.</p>
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
    # 선택된 파일의 경로를 가져옴
    filepath_to_load = HTML_FILES[page_selection]
    
    # 파일 내용을 불러옴 (경로 진단 정보가 이 함수 내에서 사이드바에 출력됨)
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
else:
    st.info("왼쪽 사이드바에서 표시할 HTML 파일을 선택해주세요.")

# 기존 참고사항은 진단 정보 아래로 이동
st.sidebar.markdown(
    """
    **참고:** 이 앱은 **`app.py`** 기준으로 **`htmls/`** 폴더에서 파일을 읽어오도록 설정되어 있습니다. 
    """
)

import streamlit as st
import streamlit.components.v1 as components
import os
import pathlib # 경로 처리를 위해 pathlib 모듈 추가

# 현재 app.py 파일이 위치한 디렉토리(anams 폴더)를 기준으로 설정합니다.
APP_DIR = pathlib.Path(__file__).parent.resolve()

# 파일 경로 및 표시 이름 정의 
# 경로는 여전히 'htmls/'로 지정되지만, 실제 파일 로딩 시 APP_DIR과 결합됩니다.
HTML_FILES = {
    "AI 소설과 독자의 감정 연구": "htmls/index.html",
    "팀 밸런스 분배기": "htmls/index2.html",
    "알고리즘 성능 비교기": "htmls/index3.html",
    "DAG 기반 순차 정리 프로그램": "htmls/index4.html",
}

def load_html_content(filepath):
    """지정된 경로에서 HTML 파일 내용을 읽어옵니다. (APP_DIR 기준)"""
    # APP_DIR과 상대 경로(filepath)를 결합하여 파일의 절대 경로를 생성합니다.
    full_path = APP_DIR / filepath
    
    try:
        # 파일이 실제로 존재하는지 확인
        if not full_path.exists():
            # 오류 메시지에 실제 시도한 절대 경로를 포함하여 출력
            error_message = f"오류: 파일을 찾을 수 없습니다."
            
            # 사용자에게 표시할 오류 메시지 (HTML 포맷)
            return f"""
                <div style='padding: 20px; color: red; background-color: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px;'>
                    {error_message}
                    <br><br>
                    <strong>시도한 경로:</strong> <code>{full_path}</code>
                    <br>
                    <p style="margin-top: 10px; font-size: 14px;">
                        <strong>해결 안내:</strong> 위에 표시된 **절대 경로**에 해당 파일이 정확히 존재하는지, 그리고 파일명(대소문자 포함)이 맞는지 다시 한번 확인해주세요.
                    </p>
                </div>
            """
        
        # 파일 내용을 읽어옴 (pathlib 객체를 open 함수에 바로 전달)
        with open(full_path, 'r', encoding='utf-8') as f:
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

# --- 1. 사이드바 네비게이션 ---
st.sidebar.title("HTML 문서 목록")

# 사용자가 선택할 수 있도록 파일 목록 표시
page_selection = st.sidebar.selectbox(
    "문서를 선택하세요:",
    list(HTML_FILES.keys())
)

# --- 2. HTML 렌더링 ---
if page_selection:
    # 선택된 파일의 상대 경로를 가져옴
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
else:
    st.info("왼쪽 사이드바에서 표시할 HTML 파일을 선택해주세요.")

st.sidebar.markdown("---")

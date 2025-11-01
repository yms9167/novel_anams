import streamlit as st
import streamlit.components.v1 as components
import os
import glob
from collections import OrderedDict

# HTML 파일들이 위치한 디렉토리 이름 정의
HTML_DIR = "htmls"

def get_html_files_dynamically():
    """
    지정된 디렉토리(HTML_DIR)에서 모든 .html 파일을 찾아 맵핑을 생성합니다.
    {파일 이름 (확장자 제외): 파일 전체 경로} 형태의 OrderedDict를 반환합니다.
    """
    files_map = OrderedDict()
    
    # 1. htmls 폴더 존재 여부 확인
    if not os.path.exists(HTML_DIR):
        # 앱 실행 중 폴더가 없으면 오류 메시지를 표시하고 빈 맵을 반환합니다.
        st.error(f"오류: HTML 파일 디렉토리 '{HTML_DIR}'를 찾을 수 없습니다. 이 폴더를 생성하고 HTML 파일을 넣어주세요.")
        return files_map
    
    # 2. .html 파일 목록을 가져와 파일 이름 순으로 정렬합니다.
    # glob을 사용하여 경로와 파일 확장자를 쉽게 찾습니다.
    html_files = sorted(glob.glob(os.path.join(HTML_DIR, "*.html")))
    
    if not html_files:
        st.warning(f"경고: '{HTML_DIR}' 디렉토리에서 .html 파일을 찾을 수 없습니다. 파일을 추가해주세요.")
        return files_map

    # 3. 파일 목록을 순회하며 맵핑을 생성합니다.
    for filepath in html_files:
        # 파일 경로에서 파일 이름(예: index.html)만 추출
        filename = os.path.basename(filepath)
        # 표시 이름은 파일 이름에서 '.html' 확장자를 제거한 것으로 설정
        display_name = filename.replace('.html', '')
        
        # 파일 경로와 표시 이름을 맵에 추가
        files_map[display_name] = filepath
            
    return files_map

def load_html_content(filepath):
    """지정된 경로에서 HTML 파일 내용을 읽어옵니다."""
    try:
        # 파일이 실제로 존재하는지 확인 (get_html_files_dynamically에서 이미 확인했지만, 런타임 변경 대비)
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
    page_title="HTML 파일 뷰어 (동적 로딩)",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Streamlit HTML 파일 뷰어 (동적 로딩)")
st.markdown("왼쪽 사이드바에서 표시할 HTML 문서를 선택하세요.")
st.divider()

# --- 동적으로 파일 목록 로드 ---
HTML_FILES = get_html_files_dynamically()
file_keys = list(HTML_FILES.keys())

# --- 1. 사이드바 네비게이션 ---
st.sidebar.title("HTML 문서 목록")

if file_keys:
    # 사용자가 선택할 수 있도록 동적으로 로드된 파일 목록 표시
    page_selection = st.sidebar.selectbox(
        "문서를 선택하세요 (파일 이름 기준):",
        file_keys
    )
    
    # --- 2. HTML 렌더링 ---
    if page_selection:
        # 선택된 파일의 경로를 가져옴
        filepath_to_load = HTML_FILES[page_selection]
        
        # 파일 내용을 불러옴
        html_content = load_html_content(filepath_to_load)
        
        st.subheader(f"📄 {page_selection}.html 미리보기")
        
        # st.components.v1.html을 사용하여 HTML 내용을 Streamlit 앱에 임베드합니다.
        components.html(
            html_content,
            height=900, 
            width=None,
            scrolling=True
        )
else:
    st.info("HTML 파일을 찾을 수 없습니다. 'htmls' 폴더를 확인하거나 파일을 추가해주세요.")


st.sidebar.markdown("---")
st.sidebar.markdown(
    f"""
    **참고:** 이 앱은 **`{HTML_DIR}/`** 폴더를 **자동으로 스캔**하여 `.html` 파일을 불러옵니다.
    <br>표시 이름은 파일 이름에서 `.html` 확장자를 제거한 형태를 사용합니다.
    """, unsafe_allow_html=True
)

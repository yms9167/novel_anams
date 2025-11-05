import streamlit as st
import os
import streamlit.components.v1 as components

# --- 설정 및 초기화 ---
# app2.py가 htmls2 폴더 안에 있으므로, HTML_DIR을 '.'로 설정하여 현재 폴더를 기준으로 파일을 찾습니다.
HTML_DIR = "."

def read_html_file(filename: str) -> str:
    """HTML 파일의 내용을 읽어옵니다."""
    try:
        # 파일 경로를 결합합니다.
        filepath = os.path.join(HTML_DIR, filename)
        
        # 'r' 모드로 파일을 열고 UTF-8 인코딩을 사용합니다.
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"오류: 파일 '{filename}'을(를) 찾을 수 없습니다. 경로를 확인해 주세요."
    except Exception as e:
        return f"파일 읽기 오류가 발생했습니다: {e}"

# --- Streamlit 앱 시작 ---
st.set_page_config(layout="wide", page_title="HTML 파일 뷰어")

st.title("🌐 Streamlit HTML 파일 뷰어 (htmls2 폴더)")
st.markdown("현재 폴더 (`htmls2`)에 있는 HTML 파일들을 선택하여 Streamlit에서 렌더링합니다.")

# 현재 디렉토리의 모든 파일 목록을 가져옵니다.
try:
    all_files = os.listdir(HTML_DIR)
    # .html 확장자를 가진 파일만 필터링하고 이름순으로 정렬합니다.
    html_files = sorted([f for f in all_files if f.endswith(".html")])
except Exception as e:
    st.error(f"폴더 내용 읽기 오류: {e}")
    html_files = []


if not html_files:
    st.warning(f"'{os.getcwd()}/{HTML_DIR}' 폴더에서 HTML 파일(*.html)을 찾을 수 없습니다.")
    st.info("HTML 파일을 `htmls2` 폴더 안에 추가해 주세요.")
else:
    # 사용자에게 파일을 선택하도록 합니다.
    selected_file = st.selectbox("불러올 HTML 파일을 선택하세요:", html_files)

    if selected_file:
        html_content = read_html_file(selected_file)

        if html_content.startswith("오류:"):
            st.error(html_content)
        else:
            st.subheader(f"✅ 선택된 파일: `{selected_file}`")

            # 1. HTML 내용 렌더링 (인터랙티브 뷰)
            st.markdown("### 🖼️ HTML 렌더링 결과")
            # Streamlit의 components.v1.html을 사용하여 HTML 내용을 렌더링합니다.
            # height를 지정하여 스크롤이 가능한 영역을 만듭니다.
            components.html(html_content, height=600, scrolling=True)
            
            # 2. HTML 원본 코드 표시
            st.markdown("### 📋 HTML 원본 코드")
            st.code(html_content, language='html', line_numbers=True)

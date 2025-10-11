import streamlit as st
import streamlit.components.v1 as components
import os

# 1. 파일 경로 설정
# 이 코드를 실행하는 디렉토리 내에 'htmls' 폴더가 있고, 그 안에 HTML 파일들이 있다고 가정합니다.
HTML_DIR = "htmls"
PAGES = {
    "1. AI 소설과 독자의 감정 연구": "index.html",
    "2. 팀 밸런스 분배기": "index2.html",
    "3. 알고리즘 성능 비교기": "index3.html",
    "4. 정보과제연구 계획서": "index4.html",
}

def load_html_content(filename):
    """
    지정된 HTML 파일의 내용을 읽어 반환합니다. 
    파일을 찾지 못하거나 읽는 중 오류가 발생하면 사용자에게 안내할 HTML 코드를 반환합니다.
    """
    filepath = os.path.join(HTML_DIR, filename)
    try:
        # UTF-8 인코딩으로 파일을 읽습니다.
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        # 파일이 없을 경우 사용자에게 표시할 오류 메시지 HTML (디자인을 눈에 띄게 수정)
        return f"""
        <div style="padding: 30px; background-color: #ffebee; color: #c62828; border: 2px dashed #ef9a9a; border-radius: 12px; font-family: sans-serif;">
            <h2 style="margin-top: 0;">❌ 파일 로드 오류</h2>
            <p><strong>'{filepath}'</strong> 파일을 찾을 수 없습니다. 경로와 파일명을 확인해주세요.</p>
            <p>현재 설정된 HTML_DIR은 '{HTML_DIR}'입니다. 파일을 이 폴더에 저장했는지 확인하세요.</p>
            <p>디버깅 정보: FileNotFoundError</p>
        </div>
        """
    except Exception as e:
        # 기타 예외 발생 시 오류 메시지 HTML
        return f"""
        <div style="padding: 30px; background-color: #fff3e0; color: #ff9800; border: 2px dashed #ffcc80; border-radius: 12px; font-family: sans-serif;">
            <h2 style="margin-top: 0;">⚠️ 파일 읽기 오류</h2>
            <p>파일 <strong>'{filepath}'</strong> 을(를) 읽는 도중 예기치 않은 오류가 발생했습니다.</p>
            <p>오류 메시지: {str(e)}</p>
        </div>
        """

def main():
    """Streamlit 애플리케이션의 메인 함수입니다."""
    
    # Streamlit 페이지 설정
    st.set_page_config(
        page_title="HTML 파일 Streamlit 뷰어",
        layout="wide", # 넓은 레이아웃 사용
        initial_sidebar_state="expanded"
    )

    st.sidebar.title("📚 프로젝트 페이지")
    
    # 2. 사이드바를 이용한 페이지 선택 네비게이션
    selection_key = st.sidebar.selectbox(
        "표시할 HTML 문서를 선택하세요:", 
        list(PAGES.keys())
    )

    selected_filename = PAGES[selection_key]

    # 파일 이름에서 숫자와 점을 제거하고 제목만 표시
    st.title(f"📄 {selection_key.split('. ', 1)[1]} ({selected_filename})")
    st.markdown("---")

    # 3. HTML 파일 내용 로드
    html_content = load_html_content(selected_filename)

    # 4. Streamlit 컴포넌트를 사용하여 HTML 렌더링
    # components.html을 사용하여 HTML, CSS, JavaScript를 샌드박스 환경에서 렌더링합니다.
    # height를 1000px로 설정하여 충분한 공간을 확보하고 스크롤링을 활성화합니다.
    components.html(
        html_content,
        height=1000,  # 렌더링 영역의 높이
        scrolling=True # 스크롤 허용
    )

if __name__ == "__main__":
    main()

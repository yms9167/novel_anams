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
        <div style="padding: 30px; background-color: #ffebee; color: #c62828; border: 2px dashed #ef9a9a; border-radius: 12px; margin: 20px;">
            <h2 style="font-size: 20px; font-weight: bold; margin-bottom: 10px;">🚨 파일 로드 실패 (FileNotFoundError)</h2>
            <p><strong>HTML 파일을 찾을 수 없습니다. 경로를 확인해주세요.</strong></p>
            <p>현재 파일: {filename}</p>
            <p>경로: {filepath}</p>
            <p><strong>조치 방법:</strong> Streamlit을 실행하는 위치와 'htmls' 폴더의 위치를 확인하거나, app.py의 파일 경로 설정 방식을 수정해야 합니다.</p>
        </div>
        """
    except Exception as e:
        # 기타 읽기 오류
        return f"""
        <div style="padding: 20px; background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; border-radius: 8px; font-family: 'Inter', sans-serif;">
            <h2 style="margin-top: 0; font-size: 1.5em;">⚠️ 파일 읽기 중 예외 발생</h2>
            <p><strong>오류 내용:</strong> {str(e)}</p>
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

    st.title(f"📄 {selection_key.split('. ', 1)[1]} ({selected_filename})")
    st.markdown("---")

    # 3. HTML 파일 내용 로드
    html_content = load_html_content(selected_filename)

    # 4. Streamlit 컴포넌트를 사용하여 HTML 렌더링
    # components.html을 사용하여 HTML, CSS, JavaScript를 샌드박스 환경에서 렌더링합니다.
    # height를 1000px로 설정하여 충분한 공간을 확보하고 스크롤링을 활성화합니다.
    components.html(
        html_content,
        height=1000,  # 렌더링 영역의 높이 (필요에 따라 조정 가능)
        scrolling=True # 컨테이너 내에서 스크롤 허용
    )

    # 5. 추가 안내
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        f"""
        **현재 파일:** `{selected_filename}`<br>
        **경로:** `{HTML_DIR}/{selected_filename}`
        """
    )
    if "파일 로드 실패" in html_content: # 수정된 오류 메시지를 확인하도록 조건 변경
        st.error("⚠️ 파일 로드에 문제가 발생했습니다. 위쪽의 빨간색 오류 메시지와 사이드바의 경로 안내를 확인해주세요.")
    else:
        st.success("✅ HTML 콘텐츠가 성공적으로 로드되었습니다. JavaScript 및 동적 콘텐츠도 정상적으로 작동합니다.")

if __name__ == "__main__":
    main()

import streamlit as st
import os
import glob
from streamlit.components.v1 import html

# Set the path to the HTML directory
HTML_DIR = "htmls2"

# --- 명시적으로 불러올 파일 목록 정의 (사용자 요청 반영) ---
# 이 파일들만 Streamlit에서 선택 가능하도록 명시적으로 지정합니다.
EXPLICIT_FILES = ["index6.html", "index7.html"]

# --- Streamlit Page Configuration ---
st.set_page_config(
    layout="wide", 
    page_title="HTML 파일 로더", 
    menu_items={'About': "Streamlit을 사용하여 HTML 파일을 로드하는 앱입니다."}
)

# --- Function to load and display HTML ---
def load_and_display_html(filepath):
    """Loads the content of an HTML file and displays it in Streamlit."""
    try:
        # Read the file content with UTF-8 encoding
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Display the HTML content using st.components.v1.html
        # A fixed height is required for proper embedding. Scrolling is enabled.
        html(
            html_content, 
            height=800,  # Adjust height as needed
            scrolling=True
        )
        
    except FileNotFoundError:
        st.error(f"오류: 파일을 찾을 수 없습니다. 경로: `{filepath}`. `{HTML_DIR}` 폴더에 `{os.path.basename(filepath)}` 파일이 있는지 확인해주세요.")
    except Exception as e:
        st.error(f"HTML 파일을 로드하는 중 오류가 발생했습니다: {e}")

# --- Main App Logic ---

st.title("Streamlit HTML 파일 미리보기 (명시적 파일)")
st.markdown("---")

# Display names (used for selectbox)
file_display_names = EXPLICIT_FILES

# Full paths (참고용. 실제 파일 로딩은 selected_file_name으로 경로를 재구성하여 처리됩니다.)
html_files_full_path = [os.path.join(HTML_DIR, f) for f in EXPLICIT_FILES]


if not file_display_names:
    st.warning("경고: 명시적으로 정의된 HTML 파일 목록이 비어 있습니다.")
else:
    # Sidebar for file selection
    st.sidebar.header("HTML 파일 선택")
    selected_file_name = st.sidebar.selectbox(
        "표시할 HTML 파일을 선택하세요:",
        file_display_names
    )
    
    if selected_file_name:
        # Reconstruct the full path of the selected file
        selected_filepath = os.path.join(HTML_DIR, selected_file_name)
        
        # Display the selected file name in the main area
        st.subheader(f"선택된 파일: `{selected_file_name}`")
        
        # Load and display the selected file content
        load_and_display_html(selected_filepath)

# Display available files in the sidebar footer for debugging/info
st.sidebar.markdown("---")
st.sidebar.markdown(f"**명시적으로 정의된 파일 수: {len(file_display_names)}**")
st.sidebar.markdown(f"불러오는 파일: `{', '.join(file_display_names)}`")

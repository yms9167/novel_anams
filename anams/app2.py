import streamlit as st
import os
import glob
from streamlit.components.v1 import html

# The name of the folder containing the HTML files
HTML_DIR_NAME = "htmls2"

# Calculate the absolute path to the script's directory for robust path handling
# 이 코드를 사용하여 app2.py 파일의 위치를 기준으로 경로를 계산합니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# The full, robust path to the HTML folder
HTML_ROOT_PATH = os.path.join(BASE_DIR, HTML_DIR_NAME)

# --- 명시적으로 불러올 파일 목록 정의 (사용자 요청 반영) ---
EXPLICIT_FILES = ["index6.html", "index7.html"]

# --- Streamlit Page Configuration ---
st.set_page_config(
    layout="wide", 
    page_title="HTML 파일 로더", 
    menu_items={'About': "Streamlit을 사용하여 HTML 파일을 로드하는 앱입니다."}
)

# --- Function to load and display HTML ---
def load_and_display_html(filepath, html_dir_name):
    """Loads the content of an HTML file and displays it in Streamlit."""
    try:
        # Read the file content with UTF-8 encoding
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Display the HTML content using st.components.v1.html
        html(
            html_content, 
            height=800,  # Adjust height as needed
            scrolling=True
        )
        
    except FileNotFoundError:
        # Improved error message for clarity
        st.error(f"⚠️ **파일을 찾을 수 없습니다.**")
        st.markdown(f"- **경로 확인:** `{html_dir_name}/{os.path.basename(filepath)}` 파일을 확인해주세요.")
        st.markdown(f"- **실제 검색 경로:** `{filepath}`")
        st.markdown("- **조치:** `app2.py`와 같은 위치에 `htmls2` 폴더가 있는지, 그리고 그 안에 해당 파일이 정확히 있는지 확인해주세요.")
    except Exception as e:
        st.error(f"HTML 파일을 로드하는 중 오류가 발생했습니다: {e}")

# --- Main App Logic ---

st.title("Streamlit HTML 파일 미리보기 (명시적 파일)")
st.markdown("---")

file_display_names = EXPLICIT_FILES

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
        # Construct the full path using the robust root path
        selected_filepath = os.path.join(HTML_ROOT_PATH, selected_file_name)
        
        # Display the selected file name in the main area
        st.subheader(f"선택된 파일: `{selected_file_name}`")
        
        # Load and display the selected file content, passing the folder name for error context
        load_and_display_html(selected_filepath, HTML_DIR_NAME)

# Display available files in the sidebar footer for debugging/info
st.sidebar.markdown("---")
st.sidebar.markdown(f"**명시적으로 정의된 파일 수: {len(file_display_names)}**")
st.sidebar.markdown(f"불러오는 파일: `{', '.join(file_display_names)}`")

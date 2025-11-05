import streamlit as st
import os
import glob
from streamlit.components.v1 import html

# Set the path to the HTML directory (based on the provided image structure)
HTML_DIR = "htmls2"

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
        st.error(f"오류: 파일을 찾을 수 없습니다. 경로: `{filepath}`")
    except Exception as e:
        st.error(f"HTML 파일을 로드하는 중 오류가 발생했습니다: {e}")

# --- Main App Logic ---

st.title("Streamlit HTML 파일 미리보기")
st.markdown("---")

# Find all HTML files in the specified directory
# glob is used to find all files matching the pattern
html_files_full_path = glob.glob(os.path.join(HTML_DIR, "*.html"))

if not html_files_full_path:
    # Display warning if no HTML files are found
    st.warning(f"경고: `{HTML_DIR}` 폴더에서 `.html` 파일을 찾을 수 없습니다. 파일 경로와 폴더 구조를 확인해주세요.")
else:
    # Create a list of file names (e.g., "index6.html") for display in the dropdown
    file_display_names = [os.path.basename(f) for f in html_files_full_path]
    
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
st.sidebar.markdown(f"**총 {len(html_files_full_path)}개의 파일 발견**")

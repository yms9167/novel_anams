from flask import Flask, render_template_string
import os

app = Flask(__name__)

# 파일 경로 및 요청 경로 매핑 정의
# URL 경로 : 실제 파일명
FILE_MAPPINGS = {
    '/index4.html': 'index4.html',    # 요청하신 경로 (research_plan.html 내용 로드)
    '/index2.html': 'index2.html',
    '/index.html': 'index.html', # 팀 밸런스 분배기 로드
    # 참고: 만약 'index.html'과 'index2.html' 파일이 실제로 있다면, 
    # 여기에 추가하여 로드할 수 있습니다. 예: '/index.html': 'index.html'
}

def load_html_file(filename):
    """지정된 HTML 파일의 내용을 읽어와 반환합니다. 파일을 찾지 못하면 None을 반환합니다."""
    # 현재 작업 디렉토리에서 파일명을 찾습니다.
    file_path = os.path.join(os.getcwd(), filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
             return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None

# --- 기본 경로: 서비스 안내 ---
@app.route('/')
def index():
    """
    메인 인덱스 페이지. 현재 서비스 중인 항목들의 링크를 제공합니다.
    """
    links_html = ""
    for route, filename in FILE_MAPPINGS.items():
        # 사용자에게 파일명과 접근 경로를 함께 보여줍니다.
        links_html += f"""
        <li class="mb-2">
            <a href="{route}" class="text-lg text-indigo-600 hover:text-indigo-800 font-medium transition duration-150 underline">
                {filename} ({route})
            </a>
        </li>
        """

    # Tailwind 스타일을 사용한 깔끔한 서비스 안내 페이지
    return render_template_string(f"""
        <div style='padding: 50px; text-align: center; font-family: "Inter", sans-serif; background-color: #f0f4f8; border-radius: 12px; max-width: 600px; margin: 50px auto; box-shadow: 0 4px 12px rgba(0,0,0,0.1);'>
            <h1 style='color: #2563eb; font-size: 2.5rem; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;'>정보과제연구 통합 서비스</h1>
            <p style='color: #4b5563; font-size: 1.1rem; margin-top: 20px; margin-bottom: 30px;'>
                다음 프로젝트 파일들에 접근할 수 있습니다.
            </p>
            <ul style='list-style: none; padding: 0;'>
                {links_html}
            </ul>
        </div>
    """)

# --- 동적 경로 핸들러 ---
@app.route('/<path:filename>')
def serve_html_content(filename):
    """
    매핑된 경로의 HTML 파일을 로드하여 렌더링합니다.
    """
    # 요청 경로를 조합합니다. 예: 요청이 index4.html 이면 /index4.html
    requested_route = '/' + filename
    
    # FILE_MAPPINGS에 해당 경로가 정의되어 있는지 확인합니다.
    html_file_to_load = FILE_MAPPINGS.get(requested_route)
    
    if html_file_to_load:
        content = load_html_file(html_file_to_load)
        if content is not None:
            # 파일 내용을 Flask의 템플릿 엔진으로 렌더링
            return render_template_string(content)
        else:
            # 파일 로드 실패 (파일 없음 등의 오류) 시 404 반환
            return render_template_string(f"""
                <div style='padding: 50px; text-align: center; font-family: "Inter", sans-serif; color: #dc2626; background-color: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; max-width: 400px; margin: 50px auto;'>
                    <h2>파일을 찾을 수 없습니다 (404)</h2>
                    <p>요청 경로: <code>{requested_route}</code></p>
                    <p>시스템 파일명: <code>{html_file_to_load}</code></p>
                    <p>이 파일이 올바른 위치에 있는지 확인해 주세요.</p>
                </div>
            """), 404
    
    # 매핑되지 않은 다른 모든 경로에 대한 404 처리
    return render_template_string(f"""
        <div style='padding: 50px; text-align: center; font-family: "Inter", sans-serif; color: #dc2626; background-color: #fee2e2; border: 1px solid #fca5a5; border-radius: 8px; max-width: 400px; margin: 50px auto;'>
            <h2>페이지를 찾을 수 없습니다 (404)</h2>
            <p>요청된 경로: <code>{requested_route}</code></p>
            <p>유효하지 않은 서비스 경로입니다. <a href="/" style="color: #2563eb; text-decoration: underline;">메인 페이지로 돌아가기</a></p>
        </div>
    """), 404

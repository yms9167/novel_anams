from flask import Flask, render_template

# Flask 애플리케이션 초기화
# render_template 함수가 'templates' 폴더 내에서 HTML 파일을 찾습니다.
app = Flask(__name__)

# --- 웹 페이지 라우팅 설정 ---

# 1. 메인 페이지: index.html (AI 소설 연구)
# 루트 경로 ('/')와 '/research' 경로에서 접근 가능합니다.
@app.route('/')
@app.route('/research')
def novel_research():
    """
    index.html (AI 소설과 독자의 감정 연구) 파일을 렌더링합니다.
    """
    return render_template('index.html')

# 2. 팀 밸런스 분배기 페이지: index2.html
@app.route('/balancer')
def team_balancer():
    """
    index2.html (팀 밸런스 분배기) 파일을 렌더링합니다.
    """
    return render_template('index2.html')

# 3. 알고리즘 성능 비교기 페이지: index3.html
@app.route('/performance')
def algorithm_performance():
    """
    index3.html (알고리즘 성능 비교기) 파일을 렌더링합니다.
    """
    return render_template('index3.html')

# 4. 프로젝트 계획서 페이지: index4.html
@app.route('/plan')
def project_plan():
    """
    index4.html (정보과제연구 계획서) 파일을 렌더링합니다.
    """
    return render_template('index4.html')

# 스크립트를 직접 실행할 때 Flask 서버를 실행합니다.
if __name__ == '__main__':
    # Flask 서버를 0.0.0.0 호스트와 8080 포트에서 실행합니다.
    app.run(host='0.0.0.0', port=8080, debug=True)

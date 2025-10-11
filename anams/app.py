from flask import Flask, render_template

# Flask 애플리케이션 초기화 시 template_folder 경로를 'htmls'로 지정합니다.
# 이 설정 덕분에 Flask는 'anams/htmls' 폴더에서 HTML 파일을 찾을 수 있습니다.
app = Flask(__name__, template_folder='htmls')

# --- 웹 페이지 라우팅 설정 ---

# 1. 메인 페이지: index.html (AI 소설 연구)
# http://0.0.0.0:8080/ 또는 http://0.0.0.0:8080/research
@app.route('/')
@app.route('/research')
def novel_research():
    """
    index.html (AI 소설과 독자의 감정 연구) 파일을 렌더링합니다.
    """
    return render_template('index.html')

# 2. 팀 밸런스 분배기 페이지: index2.html
# http://0.0.0.0:8080/balancer
@app.route('/balancer')
def team_balancer():
    """
    index2.html (팀 밸런스 분배기) 파일을 렌더링합니다.
    """
    return render_template('index2.html')

# 3. 알고리즘 성능 비교기 페이지: index3.html
# http://0.0.0.0:8080/performance
@app.route('/performance')
def algorithm_performance():
    """
    index3.html (알고리즘 성능 비교기) 파일을 렌더링합니다.
    """
    return render_template('index3.html')

# 4. 프로젝트 계획서 페이지: index4.html
# http://0.0.0.0:8080/plan
@app.route('/plan')
def project_plan():
    """
    index4.html (정보과제연구 계획서) 파일을 렌더링합니다.
    """
    return render_template('index4.html')

# 스크립트를 직접 실행할 때 Flask 서버를 실행합니다.
if __name__ == '__main__':
    # Flask 서버를 0.0.0.0 호스트와 8080 포트에서 실행합니다.
    # debug=True 설정으로 코드를 수정할 때마다 자동으로 재시작됩니다.
    app.run(host='0.0.0.0', port=8080, debug=True)

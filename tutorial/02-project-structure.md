# 02. 프로젝트 소스코드 구조 및 설명

> **소요 시간**: 약 5분  
> **학습 목표**: 웹 스크래핑 대시보드의 코드 구조와 Browser Controls 최적화 이해

---

## 2. 프로젝트 소스코드 구조 및 설명

### 2.1 프로젝트 디렉토리 구조

```
browser_mcp/
├── app.py                 # Flask 백엔드 서버
├── requirements.txt       # Python 의존성 패키지
├── templates/
│   └── index.html        # 메인 페이지 HTML 템플릿
├── static/
│   ├── style.css         # CSS 스타일시트 (변수 기반)
│   └── script.js         # 클라이언트 사이드 JavaScript
├── tutorial/             # Tutorial 가이드 문서
│   ├── README.md
│   ├── 01-browser-mcp-overview.md
│   ├── 02-project-structure.md
│   └── 03-hands-on-exercises.md
└── README.md             # 프로젝트 문서
```

### 2.2 Backend 구조 (Flask)

#### **2.2.1 메인 애플리케이션 (app.py)**

**핵심 구성 요소**:

```python
# 주요 라이브러리
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
```

**주요 함수들**:

1. **`is_valid_url(url)`** - URL 유효성 검사
2. **`scrape_website(url)`** - 웹사이트 스크래핑 핵심 로직
3. **`index()`** - 메인 페이지 라우트
4. **`scrape()`** - 스크래핑 API 엔드포인트

#### **2.2.2 스크래핑 로직 상세 분석**

**데이터 추출 과정**:

```python
def scrape_website(url):
    # 1. HTTP 요청 (User-Agent 헤더 포함)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers, timeout=10)
    
    # 2. HTML 파싱 (BeautifulSoup)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 3. 기본 정보 추출
    title = soup.find('title').get_text().strip()
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    
    # 4. 링크 추출 (최대 10개)
    links = []
    for link in soup.find_all('a', href=True)[:10]:
        # 상대 URL을 절대 URL로 변환
        href = convert_to_absolute_url(link.get('href'), url)
        links.append({'url': href, 'text': link.get_text().strip()})
    
    # 5. 이미지 추출 (최대 5개)
    images = []
    for img in soup.find_all('img', src=True)[:5]:
        src = convert_to_absolute_url(img.get('src'), url)
        images.append({'src': src, 'alt': img.get('alt', '이미지')})
```

**에러 처리 메커니즘**:

```python
try:
    # 스크래핑 로직
    return {'success': True, 'data': {...}}
except requests.exceptions.Timeout:
    return {'success': False, 'error': '요청 시간 초과 (10초)'}
except requests.exceptions.ConnectionError:
    return {'success': False, 'error': '연결 오류 - URL을 확인해주세요'}
except requests.exceptions.HTTPError as e:
    return {'success': False, 'error': f'HTTP 오류: {e.response.status_code}'}
except Exception as e:
    return {'success': False, 'error': f'스크래핑 오류: {str(e)}'}
```

#### **2.2.3 API 엔드포인트**

**GET `/`** - 메인 페이지
```python
@app.route('/')
def index():
    return render_template('index.html')
```

**POST `/scrape`** - 스크래핑 API
```python
@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url', '').strip()
    
    # URL 유효성 검사
    if not is_valid_url(url):
        return jsonify({'success': False, 'error': '올바른 URL 형식이 아닙니다'})
    
    # https:// 자동 추가
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    result = scrape_website(url)
    return jsonify(result)
```

#### **2.2.4 의존성 관리 (requirements.txt)**

```txt
Flask==2.3.3          # 웹 프레임워크
requests==2.31.0       # HTTP 요청 라이브러리
beautifulsoup4==4.12.2 # HTML 파싱 라이브러리
```

### 2.3 Frontend 구조

#### **2.3.1 HTML 템플릿 (templates/index.html)**

**페이지 구조**:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>웹 스크래핑 대시보드 - Browser Controls 실습</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>🌐 웹 스크래핑 대시보드</h1>
            <p>Cursor Browser Controls 실습을 위한 간단한 웹 스크래핑 도구</p>
        </header>

        <main class="main-content">
            <section class="input-section">
                <!-- URL 입력 폼 -->
            </section>
            <section class="results-section" id="resultsSection">
                <!-- 스크래핑 결과 표시 -->
            </section>
            <section class="error-section" id="errorSection">
                <!-- 에러 메시지 표시 -->
            </section>
        </main>

        <footer class="footer">
            <!-- Browser Controls 실습 팁 -->
        </footer>
    </div>
</body>
</html>
```

**핵심 HTML 요소들**:

| 요소 | ID/Class | 역할 |
|------|----------|------|
| URL 입력 필드 | `#urlInput` | 사용자가 스크래핑할 URL 입력 |
| 스크래핑 버튼 | `#scrapeBtn` | 스크래핑 시작 버튼 |
| 결과 영역 | `#resultsSection` | 스크래핑 결과 표시 |
| 에러 영역 | `#errorSection` | 에러 메시지 표시 |
| 폼 | `#scrapeForm` | 전체 폼 컨테이너 |

#### **2.3.2 CSS 스타일시트 (static/style.css)**

**CSS 변수 시스템**:

```css
:root {
    --primary-color: #3b82f6;        /* 메인 색상 */
    --primary-hover: #2563eb;        /* 호버 색상 */
    --background-color: #f8fafc;     /* 배경 색상 */
    --card-background: #ffffff;      /* 카드 배경 */
    --text-primary: #1f2937;         /* 주요 텍스트 */
    --text-secondary: #6b7280;       /* 보조 텍스트 */
    --border-radius: 8px;            /* 모서리 둥글기 */
    --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);  /* 그림자 */
}
```

**주요 CSS 클래스**:

| 클래스 | 역할 | Browser Controls 활용 |
|--------|------|---------------------|
| `.header` | 페이지 헤더 | 색상, 그라데이션 변경 |
| `.scrape-btn` | 스크래핑 버튼 | 크기, 색상, 애니메이션 |
| `.result-card` | 결과 카드 | 레이아웃, 스타일 변경 |
| `.error-message` | 에러 메시지 | 아이콘, 색상 변경 |
| `.info-table` | 결과 테이블 | 스타일, 간격 조정 |

#### **2.3.3 JavaScript 로직 (static/script.js)**

**주요 함수들**:

```javascript
// 1. 폼 제출 처리
scrapeForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = urlInput.value.trim();
    
    // AJAX 요청
    const response = await fetch('/scrape', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: url })
    });
    
    const data = await response.json();
    if (data.success) {
        showResults(data.data);
    } else {
        showError(data.error);
    }
});

// 2. 결과 표시
function showResults(data) {
    resultsContent.innerHTML = generateResultsHTML(data);
    resultsSection.style.display = 'block';
}

// 3. 에러 표시
function showError(message) {
    errorText.textContent = message;
    errorSection.style.display = 'block';
}

// 4. 로딩 상태 관리
function setLoadingState(isLoading) {
    scrapeBtn.disabled = isLoading;
    btnText.style.display = isLoading ? 'none' : 'inline-block';
    btnLoading.style.display = isLoading ? 'inline-block' : 'none';
}
```

### 2.4 데이터 흐름 다이어그램

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   사용자 입력    │    │   Frontend      │    │   Backend       │
│                 │    │   (JavaScript)  │    │   (Flask)       │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          │ 1. URL 입력          │                      │
          ├─────────────────────►│                      │
          │                      │                      │
          │                      │ 2. AJAX POST /scrape │
          │                      ├─────────────────────►│
          │                      │                      │
          │                      │                      │ 3. URL 검증
          │                      │                      ├─────────┐
          │                      │                      │         │
          │                      │                      │ 4. 스크래핑
          │                      │                      ├─────────┐
          │                      │                      │         │
          │                      │ 5. JSON 응답         │         │
          │                      │◄─────────────────────┤         │
          │                      │                      │         │
          │ 6. 결과 표시         │                      │         │
          │◄─────────────────────┤                      │         │
          │                      │                      │         │
          │ 7. 에러 처리         │                      │         │
          │◄─────────────────────┤                      │         │
```

### 2.5 Browser Controls 최적화 설계

#### **2.5.1 CSS 변수 활용**

**장점**: Browser Controls에서 실시간 색상 변경 가능
```css
/* 변경 전 */
.header { background: #3b82f6; }

/* Browser Controls로 변경 후 */
.header { background: var(--primary-color); }
```

#### **2.5.2 명확한 ID/Class 네이밍**

**장점**: Browser Controls에서 요소 선택 용이
```html
<!-- 명확한 ID 사용 -->
<input id="urlInput" type="url">
<button id="scrapeBtn" class="scrape-btn">
<div id="resultsSection" class="results-section">
```

#### **2.5.3 구조화된 HTML**

**장점**: Browser Controls에서 섹션별 수정 가능
```html
<main class="main-content">
    <section class="input-section">...</section>
    <section class="results-section">...</section>
    <section class="error-section">...</section>
</main>
```

### 2.6 프로젝트 특징 요약

| 특징 | 설명 | Browser Controls 활용도 |
|------|------|----------------------|
| **단순한 구조** | Flask + HTML/CSS/JS | ⭐⭐⭐⭐⭐ |
| **CSS 변수** | 실시간 색상 변경 | ⭐⭐⭐⭐⭐ |
| **명확한 ID** | 요소 선택 용이 | ⭐⭐⭐⭐⭐ |
| **AJAX 통신** | 비동기 데이터 처리 | ⭐⭐⭐⭐ |
| **에러 처리** | 다양한 시나리오 | ⭐⭐⭐⭐ |
| **반응형 디자인** | 모바일 대응 | ⭐⭐⭐ |

**핵심 메시지**:
> "이 프로젝트는 Browser Controls 실습에 최적화되어 있습니다. CSS 변수, 명확한 HTML 구조, AJAX 통신을 통해 실시간으로 웹페이지를 수정하고 테스트할 수 있습니다!"

---

**다음 단계**: [03. Browser Controls 실습](03-hands-on-exercises.md)으로 이동하세요!

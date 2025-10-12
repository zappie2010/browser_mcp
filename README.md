# 🌐 웹 스크래핑 대시보드 - Browser Controls 실습

Cursor의 Browser Controls 기능을 실습하기 위한 간단한 웹 스크래핑 대시보드 프로젝트입니다.

## 📋 프로젝트 개요

이 프로젝트는 Python Flask를 사용하여 간단한 웹 스크래핑 도구를 만들고, Cursor의 Browser Controls 기능을 통해 웹 개발 및 디버깅을 실습할 수 있도록 설계되었습니다.

## 🚀 빠른 시작

### 1. 환경 설정
```bash
# Python 가상환경 생성 및 활성화
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt
```

### 2. 서버 실행
```bash
python app.py
```
브라우저에서 `http://localhost:5000`으로 접속하세요.

### 3. Browser Controls 활성화
1. Cursor Settings → Beta → "Cursor Browser" 활성화
2. Chat에서 "+Browser" 버튼 클릭
3. `브라우저 기능을 사용해서 google.com에 접속해줘` 테스트

> **상세 가이드**: [Tutorial 사전 준비 사항](tutorial/00-prerequisites.md) 참고

## 📚 Tutorial 및 실습

이 프로젝트는 **Cursor Browser Controls Tutorial**을 위한 교육용 프로젝트입니다.

### 🎯 Tutorial 개요
- **소요 시간**: 약 40분
- **난이도**: 초급~중급
- **대상**: Python 개발자 (웹 개발 지식 불필요)

### 📋 실습 내용
1. **CSS 스타일 변경** - 실시간 색상 및 레이아웃 수정
2. **링크 필터링 기능** - 검색 기능 추가
3. **로딩 애니메이션** - 사용자 경험 개선
4. **에러 처리 개선** - 더 나은 에러 메시지
5. **데이터 내보내기** - JSON 파일 다운로드
6. **다크모드 추가** - CSS 변수 활용

> **전체 Tutorial**: [tutorial/README.md](tutorial/README.md)에서 상세한 가이드를 확인하세요!

## 🛠️ 기술 스택

- **Backend**: Python 3.8+, Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **스크래핑**: BeautifulSoup4, Requests
- **개발 도구**: Cursor Browser Controls

## 📁 프로젝트 구조

```
browser_mcp/
├── app.py                 # Flask 애플리케이션
├── requirements.txt       # Python 의존성
├── templates/
│   └── index.html        # 메인 페이지 템플릿
├── static/
│   ├── style.css         # CSS 스타일
│   └── script.js         # JavaScript 로직
└── README.md             # 프로젝트 문서
```

## 🎨 주요 기능

### 웹 스크래핑 기능
- URL 유효성 검사
- 웹페이지 기본 정보 추출 (제목, 설명, 상태 코드)
- 링크 목록 추출 (최대 10개)
- 이미지 목록 추출 (최대 5개)
- 에러 처리 및 사용자 피드백

### 사용자 인터페이스
- 반응형 디자인
- 실시간 로딩 상태 표시
- 직관적인 결과 표시
- 에러 메시지 표시

### Browser Controls 최적화
- CSS 변수 사용으로 쉬운 스타일 수정
- 명확한 클래스명과 ID
- 구조화된 HTML 마크업
- 디버깅 친화적인 코드 구조

## 🔧 커스터마이징

### CSS 변수 수정
`static/style.css` 파일의 `:root` 섹션에서 색상, 간격, 폰트 등을 쉽게 수정할 수 있습니다.

### 스크래핑 로직 수정
`app.py` 파일의 `scrape_website()` 함수에서 추출할 데이터를 수정할 수 있습니다.

### UI 컴포넌트 추가
`templates/index.html`에서 새로운 섹션이나 컴포넌트를 추가할 수 있습니다.

## 🐛 문제 해결

### 자주 발생하는 문제
- **서버 시작 실패**: Python 3.8+ 확인, 가상환경 활성화 확인
- **스크래핑 실패**: 인터넷 연결, 대상 사이트 접근 가능성 확인
- **Browser Controls 미작동**: Cursor 0.45.0+ 확인, "+Browser" 버튼 활성화

> **상세 트러블슈팅**: [tutorial/troubleshooting.md](tutorial/troubleshooting.md) 참고

## 📚 학습 자료

### Tutorial 가이드
- **[Tutorial 개요](tutorial/README.md)** - 전체 가이드 및 진행 순서
- **[사전 준비 사항](tutorial/00-prerequisites.md)** - 상세 설치 가이드
- **[Browser MCP 개요](tutorial/01-browser-mcp-overview.md)** - 개념 및 동작 원리
- **[프로젝트 구조](tutorial/02-project-structure.md)** - 코드 구조 설명
- **[실습 과제](tutorial/03-hands-on-exercises.md)** - 6개 실습 시나리오
- **[트러블슈팅](tutorial/troubleshooting.md)** - 문제 해결 가이드

### 공식 문서
- [Cursor Browser Controls 공식 문서](https://cursor.sh/docs)
- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [BeautifulSoup4 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## 🤝 기여하기

이 프로젝트는 Browser Controls 실습을 위한 교육용 프로젝트입니다. 개선 사항이나 버그 리포트는 언제든 환영합니다!

---

**💡 팁**: Browser Controls를 사용할 때는 작은 변경사항부터 시작하여 점진적으로 복잡한 수정을 시도해보세요. 실시간으로 변경사항을 확인할 수 있어 매우 직관적입니다!

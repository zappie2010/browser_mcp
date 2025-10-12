# Browser Controls Tutorial

> 웹 스크래핑 대시보드 프로젝트를 활용한 Cursor Browser Controls 실습 튜토리얼

## 📖 Tutorial 개요

**소요 시간**: 약 40분  
**난이도**: 초급~중급  
**대상**: Python 개발자 (웹 개발 지식 불필요)

## 🎯 세미나 진행 순서 (총 40분)

### **세미나 전: 사전 준비** (참석자 개별 진행)
- ⏰ **소요 시간**: 10-15분
- 📋 **준비 사항**:
  - Python 3.8+ 설치
  - Cursor IDE 0.45.0+ 설치
  - 프로젝트 다운로드 및 셋업
  - 서버 실행 테스트
- 📄 **문서**: [00. 사전 준비 사항](00-prerequisites.md)

### **1단계: 개요 설명** (5분)
- 🎤 **진행 방식**: 발표자 설명
- 📚 **내용**:
  - Browser MCP 개념 소개
  - Cursor Browser Controls 동작 원리
  - 주요 기능 및 장점
- 📄 **문서**: [01. Browser MCP 개요](01-browser-mcp-overview.md)

### **2단계: 프로젝트 구조** (5분)
- 🎤 **진행 방식**: 코드 함께 살펴보기
- 📚 **내용**:
  - 디렉토리 구조 설명
  - Backend (Flask) 주요 코드
  - Frontend (HTML/CSS/JS) 구조
- 📄 **문서**: [02. 프로젝트 구조](02-project-structure.md)

### **3단계: 실습** (30분)
- 🎤 **진행 방식**: 참석자 직접 실습
- 📚 **내용**:
  - 실습 1: CSS 스타일 변경 (5분)
  - 실습 2: 링크 필터링 기능 (7분)
  - 실습 3: 로딩 애니메이션 (5분)
  - 실습 4: 에러 처리 개선 (5분)
  - 실습 5: 데이터 내보내기 (5분)
  - 실습 6: 다크모드 추가 (8분)
- 📄 **문서**: [03. 실습 과제](03-hands-on-exercises.md)

---

## 📋 상세 목차

### [00. 사전 준비 사항](00-prerequisites.md) (세미나 전)
- 필수 설치 항목 (Python, Cursor IDE)
- 프로젝트 셋업 가이드
- 설치 확인 체크리스트
- 트러블슈팅

### [01. Browser MCP 개요 및 Cursor Browser Controls 설명](01-browser-mcp-overview.md) (5분)
- MCP (Model Context Protocol) 소개
- Browser MCP란?
- Cursor Browser Controls 동작 원리
- 주요 기능 및 장점
- Playwright MCP와의 비교
- 지원 버전

### [02. 프로젝트 소스코드 구조 및 설명](02-project-structure.md) (5분)
- 프로젝트 디렉토리 구조
- Backend (Flask) 구조
- Frontend (HTML/CSS/JS) 구조
- 데이터 흐름
- Browser Controls 최적화 설계

### [03. Browser Controls 실습](03-hands-on-exercises.md) (30분)
- 실습 1: CSS 스타일 변경
- 실습 2: 링크 필터링 기능 추가
- 실습 3: 로딩 애니메이션 개선
- 실습 4: 에러 처리 개선
- 실습 5: 결과 데이터 내보내기
- 실습 6: 다크모드 추가

## 🚀 빠른 시작

### ⚠️ 중요: 세미나 전에 준비하세요!

Tutorial을 원활하게 진행하려면 **세미나 시작 전에** 다음 사항을 완료해야 합니다:

1. ✅ **Python 3.8+ 설치**
2. ✅ **Cursor IDE 0.45.0+ 설치**
3. ✅ **프로젝트 다운로드 및 패키지 설치**
4. ✅ **서버 실행 테스트**

**상세 가이드**: [00. 사전 준비 사항](00-prerequisites.md)을 참고하세요!

### 간단 셋업 가이드

```bash
# 1. 프로젝트 다운로드
git clone <repository-url>
cd browser_mcp

# 2. 가상환경 생성 및 활성화
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 서버 실행
python app.py

# 5. 브라우저에서 확인
# http://localhost:5000
```

**문제가 발생하나요?** [트러블슈팅 가이드](00-prerequisites.md#-자주-발생하는-문제)를 확인하세요!

## 📁 Tutorial 파일 구조

```
tutorial/
├── README.md                     # Tutorial 개요 (현재 파일)
├── 01-browser-mcp-overview.md    # Section 1: Browser MCP 개요
├── 02-project-structure.md       # Section 2: 프로젝트 구조
├── 03-hands-on-exercises.md      # Section 3: 실습 과제
└── assets/                       # 이미지, 스크린샷 등
```

## 💡 Tutorial 진행 방법

1. **순서대로 진행**: 01 → 02 → 03 순서로 학습
2. **직접 실습**: 각 섹션의 예제 코드를 직접 따라해보기
3. **Browser Controls 활용**: Cursor Chat에 자연어 명령으로 수정 요청
4. **결과 확인**: 브라우저에서 실시간으로 변경사항 확인

## 🎯 학습 목표

이 Tutorial을 완료하면 다음을 할 수 있습니다:

- ✅ Cursor Browser Controls의 개념과 동작 원리 이해
- ✅ 자연어 명령으로 웹페이지 수정
- ✅ CSS 스타일을 실시간으로 변경
- ✅ JavaScript 기능을 추가 및 수정
- ✅ 브라우저에서 자동으로 테스트 실행
- ✅ 네트워크 요청 디버깅

## 🆘 문제 해결

Tutorial 진행 중 문제가 발생했나요?

- 📄 **[트러블슈팅 가이드](troubleshooting.md)**: 자주 발생하는 문제와 해결 방법
- 📄 **[사전 준비 FAQ](00-prerequisites.md#-자주-발생하는-문제)**: 설치 및 환경 설정 문제
- 🙋 **세미나 중**: 손을 들어 발표자에게 질문하세요!

## 🔗 추가 자료

- [Cursor 공식 문서](https://cursor.sh/docs)
- [Playwright 문서](https://playwright.dev)
- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [BeautifulSoup4 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python 공식 문서](https://docs.python.org/ko/3/)

## 📞 문의 및 피드백

Tutorial 진행 중 문제가 발생하거나 개선 제안이 있으시면:
- 세미나 중: 발표자에게 직접 질문
- 세미나 후: 이슈를 등록하거나 피드백 제출

---

**시작 준비가 되셨나요?** [01. Browser MCP 개요](01-browser-mcp-overview.md)부터 시작하세요! 🚀


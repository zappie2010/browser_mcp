# 00. 사전 준비 사항

> **소요 시간**: 약 10-15분  

---

## 📋 필수 설치 항목

### 1. Python 3.8 이상
- [ ] Python 설치 완료
- [ ] 버전 확인: `python --version` 또는 `python3 --version`
- [ ] 예상 출력: `Python 3.8.x` 이상

**다운로드**:
- Windows: https://www.python.org/downloads/
- macOS: `brew install python3` 또는 https://www.python.org/downloads/
- Linux: `sudo apt install python3` (Ubuntu/Debian)

### 2. Cursor IDE 0.45.0 이상
- [ ] Cursor IDE 설치 완료
- [ ] 버전 확인: `Help` → `About Cursor`
- [ ] Browser Controls 기능 확인

**다운로드**:
- https://cursor.sh/

**Browser Controls 활성화 방법**:

**1단계: Cursor Settings에서 활성화**
1. `Ctrl + ,` (Windows/Linux) 또는 `Cmd + ,` (Mac)
2. 또는 `File` → `Preferences` → `Settings`
3. 왼쪽 메뉴에서 **"Beta"** 클릭
4. **"Cursor Browser"** 옵션을 **활성화** (체크박스 선택)

**2단계: Chat에서 Browser 기능 활성화**
1. Cursor Chat 열기
2. 채팅창에서 **"+Browser"** 버튼 클릭
3. Browser 기능이 활성화되면 ✅

**3단계: 기능 확인**
1. 다음 명령 입력: `브라우저 기능을 사용해서 google.com에 접속해줘`
2. AI가 브라우저를 열고 Google에 접속하면 ✅

**참고**: Cursor 버전 0.45.0 이상 필요

### 3. Git (선택사항)
- [ ] Git 설치 완료 (프로젝트 다운로드용)
- [ ] 버전 확인: `git --version`

**다운로드**:
- https://git-scm.com/downloads

또는 ZIP 파일로 직접 다운로드 가능합니다.

---

## 🚀 프로젝트 셋업

### 1단계: 프로젝트 다운로드

**옵션 A: Git 사용**
```bash
git clone <repository-url>
cd browser_mcp
```

**옵션 B: ZIP 다운로드**
1. 프로젝트 ZIP 파일 다운로드
2. 압축 해제
3. 터미널에서 폴더로 이동

### 2단계: 가상환경 생성 (권장)

**Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
```

✅ **가상환경 활성화 확인**:
- 터미널 프롬프트 앞에 `(venv)` 표시됨

### 3단계: 패키지 설치

```bash
pip install -r requirements.txt
```

**예상 출력**:
```
Successfully installed Flask-2.3.3 requests-2.31.0 beautifulsoup4-4.12.2 ...
```

### 4단계: 서버 실행 테스트

```bash
python app.py
```

**예상 출력**:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### 5단계: 브라우저 확인

1. 브라우저에서 `http://localhost:5000` 접속
2. "🌐 웹 스크래핑 대시보드" 페이지가 보이면 ✅

---

## ✅ 설치 확인 체크리스트

### 필수 항목
- [ ] Python 3.8+ 설치 및 버전 확인
- [ ] Cursor IDE 0.45.0+ 설치
- [ ] Browser Controls 기능 확인
- [ ] 프로젝트 다운로드 완료
- [ ] 가상환경 생성 및 활성화
- [ ] `pip install -r requirements.txt` 성공
- [ ] `python app.py` 실행 성공
- [ ] 브라우저에서 `http://localhost:5000` 접속 확인

### 선택 항목
- [ ] Git 설치

---

## 🆘 자주 발생하는 문제

### 문제 1: Python 버전이 3.8 미만입니다

**증상**:
```
Python 3.7.x
```

**해결**:
- Python 최신 버전을 다시 설치하세요
- 여러 Python 버전이 설치된 경우 `python3` 명령어 사용

### 문제 2: pip 명령어를 찾을 수 없습니다

**증상**:
```
'pip' is not recognized as an internal or external command
```

**해결**:
```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
python3 -m pip install -r requirements.txt
```

### 문제 3: 패키지 설치 중 오류 발생

**증상**:
```
ERROR: Could not build wheels for ...
```

**해결**:
```bash
# pip 업그레이드
pip install --upgrade pip

# 다시 시도
pip install -r requirements.txt
```

### 문제 4: 포트 5000이 이미 사용 중입니다

**증상**:
```
Address already in use
```

**해결 A: 포트를 사용 중인 프로세스 종료**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID번호> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

**해결 B: 다른 포트 사용**
`app.py` 파일 마지막 줄 수정:
```python
# 기존
app.run(debug=True, host='0.0.0.0')

# 변경 (포트 8000 사용)
app.run(debug=True, host='0.0.0.0', port=8000)
```

### 문제 5: Browser Controls가 보이지 않습니다

**증상**:
- `Ctrl + Shift + P` → "Browser" 검색 시 "Open Browser" 명령이 없음

**해결**:
1. Cursor 버전 확인 (0.45.0 이상 필요)
2. Cursor 재시작
3. Cursor 업데이트: `Help` → `Check for Updates`

### 문제 6: 가상환경이 활성화되지 않습니다

**증상**:
- 터미널에 `(venv)` 표시가 없음

**해결**:
```bash
# Windows (PowerShell)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate
```

---

## 📞 추가 도움이 필요하신가요?

### 문서 참고
- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [Cursor 공식 문서](https://cursor.sh/docs)
- [Python 가상환경 가이드](https://docs.python.org/ko/3/tutorial/venv.html)

### Tutorial 중 문제 발생 시
- 발표자에게 손을 들어 질문하세요
- 옆 참석자에게 도움을 요청하세요

---

## 🎉 준비 완료!

모든 체크리스트를 완료하셨나요? 축하합니다! 

이제 Tutorial을 시작할 준비가 되었습니다! 🚀

**다음 단계**: [Tutorial 개요](README.md)로 이동하세요!


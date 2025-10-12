# 🆘 트러블슈팅 가이드

> Tutorial 진행 중 발생할 수 있는 문제와 해결 방법

---

## 📋 목차

1. [환경 설정 문제](#1-환경-설정-문제)
2. [서버 실행 문제](#2-서버-실행-문제)
3. [Browser Controls 문제](#3-browser-controls-문제)
4. [실습 중 문제](#4-실습-중-문제)
5. [일반적인 Python 문제](#5-일반적인-python-문제)

---

## 1. 환경 설정 문제

### 1.1 Python이 설치되지 않았습니다

**증상**:
```bash
'python' is not recognized as an internal or external command
```

**해결**:
1. Python 공식 사이트에서 다운로드: https://www.python.org/downloads/
2. 설치 시 "Add Python to PATH" 체크박스 선택
3. 터미널 재시작
4. `python --version` 또는 `python3 --version`으로 확인

### 1.2 Python 버전이 너무 낮습니다

**증상**:
```bash
Python 3.7.x
```

**해결**:
- Python 3.8 이상으로 업그레이드
- 여러 버전이 설치된 경우: `python3.8` 또는 `python3.9` 명령어 사용

### 1.3 pip가 작동하지 않습니다

**증상**:
```bash
'pip' is not recognized
```

**해결**:
```bash
# Python 모듈로 직접 실행
python -m pip install -r requirements.txt

# 또는
python3 -m pip install -r requirements.txt
```

### 1.4 가상환경 활성화가 안 됩니다 (Windows)

**증상**:
```powershell
cannot be loaded because running scripts is disabled
```

**해결**:
```powershell
# PowerShell을 관리자 권한으로 실행
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 다시 시도
venv\Scripts\Activate.ps1
```

---

## 2. 서버 실행 문제

### 2.1 포트 5000이 이미 사용 중입니다

**증상**:
```
Address already in use
Port 5000 is in use by another program
```

**해결 A: 포트를 사용 중인 프로세스 종료**

**Windows**:
```bash
# 포트 5000 사용 프로세스 찾기
netstat -ano | findstr :5000

# 프로세스 종료 (PID 번호 확인 후)
taskkill /PID <PID번호> /F
```

**macOS/Linux**:
```bash
# 포트 5000 사용 프로세스 종료
lsof -ti:5000 | xargs kill -9
```

**해결 B: 다른 포트 사용**

`app.py` 파일 수정:
```python
# 마지막 줄 변경
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)  # 포트 8000 사용
```

그리고 `http://localhost:8000`으로 접속

### 2.2 모듈을 찾을 수 없습니다

**증상**:
```python
ModuleNotFoundError: No module named 'flask'
```

**해결**:
```bash
# 가상환경이 활성화되어 있는지 확인
# 터미널에 (venv) 표시가 있어야 함

# 패키지 재설치
pip install -r requirements.txt

# 또는 개별 설치
pip install Flask requests beautifulsoup4
```

### 2.3 서버가 실행되지만 페이지가 열리지 않습니다

**증상**:
- 서버는 실행됨
- 브라우저에서 "사이트에 연결할 수 없음"

**해결**:
1. 서버 로그 확인:
   ```
   * Running on http://127.0.0.1:5000
   ```
2. 올바른 URL 사용:
   - `http://localhost:5000` 또는
   - `http://127.0.0.1:5000`
3. 방화벽 확인 (필요시 5000 포트 허용)

---

## 3. Browser Controls 문제

### 3.1 Browser Controls가 작동하지 않습니다

**증상**:
- Chat에서 브라우저 명령 시 응답 없음
- "+Browser" 버튼이 보이지 않음

**해결**:
1. **Settings에서 Cursor Browser 활성화**:
   - `Ctrl + ,` (Windows/Linux) 또는 `Cmd + ,` (Mac)
   - `Settings` → `Beta` 메뉴
   - **"Cursor Browser"** 옵션이 활성화되어 있는지 확인
   - 비활성화되어 있다면 체크박스 선택

2. **Chat에서 Browser 기능 활성화**:
   - Cursor Chat 열기
   - 채팅창에서 **"+Browser"** 버튼 클릭
   - Browser 기능이 활성화되면 ✅

3. **Cursor 버전 확인**:
   - `Help` → `About Cursor`
   - 0.45.0 이상 필요
   - 0.45.0 미만이면 업데이트: `Help` → `Check for Updates`

4. **기능 테스트**:
   ```
   브라우저 기능을 사용해서 google.com에 접속해줘
   ```

### 3.2 브라우저가 열리지 않습니다

**증상**:
- "브라우저를 열어줘" 명령 시 아무 반응 없음

**해결**:
1. Chat에서 명확한 명령:
   ```
   브라우저를 열어서 http://localhost:5000에 접속해줘
   ```
2. 서버가 실행 중인지 확인
3. Cursor 재시작

### 3.3 브라우저가 페이지를 로드하지 못합니다

**증상**:
- 브라우저는 열리지만 페이지가 표시되지 않음

**해결**:
1. 서버 실행 확인: `python app.py`
2. 터미널에서 수동 테스트:
   ```bash
   curl http://localhost:5000
   ```
3. 다른 브라우저에서 직접 접속 시도

---

## 4. 실습 중 문제

### 4.1 CSS 변경이 적용되지 않습니다

**증상**:
- CSS 파일을 수정했는데 브라우저에 반영 안 됨

**해결**:
1. **브라우저 캐시 삭제**:
   - `Ctrl + Shift + R` (Windows/Linux)
   - `Cmd + Shift + R` (Mac)
2. **서버 재시작**:
   - `Ctrl + C`로 서버 중지
   - `python app.py`로 재시작
3. **개발자 도구에서 확인**:
   - F12 → Network → Disable cache 체크

### 4.2 JavaScript 오류가 발생합니다

**증상**:
- 브라우저 콘솔에 에러 메시지

**해결**:
1. **F12**로 개발자 도구 열기
2. **Console** 탭에서 에러 메시지 확인
3. 오타나 문법 오류 수정
4. 파일 저장 후 페이지 새로고침

### 4.3 스크래핑이 작동하지 않습니다

**증상**:
- URL 입력 후 "연결 오류" 발생

**해결**:
1. **유효한 URL 입력**:
   - `https://example.com` (올바름)
   - `example` (잘못됨)
2. **인터넷 연결 확인**
3. **대상 사이트 확인**:
   - 일부 사이트는 스크래핑 차단
   - `https://example.com` 같은 테스트 사이트 사용

### 4.4 에러 메시지: CORS 오류

**증상**:
```
Access to fetch at '...' has been blocked by CORS policy
```

**해결**:
- 이 프로젝트는 Flask 서버를 사용하므로 CORS 문제가 없어야 함
- 만약 발생하면 `app.py`에 CORS 허용 추가:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 추가
```

그리고 설치:
```bash
pip install flask-cors
```

---

## 5. 일반적인 Python 문제

### 5.1 SyntaxError 발생

**증상**:
```python
SyntaxError: invalid syntax
```

**해결**:
1. 에러 메시지에서 파일과 줄 번호 확인
2. 해당 줄의 문법 오류 수정:
   - 괄호 짝 맞추기
   - 따옴표 확인
   - 콜론(:) 확인
   - 들여쓰기 확인

### 5.2 IndentationError 발생

**증상**:
```python
IndentationError: unexpected indent
```

**해결**:
- Python은 들여쓰기를 중요하게 다룸
- 스페이스 4개 또는 탭 1개로 일관성 유지
- 혼용하지 말 것

### 5.3 NameError 발생

**증상**:
```python
NameError: name 'variable_name' is not defined
```

**해결**:
1. 변수명 오타 확인
2. 변수가 정의된 후에 사용하는지 확인
3. import 누락 확인

---

## 6. Cursor 특정 문제

### 6.1 AI가 응답하지 않습니다

**증상**:
- Chat에 메시지를 보냈지만 응답 없음

**해결**:
1. 인터넷 연결 확인
2. Cursor 계정 로그인 확인
3. API 키 또는 크레딧 확인
4. Cursor 재시작

### 6.2 코드 변경이 자동 저장되지 않습니다

**증상**:
- AI가 코드를 수정했지만 파일에 반영 안 됨

**해결**:
1. `Ctrl + S`로 수동 저장
2. Cursor 설정에서 Auto Save 활성화:
   - `File` → `Preferences` → `Settings`
   - "Auto Save" 검색
   - "afterDelay"로 설정

---

## 7. 긴급 상황 대처

### 모든 것이 작동하지 않을 때

**최후의 수단**:

1. **프로젝트 재다운로드**:
   ```bash
   cd ..
   rm -rf browser_mcp
   git clone <repository-url>
   cd browser_mcp
   ```

2. **가상환경 재생성**:
   ```bash
   # 기존 가상환경 삭제
   rm -rf venv  # Windows: rmdir /s venv
   
   # 새로 생성
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   
   pip install -r requirements.txt
   ```

3. **Cursor 재설치**:
   - Cursor 완전 삭제
   - https://cursor.sh 에서 최신 버전 다운로드
   - 재설치

4. **다른 컴퓨터에서 시도**:
   - 가능하다면 다른 환경에서 테스트

---

## 8. 도움 요청하기

### Tutorial 중 도움이 필요할 때

1. **손을 들어 발표자에게 알리기**
2. **옆 참석자에게 도움 요청**
3. **에러 메시지 캡처**:
   - 스크린샷
   - 전체 에러 메시지 복사

### 문제 보고 시 포함할 정보

```
- OS: Windows 10 / macOS 13 / Ubuntu 22.04
- Python 버전: python --version 결과
- Cursor 버전: Help → About Cursor
- 에러 메시지: (전체 복사)
- 시도한 해결 방법: (무엇을 해봤는지)
```

---

## 📞 추가 리소스

- [Python 공식 문서](https://docs.python.org/ko/3/)
- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [Cursor 공식 문서](https://cursor.sh/docs)
- [Stack Overflow](https://stackoverflow.com/)

---

**문제가 해결되었나요?** [Tutorial로 돌아가기](README.md) 🚀


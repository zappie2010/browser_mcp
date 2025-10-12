Cursor 1.7 업데이트 내역
Browser Controls, Plan Mode, and Hooks

Browser Controls
- 커서가 브라우저 컨트롤 할 수 있음
- 기존에는 브라우저 자동화 기능
  - Playwrght (https://playwright.dev/) MCP 를 agent 에 붙여서 사용
    - https://www.dawnscapelab.com/the-core-concepts-of-playwright/
    - https://goddaehee.tistory.com/392
    - https://skywork.ai/skypage/ko/Playwright%20MCP%20%EC%84%9C%EB%B2%84%20%EC%99%84%EB%B2%BD%20%EA%B0%80%EC%9D%B4%EB%93%9C%3A%20AI%20%EA%B8%B0%EB%B0%98%20%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%20%EC%9E%90%EB%8F%99%ED%99%94%EC%9D%98%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%EC%8B%9C%EB%8C%80/1972521566375440384
    - Playwright는 Microsoft 에서 개발하고 2020년 1월 31일에 출시한 브라우저 테스트 및 웹 스크래핑을 위한 오픈 소스 자동화 라이브러리 입니다.
    - Playwright는 단일 API를 사용하여 Chromium , Firefox 및 WebKit 에서 브라우저 작업을 자동화하는 기능을 제공합니다.
  - chrome-devtools-mcp (https://github.com/benjaminr/chrome-devtools-mcp)
    - https://developer.chrome.com/blog/chrome-devtools-mcp?hl=ko

- 커서에서 제공하는 기능
  - 내부적으로는 Playwright MCP 를 사용하는것으로 보임
  - https://cursor.com/docs/agent/browser#browser-capabilities



Autocomplete for Agent
- 채팅창에서 자동완성 기능이 추가됨

Hooks (beta)
- 에이전트에 특정 이벤트와 연계하여 특정 동작 실행
- https://cursor.com/docs/agent/hooks#hook-events
- (예) 특정 파일이 수정되면 강제로 포메팅 스크립트를 실행
- 커서룰에 명시할 수 도 있지만, 100% 동작을 보장할수는 없음


Share prompts with deeplinks
- 미리 작성된 프롬프트를 공유 할 수 있는 링크 생성 기능


PR summaries form Bugbot
PR in GitHub, 


-----------------------------------


Cursor browser
베타 기능이라서 설정에서 활성화가 필요함
- Cursor Settings > Beta > Cursor Brower
채팅창에서 Browser 를 눌러서 활성화를 해줘야함(파랑색)

커서에도 Plan 모드가 추가됨
- 기존에는 Agent / Background / Ask 가 있었음

Plan으로 하면 계획세우고 최종으로 마크다운파일을 생성해줌
채팅창에서 Build 버튼을 누르면 개발 요청

개발완료되면, 개발자가 브라우저를 열어서 확인을 해야 했었음
채팅창에 브라우저에서 확인하라고 시키면됨
너가 직접 브라우저를 열어서 게시글 목록에 댓글 수 표시 추가 기능이 잘 반영이 됐는지 확인해주고
실제로 추가 댓글들 작성해서 잘 추가되는지 확인해줘.
회원가입도 지가 알아서 함
마지막에 스크린샷도 찍어줌
콘솔에러나 네트워크 에러 같은것들이 있는지 한번 확인해줘.


Agent Window
Ctrl + E





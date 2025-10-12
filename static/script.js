// DOM 요소 참조
const scrapeForm = document.getElementById('scrapeForm');
const urlInput = document.getElementById('urlInput');
const scrapeBtn = document.getElementById('scrapeBtn');
const btnText = document.querySelector('.btn-text');
const btnLoading = document.querySelector('.btn-loading');
const resultsSection = document.getElementById('resultsSection');
const resultsContent = document.getElementById('resultsContent');
const errorSection = document.getElementById('errorSection');
const errorText = document.getElementById('errorText');

// 폼 제출 이벤트 리스너
scrapeForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const url = urlInput.value.trim();
    if (!url) {
        showError('URL을 입력해주세요.');
        return;
    }
    
    // 로딩 상태 시작
    setLoadingState(true);
    hideError();
    hideResults();
    
    try {
        const response = await fetch('/scrape', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url })
        });
        
        const data = await response.json();
        
        if (data.success) {
            showResults(data.data);
        } else {
            showError(data.error || '스크래핑 중 오류가 발생했습니다.');
        }
    } catch (error) {
        console.error('Error:', error);
        showError('네트워크 오류가 발생했습니다. 서버가 실행 중인지 확인해주세요.');
    } finally {
        setLoadingState(false);
    }
});

// 로딩 상태 설정
function setLoadingState(isLoading) {
    scrapeBtn.disabled = isLoading;
    if (isLoading) {
        btnText.style.display = 'none';
        btnLoading.style.display = 'inline-block';
    } else {
        btnText.style.display = 'inline-block';
        btnLoading.style.display = 'none';
    }
}

// 결과 표시
function showResults(data) {
    resultsContent.innerHTML = generateResultsHTML(data);
    resultsSection.style.display = 'block';
    errorSection.style.display = 'none';
    
    // 결과 섹션으로 스크롤
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

// 에러 표시
function showError(message) {
    errorText.textContent = message;
    errorSection.style.display = 'block';
    resultsSection.style.display = 'none';
}

// 결과 숨기기
function hideResults() {
    resultsSection.style.display = 'none';
}

// 에러 숨기기
function hideError() {
    errorSection.style.display = 'none';
}

// 결과 HTML 생성
function generateResultsHTML(data) {
    return `
        <div class="result-card">
            <h3>📄 기본 정보</h3>
            <table class="info-table">
                <tr>
                    <th>URL</th>
                    <td><a href="${data.url}" target="_blank">${data.url}</a></td>
                </tr>
                <tr>
                    <th>제목</th>
                    <td>${escapeHtml(data.title)}</td>
                </tr>
                <tr>
                    <th>설명</th>
                    <td>${escapeHtml(data.description)}</td>
                </tr>
                <tr>
                    <th>상태 코드</th>
                    <td><span class="status-code">${data.status_code}</span></td>
                </tr>
                <tr>
                    <th>콘텐츠 크기</th>
                    <td>${formatBytes(data.content_length)}</td>
                </tr>
            </table>
        </div>

        ${data.links.length > 0 ? `
        <div class="result-card">
            <h3>🔗 링크 (${data.links.length}개)</h3>
            <ul class="links-list">
                ${data.links.map(link => `
                    <li>
                        <a href="${link.url}" target="_blank">${escapeHtml(link.text)}</a>
                        <br><small>${link.url}</small>
                    </li>
                `).join('')}
            </ul>
        </div>
        ` : ''}

        ${data.images.length > 0 ? `
        <div class="result-card">
            <h3>🖼️ 이미지 (${data.images.length}개)</h3>
            <ul class="images-list">
                ${data.images.map(img => `
                    <li>
                        <img src="${img.src}" alt="${escapeHtml(img.alt)}" onerror="this.style.display='none'">
                        <span>${escapeHtml(img.alt)}</span>
                        <br><small>${img.src}</small>
                    </li>
                `).join('')}
            </ul>
        </div>
        ` : ''}
    `;
}

// HTML 이스케이프 함수
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// 바이트 단위 포맷팅
function formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

// 상태 코드에 따른 스타일링
document.addEventListener('DOMContentLoaded', function() {
    // CSS에 상태 코드 스타일 추가
    const style = document.createElement('style');
    style.textContent = `
        .status-code {
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
            font-family: monospace;
        }
        .status-code:contains("200") {
            background-color: #d1fae5;
            color: #065f46;
        }
        .status-code:contains("404") {
            background-color: #fee2e2;
            color: #991b1b;
        }
        .status-code:contains("500") {
            background-color: #fef3c7;
            color: #92400e;
        }
    `;
    document.head.appendChild(style);
});

// URL 입력 필드 포커스 시 에러 숨기기
urlInput.addEventListener('focus', function() {
    hideError();
});

// Enter 키로 폼 제출
urlInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        scrapeForm.dispatchEvent(new Event('submit'));
    }
});

// 페이지 로드 시 URL 입력 필드에 포커스
document.addEventListener('DOMContentLoaded', function() {
    urlInput.focus();
});

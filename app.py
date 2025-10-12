from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(url):
    """URL 유효성 검사"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def scrape_website(url):
    """웹사이트 스크래핑 함수"""
    try:
        # User-Agent 헤더 추가 (일부 사이트에서 차단 방지)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 기본 정보 추출
        title = soup.find('title')
        title_text = title.get_text().strip() if title else "제목 없음"
        
        # 메타 설명 추출
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc.get('content', '').strip() if meta_desc else "설명 없음"
        
        # 링크 추출 (최대 10개)
        links = []
        for link in soup.find_all('a', href=True)[:10]:
            href = link.get('href')
            text = link.get_text().strip()
            if href and text:
                # 상대 URL을 절대 URL로 변환
                if href.startswith('/'):
                    href = f"{urlparse(url).scheme}://{urlparse(url).netloc}{href}"
                elif not href.startswith('http'):
                    continue
                links.append({'url': href, 'text': text[:50] + '...' if len(text) > 50 else text})
        
        # 이미지 추출 (최대 5개)
        images = []
        for img in soup.find_all('img', src=True)[:5]:
            src = img.get('src')
            alt = img.get('alt', '이미지')
            if src:
                # 상대 URL을 절대 URL로 변환
                if src.startswith('/'):
                    src = f"{urlparse(url).scheme}://{urlparse(url).netloc}{src}"
                elif not src.startswith('http'):
                    continue
                images.append({'src': src, 'alt': alt[:30] + '...' if len(alt) > 30 else alt})
        
        return {
            'success': True,
            'data': {
                'url': url,
                'title': title_text,
                'description': description,
                'links': links,
                'images': images,
                'status_code': response.status_code,
                'content_length': len(response.content)
            }
        }
        
    except requests.exceptions.Timeout:
        return {'success': False, 'error': '요청 시간 초과 (10초)'}
    except requests.exceptions.ConnectionError:
        return {'success': False, 'error': '연결 오류 - URL을 확인해주세요'}
    except requests.exceptions.HTTPError as e:
        return {'success': False, 'error': f'HTTP 오류: {e.response.status_code}'}
    except Exception as e:
        return {'success': False, 'error': f'스크래핑 오류: {str(e)}'}

@app.route('/')
def index():
    """메인 페이지"""
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    """스크래핑 API 엔드포인트"""
    data = request.get_json()
    url = data.get('url', '').strip()
    
    if not url:
        return jsonify({'success': False, 'error': 'URL을 입력해주세요'})
    
    # URL 유효성 검사
    if not is_valid_url(url):
        return jsonify({'success': False, 'error': '올바른 URL 형식이 아닙니다'})
    
    # http:// 또는 https://가 없으면 https:// 추가
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # 스크래핑 실행
    result = scrape_website(url)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

def is_valid_url(url):
    """URL 유효성 검사"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def normalize_url(url, base_url):
    """상대 URL을 절대 URL로 변환"""
    if not url:
        return None
    if url.startswith('http://') or url.startswith('https://'):
        return url
    return urljoin(base_url, url)

def extract_meta_info(soup):
    """메타 정보 추출 (기본 메타 태그, Open Graph, Twitter Card)"""
    meta_info = {
        'description': '',
        'keywords': '',
        'author': '',
        'og_title': '',
        'og_description': '',
        'og_image': '',
        'twitter_card': '',
        'twitter_title': '',
        'twitter_description': '',
        'twitter_image': ''
    }
    
    # 기본 메타 태그
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        meta_info['description'] = meta_desc.get('content', '').strip()
    
    meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
    if meta_keywords:
        meta_info['keywords'] = meta_keywords.get('content', '').strip()
    
    meta_author = soup.find('meta', attrs={'name': 'author'})
    if meta_author:
        meta_info['author'] = meta_author.get('content', '').strip()
    
    # Open Graph 메타 태그
    og_title = soup.find('meta', property='og:title')
    if og_title:
        meta_info['og_title'] = og_title.get('content', '').strip()
    
    og_desc = soup.find('meta', property='og:description')
    if og_desc:
        meta_info['og_description'] = og_desc.get('content', '').strip()
    
    og_image = soup.find('meta', property='og:image')
    if og_image:
        meta_info['og_image'] = og_image.get('content', '').strip()
    
    # Twitter Card 메타 태그
    twitter_card = soup.find('meta', attrs={'name': 'twitter:card'})
    if twitter_card:
        meta_info['twitter_card'] = twitter_card.get('content', '').strip()
    
    twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
    if twitter_title:
        meta_info['twitter_title'] = twitter_title.get('content', '').strip()
    
    twitter_desc = soup.find('meta', attrs={'name': 'twitter:description'})
    if twitter_desc:
        meta_info['twitter_description'] = twitter_desc.get('content', '').strip()
    
    twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
    if twitter_image:
        meta_info['twitter_image'] = twitter_image.get('content', '').strip()
    
    return meta_info

def extract_main_text(soup):
    """주요 텍스트 본문 추출 (문단 및 헤딩 태그)"""
    text_content = []
    
    # 주요 헤딩 추출
    headings = soup.find_all(['h1', 'h2', 'h3'])
    for heading in headings[:5]:
        text = heading.get_text().strip()
        if text:
            text_content.append({
                'type': heading.name,
                'text': text[:200] + '...' if len(text) > 200 else text
            })
    
    # 주요 문단 추출
    paragraphs = soup.find_all('p')
    for p in paragraphs[:5]:
        text = p.get_text().strip()
        if len(text) > 50:  # 짧은 텍스트 제외
            text_content.append({
                'type': 'p',
                'text': text[:200] + '...' if len(text) > 200 else text
            })
    
    return text_content

def scrape_website(url):
    """웹사이트 스크래핑 함수 (개선 버전)"""
    try:
        # User-Agent 헤더 추가 (일부 사이트에서 차단 방지)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
        # 세션을 사용하여 쿠키 및 연결 재사용
        session = requests.Session()
        response = session.get(
            url, 
            headers=headers, 
            timeout=15,
            allow_redirects=True,
            verify=True
        )
        response.raise_for_status()
        
        # 인코딩 처리
        if response.encoding is None or response.encoding == 'ISO-8859-1':
            response.encoding = response.apparent_encoding or 'utf-8'
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 기본 정보 추출
        title_tag = soup.find('title')
        title_text = title_tag.get_text().strip() if title_tag else "제목 없음"
        
        # 메타 정보 추출
        meta_info = extract_meta_info(soup)
        
        # 설명 우선순위: OG description > meta description > 기본값
        description = (
            meta_info['og_description'] or 
            meta_info['description'] or 
            "설명 없음"
        )
        
        # 링크 추출 (최대 15개로 증가)
        links = []
        seen_links = set()  # 중복 링크 방지
        for link in soup.find_all('a', href=True):
            if len(links) >= 15:
                break
            href = link.get('href')
            text = link.get_text().strip()
            if href and text:
                normalized_href = normalize_url(href, url)
                if normalized_href and normalized_href not in seen_links:
                    seen_links.add(normalized_href)
                    # JavaScript나 mailto: 같은 스키마 제외
                    if normalized_href.startswith(('http://', 'https://')):
                        links.append({
                            'url': normalized_href,
                            'text': text[:100] + '...' if len(text) > 100 else text
                        })
        
        # 이미지 추출 (최대 10개로 증가)
        images = []
        seen_images = set()  # 중복 이미지 방지
        for img in soup.find_all('img', src=True):
            if len(images) >= 10:
                break
            src = img.get('src')
            alt = img.get('alt', '이미지')
            if src:
                normalized_src = normalize_url(src, url)
                if normalized_src and normalized_src not in seen_images:
                    seen_images.add(normalized_src)
                    if normalized_src.startswith(('http://', 'https://')):
                        images.append({
                            'src': normalized_src,
                            'alt': alt[:50] + '...' if len(alt) > 50 else alt
                        })
        
        # 주요 텍스트 본문 추출
        main_text = extract_main_text(soup)
        
        # 최종 URL (리다이렉트 후)
        final_url = response.url
        
        return {
            'success': True,
            'data': {
                'url': url,
                'final_url': final_url,
                'title': title_text,
                'description': description,
                'meta_info': meta_info,
                'links': links,
                'images': images,
                'main_text': main_text,
                'status_code': response.status_code,
                'content_length': len(response.content),
                'content_type': response.headers.get('Content-Type', ''),
                'encoding': response.encoding
            }
        }
        
    except requests.exceptions.Timeout:
        return {'success': False, 'error': '요청 시간 초과 (15초)'}
    except requests.exceptions.TooManyRedirects:
        return {'success': False, 'error': '리다이렉트 횟수가 너무 많습니다'}
    except requests.exceptions.ConnectionError as e:
        error_msg = str(e)
        if 'certificate' in error_msg.lower() or 'SSL' in error_msg:
            return {'success': False, 'error': 'SSL 인증서 오류 - URL을 확인해주세요'}
        return {'success': False, 'error': f'연결 오류: {error_msg}'}
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code if e.response else 'Unknown'
        return {'success': False, 'error': f'HTTP 오류 ({status_code}): {str(e)}'}
    except requests.exceptions.RequestException as e:
        return {'success': False, 'error': f'요청 오류: {str(e)}'}
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

import requests
import re
import os
from datetime import datetime
from urllib.parse import urlparse

# Domains from existing playlists
DOMAINS = [
    'sgw.ott.tricolor.tv',
    'peers.tv',
    'zabava-htlive.cdn.ngenix.net',
    'vgtrkregion-reg.cdnvideo.ru',
    # Add more from extraction
]

def extract_domains_from_m3u(m3u_path):
    domains = set()
    with open(m3u_path, 'r', encoding='utf-8') as f:
        content = f.read()
    urls = re.findall(r'https?://[^/\s]+', content)
    for url in urls:
        domain = urlparse(url).netloc
        if domain:
            domains.add(domain)
    return list(domains)

def scrape_channel(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200 and '.m3u8' in response.text.lower():
            return response.text
    except:
        pass
    return None

def main():
    print(f"[{datetime.now()}] Starting IPTV scraper...")
    
    # Extract more domains
    m3u_path = 'iptv/all_in_one.m3u'
    if os.path.exists(m3u_path):
        new_domains = extract_domains_from_m3u(m3u_path)
        print(f"Found {len(new_domains)} domains")
    
    # TODO: Implement full crawling logic for new channels
    # For now, aggregate existing
    print("Aggregation complete.")

if __name__ == "__main__":
    main()
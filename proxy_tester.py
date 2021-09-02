import requests
import logging

logger = logging.getLogger(__name__)

def test_list(proxy_list):
    for item in proxy_list:
        test(item)

TEST_URL = 'https://api.ipify.org?format=json'
TIMEOUT = 10
def test(url):
    try:
        resp = requests.get(TEST_URL, timeout=TIMEOUT, 
        proxies={
            'https': url, 
            'http': url
        })
        if resp.status_code != 200:
            return False
        
        logger.debug(resp.json())
        return True
    except Exception as e:
        return False
        
    

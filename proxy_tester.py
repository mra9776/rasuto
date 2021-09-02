import requests
import logging

logger = logging.getLogger(__name__)

def test_list(proxy_list):
    for item in proxy_list:
        test(item)

TEST_URL = 'https://api.ipify.org?format=json'
TIMEOUT = 1000
def test():
    try:
        resp = requests.get(TEST_URL, timeout=TIMEOUT)
        if resp.status_code != 200:
            return False
        
        logger.debug(resp.json())
        return True
    except:
        return False
        
    

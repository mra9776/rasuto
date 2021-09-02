import requests
import logging
import time
logger = logging.getLogger(__name__)


def test_list(proxy_list):
    for item in proxy_list:
        test(item)


TEST_URL = 'https://api.ipify.org?format=json'
TIMEOUT = 10
RETRY_EACH = 3


def test(url):
    sum_time = 0
    for i in range(RETRY_EACH):
        try:
            start_time = time.time()
            resp = requests.get(TEST_URL, timeout=TIMEOUT,
                                proxies={
                                    'https': url,
                                    'http': url
                                })
            if resp.status_code != 200:
                return False,  None

            stop_time = time.time()
            logger.debug(resp.json())

            sum_time += stop_time - start_time
        except Exception as e:
            return False, None

    return True, sum_time * 1000 / RETRY_EACH

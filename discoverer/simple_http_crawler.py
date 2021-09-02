import requests
import logging
from entities.host import Host
from discoverer.base_crawler import BaseCrawler

logger = logging.getLogger(__name__)

class SimpleCrawler(BaseCrawler):
    
    def start(self, proxies, parameters):
        sess = requests.session()
        url = 'https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json'
        resp = sess.get(url)
        resp.raise_for_status()

        data = resp.json()
        proxies = data['proxies']
        logger.info('found %d item', len(proxies))
        
        s = sorted(proxies, key=lambda a: a.get('google_total_time'))
        return (Host(item['ip'], int(item['port']), 'http', item['google_error'] == 'no') for item in s)


# 'google_error':'no'
# 'google_status':200
# 'google_total_time':3110
# 'ip':'79.143.87.140'
# 'port':'9090'
# 'yahoo_error':'no'
# 'yahoo_status':200
# 'yahoo_total_time':21480
# 'yandex_error':'no'
# 'yandex_status':200
# 'yandex_total_time':12020
                

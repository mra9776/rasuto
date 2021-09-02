import logging
from datetime import datetime
from proxy_tester import test
import discoverer
import repository.sqlite_helper

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def init_discoverer():
    lst = discoverer.discoverer_list
    for item in lst:
        disc = item()
        yield disc.start(None, None)

def main():
    logger.info('Starting app')
    logger.info(str(datetime.now()))
    # repository.sqlite_helper.init_db()
    
    proxy_providers = init_discoverer()
    for provider in proxy_providers:
        test(provider)


if __name__ == '__main__':
    repository.sqlite_helper.init_connection()
    main()

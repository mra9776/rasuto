import logging
from datetime import datetime
from proxy_tester import test
import discoverer
import repository.sqlite_helper
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

MAX_WORKER = 100


def init_discoverer():
    lst = discoverer.discoverer_list
    for item in lst:
        disc = item()
        yield disc.start(None, None)


def main():
    logger.info('Starting app')
    logger.info(str(datetime.now()))
    # repository.sqlite_helper.init_db()

    goods = []
    proxy_providers = init_discoverer()
    futures = {}
    pool = ThreadPoolExecutor(max_workers=MAX_WORKER)
    for provider in proxy_providers:
        futures.update({pool.submit(test, str(item)): item for item in provider})
    for fut in as_completed(futures):
        item = futures[fut]
        if fut.result():
            goods.append(item)
    pool.shutdown()
    for item in goods:
        print(str(item))

if __name__ == '__main__':
    repository.sqlite_helper.init_connection()
    main()

import outlog

import logging
import datetime
log_file_name = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
print(log_file_name)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename=log_file_name, filemode='a')
logger = logging.getLogger(__name__)

def main():
    outlog.te()
    logger.info('test main')

if __name__ == '__main__':
    main()
    
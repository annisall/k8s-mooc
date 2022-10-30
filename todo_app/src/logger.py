import logging

def get_logger(logger_name):
    logging.basicConfig(level = logging.INFO,
    format= '%(asctime)s - %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%S%z')
    schedule_logger = logging.getLogger(logger_name)

    return schedule_logger
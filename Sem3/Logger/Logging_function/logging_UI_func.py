import logging

def log_info(text, data):
    logging.info(f'{text}: {data}')

def log_debug(text, data):
    logging.debug(f'{text}: {data}')

def log_error(text, data):
    logging.error(f'{text}: {data}')

def log_exception(text, data):
    logging.exception(f'{text}: {data}')
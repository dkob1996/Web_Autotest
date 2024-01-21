import logging

def log_info_ui(text='', data=''):
    logging.info(f'{text}: {data}')

def log_debug_ui(text='', data=''):
    logging.debug(f'{text}: {data}')

def log_error_ui(text='', data=''):
    logging.error(f'{text}: {data}')

def log_exception_ui(text='', data=''):
    logging.exception(f'{text}: {data}')
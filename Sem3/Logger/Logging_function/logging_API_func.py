import logging

def log_assert_error_api(msg1='', msg2='', msg3=''):
    logging.error(f'{msg1}{msg2}{msg3}')

def log_exception_api(msg1='', msg2='', msg3=''):
    logging.exception(f'{msg1}{msg2}: \n{msg3}')

def log_response_api(msg1='', msg2='', msg3=''):
    logging.info(f'{msg1}{msg2}{msg3}')



def log_long_response_api(msg1='', msg2='', msg3='', msg4='', msg5='', msg6='', msg7=''):
    logging.info(f'{msg1}{msg2}{msg3}{msg4}{msg5}{msg6}{msg7}')
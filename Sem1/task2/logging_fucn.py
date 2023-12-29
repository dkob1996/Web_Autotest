import logging
import yaml

with open('/Users/dmitrii_kobozev/Desktop/Web_Autotests/Sem1/task2/config.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Логгирование
FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(level=logging.INFO, 
                    filename=data['log_file'], 
                    filemode="a", format= FORMAT, encoding="utf-8")

def log_assert_error(message):
    logging.error(f"{message}")

def log_exception(message):
    logging.exception(f'{message}')

def log_response(message):
    logging.info(message)
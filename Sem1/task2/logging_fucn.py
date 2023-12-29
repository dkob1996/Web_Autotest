import logging
import yaml
from static_paths import yaml_path

with open(yaml_path(), 'r') as f:
    data = yaml.safe_load(f)

# Логгирование
FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(level=logging.INFO, 
                    filename=data['log_file'], 
                    filemode="a", format= FORMAT, encoding="utf-8")

def log_assert_error(message):
    logging.error(f'{message}')

def log_exception(message):
    logging.exception(f'{message}')

def log_response(message):
    logging.info(message)
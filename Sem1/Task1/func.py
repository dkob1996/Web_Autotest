import yaml
import pytest
from zeep import Settings, Client

with open('/Users/dmitrii_kobozev/Desktop/Web_Autotests/Sem1/Task1/config.yaml', 'r') as f:
    data = yaml.safe_load(f)

settings = Settings(strict = False)
client = Client(wsdl=data["addr"], settings=settings)

def checkText(bad_word):
    return client.service.checkText(bad_word)[0]['s']
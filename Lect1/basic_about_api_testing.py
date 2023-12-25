import requests

## first request
response = requests.get('https://api.github.com')
response.status_code
print(f'first response code: {response}')

# examples of requests
## post
response = requests.post('https://httpbin.org/post', data={'key':'value'})
response.status_code
print(f'POST response code: {response}')

## put
response = requests.put('https://httpbin.org/put', data={'key':'value'})
response.status_code
print(f'PUT response code: {response}')

## delete
response = requests.delete('https://httpbin.org/delete')
response.status_code
print(f'DELETE response code: {response}')

## head
response = requests.head('https://httpbin.org/get')
response.status_code
print(f'HEAD response code: {response}')

## patch
response = requests.patch('https://httpbin.org/patch', data={'key':'value'})
response.status_code
print(f'PATCH response code: {response}')

## options
response = requests.options('https://httpbin.org/get')
response.status_code
print(f'OPTIONS response code: {response}')

# Data from requset
## content, text, json
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers = {'Accept': 'application/vnd.guthub.v3.text-match+json'},
)
print(response)

# Auth
from getpass import getpass
requests.get('https://api.github.com/user', auth=('username', getpass()))
headers = {'X-Yandex-API-Key': 'b1fb281f-b5ff-4257-8b94-35f249384a32'}
data = requests.get('https://api.weather.yandex.ru/v1/forecast?lat=55.466&lon=36.93&extra=true', headers = headers)
print(data.text)

# 20:46
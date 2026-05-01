from urllib import response
import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

data = response.json()

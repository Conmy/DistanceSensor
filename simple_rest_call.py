import requests

server_url = 'http://localhost:9090'

r = requests.post(server_url, json={'distance': (1.5 * 100)});
if r.status_code == 200:
	print('POST to the server Okay!')
else:
	print('Failed to POST to server')

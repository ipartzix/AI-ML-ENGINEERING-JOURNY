import requests

r = requests.get('https://pypi.org/project/requests/', )
print(r.text)

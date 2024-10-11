import requests

ip = requests.get('https://internet-lab.ru/ip').text

print(ip)
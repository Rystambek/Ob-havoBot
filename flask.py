import requests
import os

url = 'https://rustambek2003.pythonanywhere.com/'

TOKEN= os.environ['TOKEN']
payload = {
    'url':url,
}

r = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook",params=payload)
print(r.status_code)
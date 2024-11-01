import requests
from bs4 import BeautifulSoup
import os 

url = "https://www.vgmusic.com/music/"
response = requests.get(url)
print(f"Status code: {response.status_code}",)
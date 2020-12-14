print("Helloworld")


import requests
from bs4 import BeautifulSoup
import re

urlName = "https://business.nikkei.com"
url = requests.get(urlName)
soup = BeautifulSoup(url.content, "html.parser")
import re

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=Bloodborne")
content = request.content
soup = BeautifulSoup(content, "html.parser")
youtube_domain = "https://www.youtube.com{}"
for time in soup.find_all('span', {"class":"video-time"}):
    print(time.text)

import re

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=Bloodborne")
content = request.content
soup = BeautifulSoup(content, "html.parser")
page_array ={}
for page in soup.find_all('a', {"class": True, "data-visibility-tracking": True, "data-sessionlink": True,
                                "aria-label": True}):
    page_array['{}'.format(page.text)] = page.get('href')
print(page_array)
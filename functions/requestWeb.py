import re

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=Bloodborne")
content = request.content
soup = BeautifulSoup(content, "html.parser")
youtube_domain = "https://www.youtube.com{}"
for element in soup.find_all('a', {"rel": "spf-prefetch"}):
    video_link = element.get("href")
    video_id = video_link.split("=")[1]
    all_images = soup.find_all('img', {"height": True, "alt": True, "data-ytimg": True, "onload": True})
    image = re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(video_id), str(all_images))
    image_url = str(image).strip("[\"\']")
    image_url = image_url.replace("&amp;","&")
    print(image_url)
for element in soup.find_all('span', {"class": "video-time-overlay"}):
    print(element)
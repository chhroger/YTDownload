import re
import youtube_dl
import requests
from bs4 import BeautifulSoup


def search_content(search):
    request = requests.get("https://www.youtube.com/results?search_query={}".format(search))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup


def find_video(soup, videos, i=1):
    for element in soup.find_all('a', {"rel": "spf-prefetch"}):
        video_title = element.get("title")
        video_link = "https://www.youtube.com{}".format(element.get("href"))
        video_id = video_link.split("=")[1]
        all_images = soup.find_all('img', {"height": True, "alt": True, "data-ytimg": True, "onload": True})
        image = re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(video_id), str(all_images))
        image_url = str(image).strip("[\"\']")
        image_url = image_url.replace("&amp;", "&")
        videos["{}".format(i)] = {"title": video_title, "link": video_link, "image": image_url}
        i = i + 1
    return videos


def video_time(soup, videos, i=1):
    for time in soup.find_all('span', {"class": "video-time"}):
        videos.get("{}".format(i))["time"] = time.text
        i = i + 1
    return videos


def every_video(soup):
    videos = {}
    find_video(soup, videos, i=1)
    video_time(soup, videos, i=1)
    return videos


def page_bar(soup):
    page_array = {}
    for page in soup.find_all('a', {"class": True, "data-visibility-tracking": True, "data-sessionlink": True,
                                    "aria-label": True}):
        page_array['{}'.format(page.text)] = page.get('href')
    return page_array


def download_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': "/video/%(title)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as downloader:
        downloader.download(url)


def download_mp4(url):
    ydl_opts = {'outtmpl': "/video/%(title)s.%(ext)s"}
    with youtube_dl.YoutubeDL(ydl_opts) as downloader:
        downloader.download(url)

import youtube_dl

ydl_opts={'outtmpl':"/video/%(title)s.%(ext)s"}
with youtube_dl.YoutubeDL(ydl_opts) as downloader:
    downloader.download(['https://www.youtube.com/watch?v=Ct6BUPvE2sM'])
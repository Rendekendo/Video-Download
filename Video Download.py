import subprocess
from urllib.parse import urlparse

url = input("Please enter the URL: ")

parsed_url = urlparse(url)
domain = parsed_url.netloc

if 'youtube.com' in domain or 'youtu.be' in domain:
    command = (
        f'yt-dlp -f bestvideo+bestaudio --recode-video mp4 '
        f'-o "C:\\Users\\MaxBook\\Desktop\\%(title)s.%(ext)s" '
        f'"{url}"'
    )
    subprocess.run(command, shell=True)
else:
    command = (
        f'yt-dlp --recode-video mp4 '
        f'-o "C:\\Users\\MaxBook\\Desktop\\%(title)s.%(ext)s" '
        f'"{url}"'
    )
    subprocess.run(command, shell=True)

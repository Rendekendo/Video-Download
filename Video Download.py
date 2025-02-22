while True:
    import subprocess
    import os
    from urllib.parse import urlparse

    url = input("Please enter the URL: ")

    desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")

    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Construct the yt-dlp command
    output_path = os.path.join(desktop_path, "%(title)s.%(ext)s")

    if 'youtube.com' in domain or 'youtu.be' in domain:
        command = (
            f'yt-dlp -f bestvideo+bestaudio --recode-video mp4 '
            f'-o "{output_path}" "{url}"'
        )
    else:
        command = (
            f'yt-dlp --recode-video mp4 '
            f'-o "{output_path}" "{url}"'
        )

    subprocess.run(command, shell=True)
    print("---Video Downloaded---")



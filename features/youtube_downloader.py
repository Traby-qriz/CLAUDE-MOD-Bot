# File: features/youtube_downloader.py

from pytube import YouTube

async def youtube_downloader(url, download_type='audio'):
    try:
        yt = YouTube(url)
        if download_type == 'audio':
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        filename = stream.download()
        return f"Downloaded: {filename}"
    except Exception as e:
        return f"Error: {str(e)}"
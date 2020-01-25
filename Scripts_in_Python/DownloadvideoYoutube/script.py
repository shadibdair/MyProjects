# Pytube is a very serious, lightweight, dependency-free Python 
# library (and command-line utility) for downloading YouTube Videos.
# from pytube import YouTube
import pytube

url = "https://www.youtube.com/watch?v=BrlnGXDLmEg"

video = pytube.YouTube(url)
youtube = video.streams.first()
youtube.download(r'/home/Desktop')
from pytube import YouTube
import sys

link = sys.argv[-1]
if(type(link) == str and link[0:31] == "https://www.youtube.com/watch?v"):
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()

    print("Downloading...")
    ys.download()
    print("Video downloaded")
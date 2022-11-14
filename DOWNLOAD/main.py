

# SKUYMI [helmisalsabila.com]

from pytube import YouTube

link = "https://www.youtube.com/watch?v=_3y5di2chzY"
yt = YouTube(link)
yt.streams.first().download()


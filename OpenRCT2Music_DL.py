#This is a Proof of Concept. Written by Krutonium - https://github.com/Krutonium


import os

import moviepy.editor as mp
#moviepy - https://github.com/Zulko/moviepy
from pytube import YouTube
#pytube - https://github.com/nficano/pytube

print('Downloading Video from YouTube...')
yt = YouTube('https://www.youtube.com/watch?v=ykuT2RqB_LM')
#yt.streams.first().download()
print('Download Done, creating tracks...')
#os.rename('Rollercoaster Tycoon 2 Gameplay Music Remastered - PC OST.mp4','RCT2Music.mp4')
#At this point we have the raw audio file

clip = mp.VideoFileClip("RCT2Music.mp4").subclip(0,95)
clip.audio.write_audiofile("RomanFanfare.mp3")

    
    
    
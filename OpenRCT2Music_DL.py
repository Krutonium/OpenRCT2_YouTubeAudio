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

clip = mp.VideoFileClip("RCT2Music.mp4")

#00:00 Roman Fanfare Style 
#01:35 Oriental Style 
#03:30 Martian Style 
#05:49 Jungle Drums Style 
#07:39 Toyland Style 
#09:45 Space Style 
#12:36 Horror Style 
#14:38 Techno Style 
#16:36 Water Style 
#18:32 Wild West Style 
#20:43 Jurassic Style 
#22:56 Rock Style 
#24:58 Rock Style 2 
#26:40 Ice Style 
#29:10 Snow Style 
#31:05 Medieval Style

#Unfortunatly some of these have a little extra audio at the beginning/end either added or removed.

clip.subclip(0,96).audio.write_audiofile("RomanFanfare.mp3")
clip.subclip(96,211).audio.write_audiofile("OrientalStyle.mp3")
clip.subclip(211,350).audio.write_audiofile("MartianStyle.mp3")

    

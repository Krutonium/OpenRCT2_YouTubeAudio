#This is a Proof of Concept. Written by Krutonium - https://github.com/Krutonium
import os
import moviepy.editor as mp
#moviepy - https://github.com/Zulko/moviepy
from pytube import YouTube
#pytube - https://github.com/nficano/pytube

DryRun = True


print('Downloading Video from YouTube...')
yt = YouTube('https://www.youtube.com/watch?v=ykuT2RqB_LM')
if DryRun == False:
    yt.streams.first().download()
    os.rename('Rollercoaster Tycoon 2 Gameplay Music Remastered - PC OST.mp4','RCT2Music.mp4')
print('Download Done, creating tracks...')

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

if not os.path.exists("./wavs/"):
    os.makedirs("./wavs/")
if not os.path.exists("./dats/"):
    os.makedirs("./dats/")

#Math is Previous Time, Previous Time + Duration

clip.subclip(0,96).audio.write_audiofile("./wavs/01RomanFanfare.wav")
clip.subclip(96,211).audio.write_audiofile("./wavs/02OrientalStyle.wav")
clip.subclip(211,350).audio.write_audiofile("./wavs/03MartianStyle.wav")
clip.subclip(350,469).audio.write_audiofile("./wavs/04JungleDrumsStyle.wav")
clip.subclip(469,579).audio.write_audiofile("./wavs/05ToylandStyle.wav")
clip.subclip(569,695).audio.write_audiofile("./wavs/06SpaceStyle.wav")
clip.subclip(695,878).audio.write_audiofile("./wavs/07HorrorStyle.wav")
clip.subclip(878,998).audio.write_audiofile("./wavs/08TechoStyle.wav") #Seems to end too late?
clip.subclip(998,1116).audio.write_audiofile("./wavs/09WaterStyle.wav")
clip.subclip(1116,1232).audio.write_audiofile("./wavs/10WildWestStyle.wav")
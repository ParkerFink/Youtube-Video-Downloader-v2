import os
import tkinter
import webbrowser

from pytube import YouTube
#from pytube import Playlist


#checks to see if videos folder exists
videosFolder = os.path.exists('videos')
if videosFolder == True:
    pass
else:
    os.mkdir('videos')

            

#tkinter mainloop
window = tkinter.Tk()
window.title("Youtube Video Downloader")
window.geometry('400x150')


#download the video
def download(video):
    yt = YouTube(video)
    yt.streams.get_highest_resolution().download('videos/')

#gets the url
def getEntry():
    submitted = entry.get()
    entry.delete(0,1000000000)
    print(submitted)
    download(submitted)

def openVideos():
    cwd = os.getcwd() + '/videos'
    os.startfile(cwd)

def youtube():
    webbrowser.open('https://www.youtube.com/')

entry = tkinter.Entry(width=50)
entry.pack()

submit = tkinter.Button(text="Submit", command=lambda: getEntry(), width=35)
submit.pack()


open = tkinter.Button(text="Open Videos", command=openVideos, width=35)
open.pack()

youtube = tkinter.Button(text="Open Youtube", command=youtube, width=35)
youtube.pack()


window.mainloop()
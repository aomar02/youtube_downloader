from logging import exception
from tkinter import *
import pytube

root = Tk()
root.title("youtube downloader")
root.geometry("400x260")
root.resizable(False, False)

def download(link) :
    try :
        youtube = pytube.YouTube(link)
        video = youtube.streams.first()
        video.download("c:/Users/aalja/Desktop")
        footer_text.config(text="download completed", fg="green")
    except Exception as e :
        print(e)
        footer_text.config(text="valid URL!", fg="red")
    


title = Label(root, text="PYTHON YOUTUBE DOWNLOADER", font=('monospace', 10))
title.pack(pady=(50, 0))

sub_text = Label(root, text="please enter video link below :")
sub_text.pack(pady=(20, 0))

url = Entry(root, width=50)
url.pack(pady=(20, 0))

button = Button(root, text="DOWNLOAD", bg="red", fg="white", border=0 ,command=lambda : download(url.get()))
button.pack(pady=(20, 0))

footer_text = Label(root, text="your video will be downloaded to the desktop")
footer_text.pack(pady=(40, 0))

root.mainloop()
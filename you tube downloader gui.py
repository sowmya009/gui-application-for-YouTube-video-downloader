from pytube import YouTube
from tkinter import *
from pytube import YouTube
from tkinter.ttk import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os

root=Tk()
root.geometry('750x450')
root.configure(bg='grey')
root.resizable(False,False)
#to add logo first convert it into .ico extension
root.iconbitmap('pic.ico')
root.title('YouTube Video ')

def body():
    label=Label(root,text="YouTube Video Downloader",font="Italian 25 bold").grid(row=0,column=2,padx=5,pady=5,columnspan=3)
    
    give=Label(root,text="Link of the video : ").grid(row=2,column=1,padx=10,pady=10)
    root.giveText=Entry(root,width=65,textvariable=link).grid(row=2,column=2,padx=10,pady=10,columnspan=2)


    destination=Label(root,text="Where to store :").grid(row=3,column=1,padx=10,pady=10)
    root.destinationText=Entry(root,width=50,textvariable=download_path).grid(row=3,column=2,padx=10,pady=10)

    select_desti=Button(root,text="Browse",command=browse,width=10).grid(row=3,column=3,padx=2,pady=2)

    video_download=Button(root,text="Download",command=download,width=10).grid(row=5,column=2,padx=5,pady=5)

def browse():
    folder=fd.askdirectory(initialdir="Your directory path")
    download_path.set(folder)
    
def download():
    try:
        YouTube(link.get()).streams.first().download(download_path.get())
        mb.showinfo("Download Successfull","Your video is downloaded successfully.")
    except Exception as e:
        #root.update()
        mb.showinfo("Error","Error!! Video cannot be downloaded.")
    
link=StringVar()
download_path=StringVar()
body()
root.mainloop()

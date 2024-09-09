import tkinter
import customtkinter

from pytubefix import YouTube
from pytubefix.cli import on_progress

def startDownload():
    try:
        ytlink=link.get()
        ytobject=YouTube(ytlink,on_progress_callback=on_progress)
        video=ytobject.streams.get_highest_resolution()
        title.configure(text=ytobject.title,text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.configure(text="Download Error",text_color="red")
    
def on_progress(stream,chunk,bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded=total_size-bytes_remaining
    percentage_completion=bytes_downloaded/total_size*100
    per=str(int(percentage_completion))
    ppercent.configure(text=per+'%')
    ppercent.update()

    #update progress bar
    progressbar.set(float(percentage_completion/100))



#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app=customtkinter.CTk()
app.geometry("720x480)")
app.title("YouTube Downloader")



#Adding UI elements
title=customtkinter.CTkLabel(app,text="Insert a YouTube link")
title.pack(padx=10,pady=10)

#Link Input
url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

#Finished_Downloading
finishLabel=customtkinter.CTkLabel(app,text="")
finishLabel.pack()

#progress percent
ppercent=customtkinter.CTkLabel(app,text="0%")
ppercent.pack()

progressbar=customtkinter.CTkProgressBar(app,width=400)
progressbar.set(0)
progressbar.pack(padx=10,pady=10)

#Download Button
download=customtkinter.CTkButton(app,text='Download',command=startDownload)
download.pack(padx=10,pady=10)

#Runapp
app.mainloop()
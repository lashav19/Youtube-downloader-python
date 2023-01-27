import customtkinter
from pytube import YouTube
from PIL import Image
import tkinter
from tkinter import messagebox
import os


#shortcuts for widgets ex: Button(master=app, text="Press me!")
Label = customtkinter.CTkLabel
Button = customtkinter.CTkButton
Entry = customtkinter.CTkEntry

def downloadVideo(video_link: str, path: str, extension=str):

    if video_link == "":
        errorWindow(442, "Please input video link")
        return
    video = YouTube(video_link)
    video_download = None
    if extension == "mp4":
        print("downloading mp4")
        video_download = video.streams.get_highest_resolution()
        video_download.download(str(path))

    if extension == "mp3":
        print("Downloading mp3")
        video_download = video.streams.filter(only_audio=True).first().on_progress()
        out_file = video_download.download(str(path), )
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)



def fileBrowse():
    browse = customtkinter.filedialog.askdirectory(initialdir=fr"C:/Users/{os.getlogin()}/Downloads")
    browse = customtkinter.StringVar(app, browse)
    directory.configure(textvariable=browse)
    directory.configure(state="disabled")


def errorWindow(errorCode, message):
    messagebox.showerror(errorCode, message)


#main
if __name__ == "__main__":
    #sets the theme of the app
    customtkinter.set_appearance_mode("dark")

    #define app and values
    app = customtkinter.CTk()
    app.title("Youtube Downloader")
    app.geometry("1000x700")


    #widgets
    l1 = Label(app, text="Youtube downloader", font=("Helvetica", 30))
    l1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    link = customtkinter.CTkEntry(app, placeholder_text="Youtube link", width=300)
    link.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

    folder = Image.open("folder.png")

    directory = Entry(app, placeholder_text="Download directory", width=300)
    directory.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

    dirButton = Button(app, text="", image=customtkinter.CTkImage(folder), fg_color="transparent", width=25, command=fileBrowse)
    dirButton.place(relx=0.67, rely=0.35, anchor=tkinter.CENTER)

    start = Button(app, text="Download video", width=250, command=downloadVideo())
    start.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)


    #starting the window
    app.mainloop()

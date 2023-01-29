from pytube import YouTube
from pathlib import Path
from PIL import Image, ImageTk
import customtkinter
import tkinter
from tkinter import messagebox
import os
from downloader_functions import getImage, download_video
from time import sleep


# shortcuts for widgets ex: Button(master=app, text="Press me!")
Label = customtkinter.CTkLabel
Button = customtkinter.CTkButton
Entry = customtkinter.CTkEntry
Picture = customtkinter.CTkImage
OptionMenu = customtkinter.CTkOptionMenu


def downloader():  # Downloads the youtube video
    if link.get() == "":  # checks if there is a link that is input
        errorWindow("Error", "Please input video link")
        return
    messagebox.showinfo(
        "Heads up", "The program will freeze sometimes, just give it some time")

    video = YouTube(link.get())
    showThumbnail = Picture(getImage(video.thumbnail_url), size=(250, 200))

    tn = Label(app, text="", image=showThumbnail, height=40, width=150)
    tn.place(relx=0.2, rely=0.4, anchor=tkinter.CENTER)

    app.update_idletasks()


    download_video(video, filetype.get(), directory.get())  # calls function to download the video

    sleep(1)
    messagebox.showinfo("Download complete", "Sucessfully downloaded video")





# Opens a file browser where you select your downloads directory, defaults to the standard windows directory
def fileBrowse():
    browse = customtkinter.filedialog.askdirectory(initialdir=fr"C:/Users/{os.getlogin()}/Downloads")

    # updates the text in the directory to include the string text of which directory you chose
    browse = customtkinter.StringVar(app, browse)
    directory.configure(textvariable=browse)


def errorWindow(errorCode, message):  # Shows error window, takes error code (title of window) and message  to display
    messagebox.showerror(errorCode, message)


# main
if __name__ == "__main__":
    # sets the theme of the app
    customtkinter.set_appearance_mode("dark")


    # define app and values
    app = customtkinter.CTk()
    app.title("Youtube Downloader")
    app.geometry("1000x700")


    # widgets
    l1 = Label(app, text="Youtube downloader", font=("Helvetica", 30))
    l1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)


    link = customtkinter.CTkEntry(
        app, placeholder_text="Youtube link", width=300)
    link.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)


    # Failsafe for both testing and production code so no mixups happen
    try:
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        imgpath = os.path.join(scriptDir, "Exe", 'folder.png')
        folder = Image.open(imgpath)
    except FileNotFoundError:
        folder = Image.open("folder.png")

    directory = Entry(app, placeholder_text="Download directory", width=300)
    directory.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)


    # button that calls the fileBrowse function
    dirButton = Button(app, text="", image=customtkinter.CTkImage(
        folder), fg_color="transparent", width=25, command=fileBrowse)
    dirButton.place(relx=0.67, rely=0.45, anchor=tkinter.CENTER)

    Label(app, text="Filetype:", font=("Helvetica", 15)).place(
        relx=0.38, rely=0.55, anchor=tkinter.CENTER)
    filetype = OptionMenu(master=app, values=["mp3", "mp4"])
    filetype.place(relx=0.50, rely=0.55, anchor=tkinter.CENTER)

    # button that calls the downloader function
    start = Button(app, text="Download video", width=250, command=downloader)
    start.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

    # label for getting the thumbnail

    # starting the window
    app.mainloop()

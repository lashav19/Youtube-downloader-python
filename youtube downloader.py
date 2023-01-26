from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from time import sleep
import os


#https://www.youtube.com/watch?v=En_nLyMKRAI
#C:\Users\Lasse\Downloads


def downloader():
    print(file.get())
    if entry.get() == "":
        errorWindow(442, "Please input video link")
        return
    video = YouTube(entry.get())
    video_download = None
    if file.get() == "mp4":
        print("downloading mp4")
        video_download = video.streams.get_highest_resolution()
        video_download.download(str(path.get()))

    if file.get() == "mp3":
        print("Downloading mp3")
        video_download = video.streams.filter(only_audio=True).first()
        out_file = video_download.download(str(path.get()))
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    messagebox.showinfo("Video download", "Complete" f"\n Downloaded {str(YouTube.title)} as {file.get()}")
    link.set("")

    return



def errorWindow(errorCode, message):
    messagebox.showinfo(f"Error {errorCode}", message)



if __name__ == '__main__':
    window = tk.Tk()
    window.title("Youtube Downloader")
    window.geometry("800x400")

    formats = [
        "mp3",
        "mp4",
    ]


    yt = tk.Label(window, text="Youtube Downloader")
    yt.pack(padx=20, pady=30)

    link = tk.StringVar()
    enter_link = tk.Label(window, text="Enter video link:").pack()
    entry = tk.Entry(window, width=50)
    entry.pack(padx=30, pady=30)


    display = tk.Label(window, text="Enter download path:").pack()


    paths = tk.StringVar()
    path = tk.Entry(window, width=50, textvariable=paths)
    paths.set(fr"C:/Users/{os.getlogin()}/Downloads").pack(padx=30, pady=30)

    file = tk.StringVar()
    file.set("mp3")
    formatmenu = tk.OptionMenu(window, file, *formats)
    formatmenu.pack(padx=10)

    tk.Button(window, text="Download", background="white", foreground="blue", command=downloader).pack()


    window.mainloop()

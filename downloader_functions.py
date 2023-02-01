import os
import threading
import requests
import asyncio
from PIL import Image
from io import BytesIO
from pytube import YouTube
from tkinter import messagebox
from time import sleep


def getImage(URL):
    """
    Usage: getImage(URL)
    Uses Pillow, requests and BytesIO to convert an image from an imageUrl to bytes
    """
    thumbnail = requests.get(URL)
    img = Image.open(BytesIO(thumbnail.content), mode="r")
    b = BytesIO()
    img.save(b, format="PNG")
    b_value = b.getvalue()
    img = Image.open(BytesIO(b_value))
    return img

def complete():
    messagebox.showinfo("Download complete", "Successfully downloaded video")


async def download_video(link: str, file_type: str, download_dir: str, callback, app):
    """
    uses asyncio to run the function asyncrously to the code
    Downloads a youtube video either mp3 or mp4 using pytube
    Usage: download_video(link, "mp3" download_dir)
    """

    async def updateProgress(start, finish):
        for i in range(start, finish):
            sleep(0.05)
            callback(i+1/100)

        app.update()
        app.update_idletasks()

    def getmp3():

        stream = video.streams.filter(only_audio=True).first()
        out_file = stream.download(ddir)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        try:
            sleep(0.24)
            os.rename(out_file, new_file)
        # Renaming the the file because a duplicate exist
        except FileExistsError:  # If the file name already exists it adds _+1 to the file name
            name = 1
            while True:
                file, extension = os.path.splitext(new_file)
                file_new = f"{file}_{name}.mp3"
                print(base + f"_{name}.mp3")
                try:
                    os.rename(out_file, file_new)
                    break
                except FileExistsError:
                    print(f"Retry -> Name = {name}")
                    name += 1

            complete()

    def getmp4():
        def updateRest():
            for i in range(70,100):
                sleep(0.02)
                callback(i)
        stream = video.streams.get_highest_resolution()
        stream.download(download_dir)
        update = threading.Thread(updateRest())
        update.start()
        complete()
    # Checks which filetype is used
    video_download = None
    global video
    global ddir
    ddir = download_dir
    video = YouTube(link)

    if file_type == "mp4":  # Downloads highest mp4 resolution
        await updateProgress(0,70)
        mp4 = threading.Thread(getmp4())
        mp4.start()





    if file_type == "mp3":  # video as only audio then renames the file to .mp3
        await updateProgress(0, 20)
        app.update_idletasks()
        download_thread = threading.Thread(target=getmp3())
        update_thread = threading.Thread(await updateProgress(20, 100))
        update_thread.start()
        download_thread.start()
        app.mainloop()




def getThumbnail(link):
    thumbnail = YouTube(link).thumbnail_url
    return thumbnail


if __name__ == "__main__":
    yt = "https://www.youtube.com/watch?v=jBuc76nfuKA"
    print("test")

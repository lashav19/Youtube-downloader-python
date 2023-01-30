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


async def download_video(link: str, file_type: str, download_dir: str, callback, app):
    """
    uses asyncio to run the function asyncrously to the code
    Downloads a youtube video either mp3 or mp4 using pytube
    Usage: download_video(link, "mp3" download_dir)
    """

    def updateProgress(percent):
        callback(percent)
        app.update()
        app.update_idletasks()


    # Checks which filetype is used
    video_download = None
    video = YouTube(link)

    if file_type == "mp4":  # Downloads highest mp4 resolution
        updateProgress(0)
        app.update_idletasks()
        stream = video.streams.get_highest_resolution()
        updateProgress(.5)
        stream.download(download_dir)


    if file_type == "mp3":  # video as only audio then renames the file to .mp3
        updateProgress(0)
        app.update_idletasks()
        stream = video.streams.filter(only_audio=True).first()
        updateProgress(0.2)
        out_file = stream.download(download_dir)
        sleep(0.2)
        updateProgress(0.4)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        try:
            app.update_idletasks()
            updateProgress(0.6)
            sleep(0.2)
            updateProgress(0.8)
            os.rename(out_file, new_file)
        # Renaming the the file because a duplicate exist
        except FileExistsError:  # If the file name already exists it adds _+1 to the file name
            name = 1
            while True:
                file, extension = os.path.splitext(new_file)
                file_new = f"{file}_{name}.mp3"
                updateProgress(0.9)
                print(base + f"_{name}.mp3")

                try:
                    os.rename(out_file, file_new)
                    break
                except FileExistsError:
                    print(f"Retry -> Name = {name}")
                    name += 1
    updateProgress(100)
    complete()


def complete():
    messagebox.showinfo("Download complete", "Successfully downloaded video")

def getThumbnail(link):
    thumbnail = YouTube(link).thumbnail_url
    return thumbnail


if __name__ == "__main__":
    yt = "https://www.youtube.com/watch?v=jBuc76nfuKA"
    print("test")

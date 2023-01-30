import os
import requests
from PIL import Image
from io import BytesIO
from pytube import YouTube
from tkinter import messagebox


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


def download_video(link: str, file_type: str, download_dir: str, callback, app):
    """
    Downloads a youtube video either mp3 or mp4 using pytube
    Usage: download_video(link, "mp3" download_dir)
    """

    def updateProgress(chunk, file_handle, bytes_remaining):
        percent = (stream.filesize - bytes_remaining) / stream.filesize * 100
        print(percent)
        callback(percent)

    # Checks which filetype is used
    video_download = None
    video = YouTube(link, on_progress_callback=updateProgress)
    if file_type == "mp4":  # Downloads highest mp4 resolution
        stream = video.streams.get_highest_resolution()
        stream.download(download_dir)


    if file_type == "mp3":  # video as only audio then renames the file to .mp3
        stream = video.streams.filter(only_audio=True).first()
        try:
            out_file = stream.download(download_dir, chunk_size=1024, callback=callback)
        # Renaming the the file because a duplicate exist
        except FileExistsError:  # If the file name already exists it adds _+1 to the file name
            name = 1
            while True:
                file, extension = os.path.splitext(out_file)
                file_new = f"{out_file}_{name}.mp3"
                print(f"{out_file}_{name}.mp3")

                try:
                    os.rename(out_file, file_new)
                    break
                except FileExistsError:
                    print(f"Retry -> Name = {name}")
                    name += 1
    complete()


def complete():
    messagebox.showinfo("Download complete", "Successfully downloaded video")

def getThumbnail(link):
    thumbnail = YouTube(link).thumbnail_url
    return thumbnail


if __name__ == "__main__":
    yt = "https://www.youtube.com/watch?v=jBuc76nfuKA"
    print("test")

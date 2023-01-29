from PIL import Image, ImageTk
from io import BytesIO
from pytube import YouTube
import os
import requests


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


def download_video(link: str, file_type: str, download_dir: str):
    """
    Downloads a youtube video either mp3 or mp4 using pytube
    Usage: download_video(link, "mp3" download_dir)
    """
    # Checks which filetype is used
    video_download = None
    video = YouTube(link)
    if file_type == "mp4":  # Downloads highest mp4 resolution
        video.streams.get_highest_resolution().download(download_dir)

    if file_type == "mp3":  # video as only audio then renames the file to .mp3
        audio_stream = video.streams.filter(only_audio=True).first()
        out_file = audio_stream.download(download_dir)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        # Renaming the file to mp3 because it downloads as a "mp4" file with no video
        try:
            os.rename(out_file, new_file)
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


def getThumbnail(link):
    thumbnail = YouTube(link).thumbnail_url
    return thumbnail


if __name__ == "__main__":
    yt = "https://www.youtube.com/watch?v=jBuc76nfuKA"
    print("test")

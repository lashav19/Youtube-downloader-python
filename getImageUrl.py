from PIL import Image
from io import BytesIO
import requests
from tempfile import TemporaryFile
from pytube import YouTube
yt = "https://www.youtube.com/watch?v=jBuc76nfuKA"


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




if __name__ == "__main__":
    print("test")



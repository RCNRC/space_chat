from pathlib import Path
from urllib.parse import urlparse
import os
import requests


def get_image_type(image_url):
    parsed_url = urlparse(image_url)
    (_, ext) = os.path.splitext(parsed_url.path)
    return ext


def download_image(image_url, image_name, image_directory="./images", params=None):
    response = requests.get(url=image_url, params=params)
    response.raise_for_status()

    if not os.path.exists(image_directory):
        Path(image_directory).mkdir(parents=True, exist_ok=True)
    with open(f"{image_directory}/{image_name}{get_image_type(image_url)}", 'wb') as fh:
        fh.write(response.content)


if __name__ == '__main__':
    pass
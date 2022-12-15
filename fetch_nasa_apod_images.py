from base_scripts import download_image
from dotenv import dotenv_values
import requests


def fetch_nasa_apod_images(api_token, images_number=40):
    api_endpoint = "https://api.nasa.gov/planetary/apod"
    payload = {"count": f"{images_number}", "api_key": f"{api_token}"}
    response = requests.get(api_endpoint, params=payload)
    response.raise_for_status()
    for iters, image in enumerate(response.json()):
        if(image["media_type"]=="image"):
            download_image(image_url=image["url"], image_name=f"nasa_apod_{iters}")


def main():
    api_token = dotenv_values(".env")["NASA_API_KEY"]
    fetch_nasa_apod_images(api_token=api_token)


if __name__ == '__main__':
    main()

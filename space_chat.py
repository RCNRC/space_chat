from base_scripts import download_image
from dotenv import dotenv_values
import datetime
import requests


def fetch_nasa_epyc(api_token, images_number=10):
    api_endpoint = "https://api.nasa.gov/EPIC/api/natural"
    api_archive_endpoint = "https://api.nasa.gov/EPIC/archive/natural/"
    payload = {"api_key": f"{api_token}"}

    response = requests.get(api_endpoint, params=payload)
    response.raise_for_status()

    for i in range(images_number):
        image_id = response.json()[i]["image"]
        date_time = datetime.datetime.fromisoformat(response.json()[i]["date"])
        download_image(
            image_url=f"{api_archive_endpoint}{date_time.year}/{date_time.month}/{date_time.day}/png/{image_id}.png",
            image_name=f"nasa_epyc_{i}", params=payload
        )


def fetch_nasa_apod(api_token, images_number=40):
    api_endpoint = "https://api.nasa.gov/planetary/apod"
    payload = {"count": f"{images_number}", "api_key": f"{api_token}"}
    response = requests.get(api_endpoint, params=payload)
    response.raise_for_status()
    for iters, image in enumerate(response.json()):
        if(image["media_type"]=="image"):
            download_image(image_url=image["url"], image_name=f"nasa_apod_{iters}")


def fetch_spacex_last_launch(news_id="latest"):
    response = requests.get(url=f"https://api.spacexdata.com/v5/launches/{news_id}")
    response.raise_for_status()
    images_url = response.json()["links"]["flickr"]["original"]
    for iters, image_url in enumerate(images_url):
        download_image(image_url=image_url, image_name=f"spacex_{iters}")


def main():
    download_image(image_url="https://dvmn.org/media/HST-SM4.jpeg", image_name="Hubble")
    fetch_spacex_last_launch(news_id="5eb87d47ffd86e000604b38a")
    api_token = dotenv_values(".env")["NASA_API_KEY"]
    fetch_nasa_apod(api_token)
    fetch_nasa_epyc(api_token=api_token)


if __name__ == '__main__':
    main()
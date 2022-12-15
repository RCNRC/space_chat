from base_scripts import download_image
from dotenv import dotenv_values
import datetime
import requests


def fetch_nasa_epic_images(api_token, images_number=10):
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


def main():
    api_token = dotenv_values(".env")["NASA_API_KEY"]
    fetch_nasa_epic_images(api_token=api_token)


if __name__ == '__main__':
    main()
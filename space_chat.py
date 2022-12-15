from base_scripts import download_image
from fetch_spacex_images import fetch_spacex_images
from fetch_nasa_apod_images import fetch_nasa_apod_images
from fetch_nasa_epic_images import fetch_nasa_epic_images
from dotenv import dotenv_values


def main():
    download_image(image_url="https://dvmn.org/media/HST-SM4.jpeg", image_name="Hubble")
    fetch_spacex_images(news_id="5eb87d47ffd86e000604b38a")
    api_token = dotenv_values(".env")["NASA_API_KEY"]
    fetch_nasa_apod_images(api_token)
    fetch_nasa_epic_images(api_token=api_token)


if __name__ == '__main__':
    main()

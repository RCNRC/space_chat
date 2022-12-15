from base_scripts import download_image
import requests


def fetch_spacex_images(news_id="latest"):
    response = requests.get(url=f"https://api.spacexdata.com/v5/launches/{news_id}")
    response.raise_for_status()
    images_url = response.json()["links"]["flickr"]["original"]
    for iters, image_url in enumerate(images_url):
        download_image(image_url=image_url, image_name=f"spacex_{iters}")


if __name__ == '__main__':
    pass

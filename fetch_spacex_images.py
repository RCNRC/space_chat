from base_scripts import download_image
import requests
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('news_id', nargs='?')
    return parser.parse_args()


def fetch_spacex_images(news_id="latest"):
    response = requests.get(url=f"https://api.spacexdata.com/v5/launches/{news_id}")
    response.raise_for_status()
    images_url = response.json()["links"]["flickr"]["original"]
    for iters, image_url in enumerate(images_url):
        download_image(image_url=image_url, image_name=f"spacex_{iters}")


def main():
    arguments = get_arguments()
    news_id = arguments.news_id if arguments.news_id else "latest"
    fetch_spacex_images(news_id=news_id)


if __name__ == '__main__':
    main()

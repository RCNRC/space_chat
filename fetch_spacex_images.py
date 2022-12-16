from base_scripts import download_image
import requests
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="Script downloads images from SpaceX news in \"./image\" directory.")
    parser.add_argument('news_id', nargs='?', default="latest",
                        help="this is a unique identifier for the news of SpaceX company."
                        )
    return parser.parse_args()


def fetch_spacex_images(news_id="latest"):
    response = requests.get(url=f"https://api.spacexdata.com/v5/launches/{news_id}")
    response.raise_for_status()
    images_url = response.json()["links"]["flickr"]["original"]
    for image_number, image_url in enumerate(images_url):
        download_image(image_url=image_url, image_name=f"spacex_{image_number}")


def main():
    arguments = get_arguments()
    fetch_spacex_images(news_id=arguments.news_id)


if __name__ == '__main__':
    main()

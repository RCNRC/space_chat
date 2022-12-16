import telegram
from dotenv import dotenv_values
import os
import argparse
from random import shuffle
import time


def get_arguments():
    parser = argparse.ArgumentParser(description="Script starts the telegram bot.")
    parser.add_argument('hours_num', nargs='?', default=4, help="the number of hours between file uploads.")
    return parser.parse_args()


def post_images(bot, chat_id, hours_num, directory="images", ):
    files = os.walk(f"./{directory}")
    files = next(files)[2]
    shuffle(files)
    for file in files:
        with open(f"{directory}/{file}", 'rb') as file_handler:
            document = file_handler.read()
        bot.send_document(chat_id=chat_id, document=document)
        time.sleep(hours_num*60*60)
        hours_num = int(os.getenv('HOURS_NUM')) if os.getenv('HOURS_NUM') else hours_num
    post_images(bot=bot, chat_id=chat_id, directory=directory, hours_num=hours_num)


def main():
    api_key = dotenv_values(".env")["TELEGRAM_API_KEY"]
    bot = telegram.Bot(token=api_key)
    chat_id = dotenv_values(".env")["CHAT_ID"]
    arguments = get_arguments()
    post_images(bot=bot, chat_id=chat_id, hours_num=int(arguments.hours_num))


if __name__ == '__main__':
    main()

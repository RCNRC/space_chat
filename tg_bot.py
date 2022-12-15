import telegram
from dotenv import dotenv_values
import os
import argparse
from random import shuffle
import time


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('hours_num', nargs='?')
    return parser.parse_args()


def posting_random_image(bot, chat_id, directory="images", hours_num=4):
    files = os.walk(f"./{directory}")
    files = next(files)[2]
    shuffle(files)
    for file in files:
        bot.send_document(chat_id=chat_id, document=open(f"images/{file}", 'rb'))
        time.sleep(hours_num*60*60)
    posting_random_image(bot=bot, chat_id=chat_id, directory=directory, hours_num=hours_num)


def main():
    api_key = dotenv_values(".env")["TELEGRAM_API_KEY"]
    bot = telegram.Bot(token=api_key)
    chat_id = dotenv_values(".env")["CHAT_ID"]
    arguments = get_arguments()
    hours_num = int(arguments.hours_num) if arguments.hours_num else 4
    posting_random_image(bot=bot, chat_id=chat_id, hours_num=hours_num)


if __name__ == '__main__':
    main()

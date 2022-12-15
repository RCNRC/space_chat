import telegram
from dotenv import dotenv_values
import os
import argparse
from random import choice


def get_random_file(directory):
    files = os.walk(f"./{directory}")
    files = next(files)[2]
    return choice(files)


def post_file(bot, chat_id, file, directory="images"):
    file = file if (file and os.path.isfile(f"{directory}/{file}")) else get_random_file(directory=directory)
    bot.send_document(chat_id=chat_id, document=open(f"{directory}/{file}", 'rb'))


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?')
    return parser.parse_args()


def main():
    api_key = dotenv_values(".env")["TELEGRAM_API_KEY"]
    bot = telegram.Bot(token=api_key)
    chat_id = dotenv_values(".env")["CHAT_ID"]
    file = get_arguments().file if get_arguments().file else None
    post_file(bot=bot, chat_id=chat_id, file=file)


if __name__ == '__main__':
    main()

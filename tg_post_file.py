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
    if (not file) or (not os.path.isfile(f"{directory}/{file}")):
        file = get_random_file(directory=directory)
    with open(f"{directory}/{file}", 'rb') as file_handler:
        document = file_handler.read()
    bot.send_document(chat_id=chat_id, document=document)


def get_arguments():
    parser = argparse.ArgumentParser(description="Script posts file in telegram chat.")
    parser.add_argument('file', nargs='?', default=None,
                        help="this is the name of the file that will be sent to the telegram chat."
                        )
    return parser.parse_args()


def main():
    api_key = dotenv_values(".env")["TELEGRAM_API_KEY"]
    bot = telegram.Bot(token=api_key)
    chat_id = dotenv_values(".env")["CHAT_ID"]
    post_file(bot=bot, chat_id=chat_id, file=get_arguments().file)


if __name__ == '__main__':
    main()

import telegram
from dotenv import dotenv_values


def main():
    api_token = dotenv_values(".env")["TELEGRAM_API_KEY"]
    bot = telegram.Bot(token=api_token)
    bot.send_message(chat_id="-1001710105390", text="Text.")


if __name__ == '__main__':
    main()

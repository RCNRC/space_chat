# Установка

Скачать гит репозиторий. В корне репозитория создать файл `.env` и поместить внутрь следующие строки:
1. `NASA_API_KEY=ваш_токен`, где заменить строку `ваш_токен` на ваш уникальный токен с сайта [Nasa](https://api.nasa.gov/).
2. `TELEGRAM_API_KEY=апи_ключ`, где заменить строку `апи_ключ` на ваш уникальный апи ключ полученный при создании бота у [BotFather](https://telegram.me/BotFather).
3. `CHAT_ID=id_чата`, где заменить строку `id_чата` на id чата. Бот в этом чате должен иметь право на отправку файлов. 

# Требования к использованию

Требуется [Python](https://www.python.org/downloads/) версии 3.7 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/). Для установки необходимых зависимостей используйте команду:  
1. Для Unix/macOs:
```commandline
python -m pip install -r requirements.txt
```
2. Для Windows:
```commandline
py -m pip download --destination-directory DIR -r requirements.txt
```

# space_chat.py

Это python скрипт. Скачивает фотографии с сайтов [SpaceX](https://github.com/r-spacex/SpaceX-API) и [Nasa](https://api.nasa.gov/) и помещает их в папку `images`.  
Использование: запустить файл как python скрипт.  
Пример использования:
```commandline
python3 space_chat.py
```

# tg_bot.py

Это python скрипт, который запускает телеграм-бота. Бот публикует все файлы из папки `images` случайным образом. После публикации всех файлов бот начинает работу сначала.  
Скрипт имеет один необязательный позиционный параметр: число часов между публикациями. Время между публикациями по умолчанию установлено на 4 часа.  
Использование: запустить файл как python скрипт.  
Пример использования с установкой времени между публикациями в 2 часа:
```commandline
python3 tg_bot.py 2
```  
Пример использования с установкой времени по умолчанию в 4 часа:
```commandline
python3 tg_bot.py
```

# fetch_spacex_images.py

Это python скрипт. Скачивает фотографии с сайта [SpaceX](https://github.com/r-spacex/SpaceX-API) и помещает их в папку `images`.  
Скрипт имеет один необязательный позиционный параметр: id нужной новости. По умолчанию используется последняя опубликованная новость.  
Использование: запустить файл как python скрипт.  
Пример использования для получения фотографий из новости с id=`5eb87d47ffd86e000604b38a`:
```commandline
python3 fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```  
Пример использования для получения фотографий из последней опубликованной новости:
```commandline
python3 fetch_spacex_images.py
```

# fetch_nasa_apod_images.py

Это python скрипт. Скачивает 40 фотографий дня из секции "APOD" с сайта [Nasa](https://api.nasa.gov/) и помещает их в папку `images`.  
Использование: запустить файл как python скрипт.  
Пример использования:
```commandline
python3 fetch_nasa_apod_images.py
```

# fetch_nasa_epic_images.py

Это python скрипт. Скачивает 10 фотографий Земли из секции "EPIC" с сайта [Nasa](https://api.nasa.gov/) и помещает их в папку `images`.  
Использование: запустить файл как python скрипт.  
Пример использования:
```commandline
python3 fetch_nasa_epic_images.py
```
# space_chat

Это python скрипт. Скачивает фотографии с сайтов [SpaceX](https://github.com/r-spacex/SpaceX-API) и [Nasa](https://api.nasa.gov/) и помещает их в папку `space_chat/images`.

## Установка

Скачать гит репозиторий. В корне репозитория создать файл `.env` и поместить внутрь строку `NASA_API_KEY=ваш токен`, где заменить строку `ваш токен` на ваш уникальный токен с сайта [Nasa](https://api.nasa.gov/).

## Требования к использованию

Требуется [Python](https://www.python.org/downloads/) версии 3.7 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/). Для установки необходимых зависимостей используйте команду:  
1. Для Unix/macOs:
```commandline
python -m pip install -r requirements.txt
```
2. Для Windows:
```commandline
py -m pip download --destination-directory DIR -r requirements.txt
```

## Использование

Запустить файл space_chat.py как Python скрипт.

## Пример использования

```commandline
python3 space_chat.py
```  
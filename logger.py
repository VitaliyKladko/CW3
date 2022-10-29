import logging
from config import LOGGER_API_PATH, LOGGER_FORMAT


def logger_config():
    """
    Функция для загрузки конфига пользовательского логгера в app.py
    :return: None
    """
    # Создаем логгер и устанавливаем уровень
    api_logger = logging.getLogger('api_logger')
    api_logger.setLevel(logging.DEBUG)

    # Создаем хендлер, устанавливаем его уровень и подключаем к логгеру 'api_logger'
    api_logger_handler = logging.FileHandler(LOGGER_API_PATH)
    api_logger_handler.setLevel(logging.DEBUG)
    api_logger.addHandler(api_logger_handler)

    # создаем формат для логгера и подключаем его к хендлеру
    api_logger_format = logging.Formatter(LOGGER_FORMAT)
    api_logger_handler.setFormatter(api_logger_format)

import logging
from functools import wraps
from typing import Callable


def handle_errors(func: Callable) -> Callable:
    """Декоратор для обработки ошибок."""

    @wraps(func)
    def wrapper(self, *args, **kwargs) -> bool:
        logger = getattr(self, 'logger', logging.getLogger(func.__module__))
        method_name = func.__name__

        try:
            logger.info(f'🟢 Выполняем {method_name}')
            result = func(self, *args, **kwargs)

            if result:
                logger.info(f'🟢 {method_name} выполнен успешно')
            else:
                logger.error(f'🔴 {method_name} не выполнен')

            return result

        except Exception as e:
            logger.exception(f'🔴 Ошибка в {method_name}: {e}')
            return False

    return wrapper

    
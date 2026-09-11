import logging

from config_loader import config


def setup_logging() -> None:
    """Настраивает root-логгер из config.yaml. Безопасен при повторных вызовах."""

    root = logging.getLogger()

    if root.handlers:
        return

    logging.basicConfig(
        level=config.LOGGING_LEVEL,
        format=config.LOGGING_FORMAT,
        datefmt=config.LOGGING_DATE_FMT,
    )
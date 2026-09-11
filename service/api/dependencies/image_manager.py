
from functools import lru_cache

from image_manager import ImageManager


@lru_cache()
def get_image_manager() -> ImageManager:
    """DI для ImageManager с кешированием."""
    return ImageManager()

from typing import Any

from PIL import Image as PILImage

from elements.image_element import ImageElement
from elements.text_element import TextElement
from models.dataclasses import Image, Text


class ElementFactory:
    """Фабрика для создания элементов."""

    @staticmethod
    def create(element: Image | Text, canvas: PILImage.Image) -> ImageElement | TextElement | None:
        """Создает один их типов элементов."""

        if isinstance(element, Image):
            return ImageElement(element, canvas)
        if isinstance(element, Text):
            return TextElement(element, canvas)
        else:
            return None
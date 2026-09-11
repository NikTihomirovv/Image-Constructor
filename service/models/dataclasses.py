from dataclasses import dataclass, field

@dataclass
class Image:
    """Данные для описания картинки."""

    img: str = 'default_name.png'
    width: int = 1920
    height: int = 1080
    x: int = 0
    y: int = 0
    z: int = 0
    border_radius: int = 0


@dataclass
class Text:
    """Данные для описания текста."""

    text: str = 'default_text'
    font: str = 'arial'
    size: int = 14
    color: str = "#000000"
    width: int = 0
    height: int = 0
    x: int = 0
    y: int = 0
    z: int = 0
    alignment_y: str = 'top'
    alignment_x: str = 'left'
    line_height: int = 0
    letter_spacing: int = 0


@dataclass
class Canvas:
    """Данные для описания холста."""

    name: str = 'default_name'
    width: int = 1920
    height: int = 1080
    bg_color: str = "#FFFFFF"
    color_mode: str = 'RGB'

    images: list[Image] = field(default_factory=list)
    textes: list[Text] = field(default_factory=list)

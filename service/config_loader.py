from dataclasses import dataclass
from pathlib import Path
from typing import Final

import yaml

BASE_DIR = Path(__file__).resolve().parent


def load_config(config_path: str = "config.yaml") -> dict:
    """Загружает конфиг из YAML"""
    if not Path(config_path).exists():
        return {}
    
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}

raw_config = load_config(BASE_DIR / "config.yaml")

@dataclass
class Config:
    SAVE_TO_FOLDER: Final[bool] = raw_config.get('storage', {}).get('save_to_folder', False)
    OUTPUT_DIR: Final[str] = raw_config.get('storage', {}).get('output_dir', 'output/')
    FONTS_DIR: Final[str] = raw_config.get('storage', {}).get('fonts_dir', 'fonts/')
    RESOURCES_DIR: Final[str] = raw_config.get('storage', {}).get('resources_dir', 'resources/')

    LOGGING_LEVEL: Final[str] = raw_config.get('logging', {}).get('level', 'DEBUG')
    LOGGING_FORMAT: Final[str] = raw_config.get('logging', {}).get('format', '%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s')
    LOGGING_DATE_FMT: Final[str] = raw_config.get('logging', {}).get('datefmt', '%Y-%m-%d %H:%M:%S')

    RECURSION_LIMIT: Final[int] = raw_config.get('recursion', {}).get('limit', 1000)

    
@dataclass
class StaticPatternsVKConfig:
    """Конфигурация статических паттернов для VK."""
    
    CANVAS_WIDTH: Final[int] = raw_config.get('static_patterns_vk', {}).get('canvas_width', 1080)
    CANVAS_HEIGHT: Final[int] = raw_config.get('static_patterns_vk', {}).get('canvas_height', 1350)
    CANVAS_BG_COLOR: Final[str] = raw_config.get('static_patterns_vk', {}).get('canvas_bg_color', '#FFFFFF')
    CANVAS_COLOR_MODE: Final[str] = raw_config.get('static_patterns_vk', {}).get('canvas_color_mode', 'RGB')
    
    TITLE_FONT: Final[str] = raw_config.get('static_patterns_vk', {}).get('title_font', 'inner.ttf')
    TITLE_SIZE: Final[int] = raw_config.get('static_patterns_vk', {}).get('title_size', 60)
    TITLE_COLOR: Final[str] = raw_config.get('static_patterns_vk', {}).get('title_color', '#000000')
    TITLE_ALIGNMENT_X: Final[str] = raw_config.get('static_patterns_vk', {}).get('title_alignment_x', 'left')
    TITLE_ALIGNMENT_Y: Final[str] = raw_config.get('static_patterns_vk', {}).get('title_alignment_y', 'top')
    TITLE_LINE_HEIGHT: Final[int] = raw_config.get('static_patterns_vk', {}).get('title_line_height', 0)
    TITLE_LETTER_SPACING: Final[int] = raw_config.get('static_patterns_vk', {}).get('title_letter_spacing', 0)
    
    TEXT_FONT: Final[str] = raw_config.get('static_patterns_vk', {}).get('text_font', 'inner.ttf')
    TEXT_SIZE: Final[int] = raw_config.get('static_patterns_vk', {}).get('text_size', 40)
    TEXT_COLOR: Final[str] = raw_config.get('static_patterns_vk', {}).get('text_color', '#000000')
    TEXT_ALIGNMENT_X: Final[str] = raw_config.get('static_patterns_vk', {}).get('text_alignment_x', 'left')
    TEXT_ALIGNMENT_Y: Final[str] = raw_config.get('static_patterns_vk', {}).get('text_alignment_y', 'top')
    TEXT_LINE_HEIGHT: Final[int] = raw_config.get('static_patterns_vk', {}).get('text_line_height', 0)
    TEXT_LETTER_SPACING: Final[int] = raw_config.get('static_patterns_vk', {}).get('text_letter_spacing', 0)
    
    LOGO_FONT: Final[str] = raw_config.get('static_patterns_vk', {}).get('logo_font', 'inner.ttf')
    LOGO_SIZE: Final[int] = raw_config.get('static_patterns_vk', {}).get('logo_size', 40)
    LOGO_COLOR: Final[str] = raw_config.get('static_patterns_vk', {}).get('logo_color', '#000000')
    LOGO_ALIGNMENT_X: Final[str] = raw_config.get('static_patterns_vk', {}).get('logo_alignment_x', 'left')
    LOGO_ALIGNMENT_Y: Final[str] = raw_config.get('static_patterns_vk', {}).get('logo_alignment_y', 'top')
    LOGO_LINE_HEIGHT: Final[int] = raw_config.get('static_patterns_vk', {}).get('logo_line_height', 0)
    LOGO_LETTER_SPACING: Final[int] = raw_config.get('static_patterns_vk', {}).get('logo_letter_spacing', 0)


@dataclass
class StaticPatternsTGConfig:
    """Конфигурация статических паттернов для Telegram."""
    
    CANVAS_WIDTH: Final[int] = raw_config.get('static_patterns_tg', {}).get('canvas_width', 1080)
    CANVAS_HEIGHT: Final[int] = raw_config.get('static_patterns_tg', {}).get('canvas_height', 1350)
    CANVAS_BG_COLOR: Final[str] = raw_config.get('static_patterns_tg', {}).get('canvas_bg_color', '#FFFFFF')
    CANVAS_COLOR_MODE: Final[str] = raw_config.get('static_patterns_tg', {}).get('canvas_color_mode', 'RGB')
    
    TITLE_FONT: Final[str] = raw_config.get('static_patterns_tg', {}).get('title_font', 'inner.ttf')
    TITLE_SIZE: Final[int] = raw_config.get('static_patterns_tg', {}).get('title_size', 60)
    TITLE_COLOR: Final[str] = raw_config.get('static_patterns_tg', {}).get('title_color', '#000000')
    TITLE_ALIGNMENT_X: Final[str] = raw_config.get('static_patterns_tg', {}).get('title_alignment_x', 'left')
    TITLE_ALIGNMENT_Y: Final[str] = raw_config.get('static_patterns_tg', {}).get('title_alignment_y', 'top')
    TITLE_LINE_HEIGHT: Final[int] = raw_config.get('static_patterns_tg', {}).get('title_line_height', 0)
    TITLE_LETTER_SPACING: Final[int] = raw_config.get('static_patterns_tg', {}).get('title_letter_spacing', 0)
    
    TEXT_FONT: Final[str] = raw_config.get('static_patterns_tg', {}).get('text_font', 'inner.ttf')
    TEXT_SIZE: Final[int] = raw_config.get('static_patterns_tg', {}).get('text_size', 40)
    TEXT_COLOR: Final[str] = raw_config.get('static_patterns_tg', {}).get('text_color', '#000000')
    TEXT_ALIGNMENT_X: Final[str] = raw_config.get('static_patterns_tg', {}).get('text_alignment_x', 'left')
    TEXT_ALIGNMENT_Y: Final[str] = raw_config.get('static_patterns_tg', {}).get('text_alignment_y', 'top')
    TEXT_LINE_HEIGHT: Final[int] = raw_config.get('static_patterns_tg', {}).get('text_line_height', 0)
    TEXT_LETTER_SPACING: Final[int] = raw_config.get('static_patterns_tg', {}).get('text_letter_spacing', 0)
    
    LOGO_FONT: Final[str] = raw_config.get('static_patterns_tg', {}).get('logo_font', 'inner.ttf')
    LOGO_SIZE: Final[int] = raw_config.get('static_patterns_tg', {}).get('logo_size', 40)
    LOGO_COLOR: Final[str] = raw_config.get('static_patterns_tg', {}).get('logo_color', '#000000')
    LOGO_ALIGNMENT_X: Final[str] = raw_config.get('static_patterns_tg', {}).get('logo_alignment_x', 'left')
    LOGO_ALIGNMENT_Y: Final[str] = raw_config.get('static_patterns_tg', {}).get('logo_alignment_y', 'top')
    LOGO_LINE_HEIGHT: Final[int] = raw_config.get('static_patterns_tg', {}).get('logo_line_height', 0)
    LOGO_LETTER_SPACING: Final[int] = raw_config.get('static_patterns_tg', {}).get('logo_letter_spacing', 0)

config = Config()
vk_static_patterns_config = StaticPatternsVKConfig()
tg_static_patterns_config = StaticPatternsTGConfig()





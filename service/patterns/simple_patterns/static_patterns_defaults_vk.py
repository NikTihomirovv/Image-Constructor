from typing import Final

from config_loader import vk_static_patterns_config


class VKDefaults:
    """Базовые настройки для VK (1080x1350)."""
    CANVAS_WIDTH: Final[int] = vk_static_patterns_config.CANVAS_WIDTH
    CANVAS_HEIGHT: Final[int] = vk_static_patterns_config.CANVAS_HEIGHT
    CANVAS_BG_COLOR: Final[str] = vk_static_patterns_config.CANVAS_BG_COLOR
    CANVAS_COLOR_MODE: Final[str] = vk_static_patterns_config.CANVAS_COLOR_MODE
    
    TITLE_FONT: Final[str] = vk_static_patterns_config.TITLE_FONT
    TITLE_SIZE: Final[int] = vk_static_patterns_config.TITLE_SIZE
    TITLE_COLOR: Final[str] = vk_static_patterns_config.TITLE_COLOR
    TITLE_ALIGNMENT_X: Final[str] = vk_static_patterns_config.TITLE_ALIGNMENT_X
    TITLE_ALIGNMENT_Y: Final[str] = vk_static_patterns_config.TITLE_ALIGNMENT_Y
    TITLE_LINE_HEIGHT: Final[int] = vk_static_patterns_config.TITLE_LINE_HEIGHT
    TITLE_LETTER_SPACING: Final[int] = vk_static_patterns_config.TITLE_LETTER_SPACING
    
    TEXT_FONT: Final[str] = vk_static_patterns_config.TEXT_FONT
    TEXT_SIZE: Final[int] = vk_static_patterns_config.TEXT_SIZE
    TEXT_COLOR: Final[str] = vk_static_patterns_config.TEXT_COLOR
    TEXT_ALIGNMENT_X: Final[str] = vk_static_patterns_config.TEXT_ALIGNMENT_X
    TEXT_ALIGNMENT_Y: Final[str] = vk_static_patterns_config.TEXT_ALIGNMENT_Y
    TEXT_LINE_HEIGHT: Final[int] = vk_static_patterns_config.TEXT_LINE_HEIGHT
    TEXT_LETTER_SPACING: Final[int] = vk_static_patterns_config.TEXT_LETTER_SPACING
    
    LOGO_FONT: Final[str] = vk_static_patterns_config.LOGO_FONT
    LOGO_SIZE: Final[int] = vk_static_patterns_config.LOGO_SIZE
    LOGO_COLOR: Final[str] = vk_static_patterns_config.LOGO_COLOR
    LOGO_ALIGNMENT_X: Final[str] = vk_static_patterns_config.LOGO_ALIGNMENT_X
    LOGO_ALIGNMENT_Y: Final[str] = vk_static_patterns_config.LOGO_ALIGNMENT_Y
    LOGO_LINE_HEIGHT: Final[int] = vk_static_patterns_config.LOGO_LINE_HEIGHT
    LOGO_LETTER_SPACING: Final[int] = vk_static_patterns_config.LOGO_LETTER_SPACING


class VK_StaticPattern_1_Defaults(VKDefaults):
    """Вертикальный паттерн 1080 * 1350: 1/3 текста 980 * 400, 2/3 картинка 1080 * 900."""

    CANVAS_NAME: Final[str] = 'vk_static_pattern_1'
    
    # ===== Изображения =====
    # IMAGE_1: Фоновое изображение
    IMAGE_1_WIDTH: Final[int] = 1080
    IMAGE_1_HEIGHT: Final[int] = 900
    IMAGE_1_X: Final[int] = 0
    IMAGE_1_Y: Final[int] = 450
    IMAGE_1_Z: Final[int] = 1
    IMAGE_1_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_1_ROTATION: Final[float] = 0
    IMAGE_1_OPACITY: Final[float] = 1.0
    IMAGE_1_FLIP_X: Final[bool] = False
    IMAGE_1_FLIP_Y: Final[bool] = False
    
    # ===== Тексты =====
    # TEXT_1: Текст
    TEXT_1_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_1_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_1_COLOR: Final[str] = '#000000'
    TEXT_1_WIDTH: Final[int] = 980
    TEXT_1_HEIGHT: Final[int] = 400
    TEXT_1_X: Final[int] = 50
    TEXT_1_Y: Final[int] = 25
    TEXT_1_Z: Final[int] = 1
    TEXT_1_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_1_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_1_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_1_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING


class VK_StaticPattern_2_Defaults(VKDefaults):
    """Вертикальный паттерн 1080 * 1350: 1/3 текста 980 * 400, линия слева 5 * 400, 2/3 картинка 1080 * 900."""

    CANVAS_NAME: Final[str] = 'vk_static_pattern_2'

    # ===== Изображения =====
    # IMAGE_1: Фоновое изображение
    IMAGE_1_WIDTH: Final[int] = 1080
    IMAGE_1_HEIGHT: Final[int] = 900
    IMAGE_1_X: Final[int] = 0
    IMAGE_1_Y: Final[int] = 450
    IMAGE_1_Z: Final[int] = 1
    IMAGE_1_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_1_ROTATION: Final[float] = 0
    IMAGE_1_OPACITY: Final[float] = 1.0
    IMAGE_1_FLIP_X: Final[bool] = False
    IMAGE_1_FLIP_Y: Final[bool] = False

    # IMAGE_2: Линия слева
    IMAGE_2_WIDTH: Final[int] = 5
    IMAGE_2_HEIGHT: Final[int] = 400
    IMAGE_2_X: Final[int] = 25
    IMAGE_2_Y: Final[int] = 25
    IMAGE_2_Z: Final[int] = 1
    IMAGE_2_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_2_ROTATION: Final[float] = 0
    IMAGE_2_OPACITY: Final[float] = 1.0
    IMAGE_2_FLIP_X: Final[bool] = False
    IMAGE_2_FLIP_Y: Final[bool] = False
    
    # ===== Тексты =====
    # TEXT_1: Текст
    TEXT_1_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_1_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_1_COLOR: Final[str] = '#000000'
    TEXT_1_WIDTH: Final[int] = 980
    TEXT_1_HEIGHT: Final[int] = 400
    TEXT_1_X: Final[int] = 50
    TEXT_1_Y: Final[int] = 25
    TEXT_1_Z: Final[int] = 1
    TEXT_1_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_1_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_1_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_1_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING


class VK_StaticPattern_3_First_Defaults(VKDefaults):
    """Вертикальный паттерн 1080 * 1350: картинка 1080 * 1350, 1/2 текста, градиент 1080 * 450, свитчер, горизонтальная линия 800 * 1."""

    CANVAS_NAME: Final[str] = 'vk_static_pattern_3_first'

    # ===== Изображения =====
    # IMAGE_1: Фоновое изображение
    IMAGE_1_WIDTH: Final[int] = 1080
    IMAGE_1_HEIGHT: Final[int] = 1350
    IMAGE_1_X: Final[int] = 0
    IMAGE_1_Y: Final[int] = 0
    IMAGE_1_Z: Final[int] = 1
    IMAGE_1_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_1_ROTATION: Final[float] = 0
    IMAGE_1_OPACITY: Final[float] = 1.0
    IMAGE_1_FLIP_X: Final[bool] = False
    IMAGE_1_FLIP_Y: Final[bool] = False

    # IMAGE_2: Градиент
    IMAGE_2_WIDTH: Final[int] = 1080
    IMAGE_2_HEIGHT: Final[int] = 450
    IMAGE_2_X: Final[int] = 0
    IMAGE_2_Y: Final[int] = 900
    IMAGE_2_Z: Final[int] = 2
    IMAGE_2_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_2_ROTATION: Final[float] = 0
    IMAGE_2_OPACITY: Final[float] = 1.0
    IMAGE_2_FLIP_X: Final[bool] = False
    IMAGE_2_FLIP_Y: Final[bool] = False

    # IMAGE_3: Линия
    IMAGE_3_WIDTH: Final[int] = 800
    IMAGE_3_HEIGHT: Final[int] = 1
    IMAGE_3_X: Final[int] = 140
    IMAGE_3_Y: Final[int] = 1300
    IMAGE_3_Z: Final[int] = 3
    IMAGE_3_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_3_ROTATION: Final[float] = 0
    IMAGE_3_OPACITY: Final[float] = 1.0
    IMAGE_3_FLIP_X: Final[bool] = False
    IMAGE_3_FLIP_Y: Final[bool] = False

    # IMAGE_4: Стрелка
    IMAGE_4_WIDTH: Final[int] = 65
    IMAGE_4_HEIGHT: Final[int] = 65
    IMAGE_4_X: Final[int] = 657
    IMAGE_4_Y: Final[int] = 1240
    IMAGE_4_Z: Final[int] = 3
    IMAGE_4_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_4_ROTATION: Final[float] = 0
    IMAGE_4_OPACITY: Final[float] = 1.0
    IMAGE_4_FLIP_X: Final[bool] = False
    IMAGE_4_FLIP_Y: Final[bool] = False

    # ===== Тексты =====
    # TEXT_1: Заголовок
    TEXT_1_FONT: Final[str] = VKDefaults.TITLE_FONT
    TEXT_1_SIZE: Final[int] = VKDefaults.TITLE_SIZE
    TEXT_1_COLOR: Final[str] = '#FFFFFF'
    TEXT_1_WIDTH: Final[int] = 980
    TEXT_1_HEIGHT: Final[int] = 200
    TEXT_1_X: Final[int] = 50
    TEXT_1_Y: Final[int] = 636
    TEXT_1_Z: Final[int] = 3
    TEXT_1_ALIGNMENT_X: Final[str] = VKDefaults.TITLE_ALIGNMENT_X
    TEXT_1_ALIGNMENT_Y: Final[str] = VKDefaults.TITLE_ALIGNMENT_Y
    TEXT_1_LINE_HEIGHT: Final[int] = VKDefaults.TITLE_LINE_HEIGHT
    TEXT_1_LETTER_SPACING: Final[int] = VKDefaults.TITLE_LETTER_SPACING

    # TEXT_2: Основной текст
    TEXT_2_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_2_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_2_COLOR: Final[str] = '#FFFFFF'
    TEXT_2_WIDTH: Final[int] = 980
    TEXT_2_HEIGHT: Final[int] = 400
    TEXT_2_X: Final[int] = 50
    TEXT_2_Y: Final[int] = 836
    TEXT_2_Z: Final[int] = 3
    TEXT_2_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_2_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_2_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_2_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING

    # TEXT_3: Читать далее
    TEXT_3_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_3_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_3_COLOR: Final[str] = '#FFFFFF'
    TEXT_3_WIDTH: Final[int] = 300
    TEXT_3_HEIGHT: Final[int] = 30
    TEXT_3_X: Final[int] = 357
    TEXT_3_Y: Final[int] = 1250
    TEXT_3_Z: Final[int] = 3
    TEXT_3_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_3_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_3_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_3_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING


class VK_StaticPattern_3_Second_Defaults(VKDefaults):
    """Вертикальный паттерн 1080 * 1350: картинка 1080 * 1350, 1/2 текста, градиент 1080 * 450, свитчер, горизонтальная линия 800 * 1."""

    CANVAS_NAME: Final[str] = 'vk_static_pattern_3_second'

    # ===== Изображения =====
    # IMAGE_1: Фоновое изображение
    IMAGE_1_WIDTH: Final[int] = 1080
    IMAGE_1_HEIGHT: Final[int] = 1350
    IMAGE_1_X: Final[int] = 0
    IMAGE_1_Y: Final[int] = 0
    IMAGE_1_Z: Final[int] = 1
    IMAGE_1_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_1_ROTATION: Final[float] = 0
    IMAGE_1_OPACITY: Final[float] = 1.0
    IMAGE_1_FLIP_X: Final[bool] = False
    IMAGE_1_FLIP_Y: Final[bool] = False

    # IMAGE_2: Градиент
    IMAGE_2_WIDTH: Final[int] = 1080
    IMAGE_2_HEIGHT: Final[int] = 450
    IMAGE_2_X: Final[int] = 0
    IMAGE_2_Y: Final[int] = 900
    IMAGE_2_Z: Final[int] = 2
    IMAGE_2_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_2_ROTATION: Final[float] = 0
    IMAGE_2_OPACITY: Final[float] = 1.0
    IMAGE_2_FLIP_X: Final[bool] = False
    IMAGE_2_FLIP_Y: Final[bool] = False

    # IMAGE_3: Линия
    IMAGE_3_WIDTH: Final[int] = 800
    IMAGE_3_HEIGHT: Final[int] = 1
    IMAGE_3_X: Final[int] = 140
    IMAGE_3_Y: Final[int] = 1300
    IMAGE_3_Z: Final[int] = 3
    IMAGE_3_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_3_ROTATION: Final[float] = 0
    IMAGE_3_OPACITY: Final[float] = 1.0
    IMAGE_3_FLIP_X: Final[bool] = False
    IMAGE_3_FLIP_Y: Final[bool] = False

    # IMAGE_4: Стрелка
    IMAGE_4_WIDTH: Final[int] = 65
    IMAGE_4_HEIGHT: Final[int] = 65
    IMAGE_4_X: Final[int] = 657
    IMAGE_4_Y: Final[int] = 1240
    IMAGE_4_Z: Final[int] = 3
    IMAGE_4_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_4_ROTATION: Final[float] = 0
    IMAGE_4_OPACITY: Final[float] = 1.0
    IMAGE_4_FLIP_X: Final[bool] = False
    IMAGE_4_FLIP_Y: Final[bool] = False

    # ===== Тексты =====
    # TEXT_1: Основной текст
    TEXT_1_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_1_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_1_COLOR: Final[str] = '#FFFFFF'
    TEXT_1_WIDTH: Final[int] = 980
    TEXT_1_HEIGHT: Final[int] = 600
    TEXT_1_X: Final[int] = 50
    TEXT_1_Y: Final[int] = 536
    TEXT_1_Z: Final[int] = 1
    TEXT_1_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_1_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_1_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_1_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING

    # TEXT_2: Читать далее
    TEXT_2_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_2_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_2_COLOR: Final[str] = '#FFFFFF'
    TEXT_2_WIDTH: Final[int] = 300
    TEXT_2_HEIGHT: Final[int] = 30
    TEXT_2_X: Final[int] = 357
    TEXT_2_Y: Final[int] = 1250
    TEXT_2_Z: Final[int] = 3
    TEXT_2_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_2_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_2_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_2_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING


class VK_StaticPattern_3_Third_Defaults(VKDefaults):
    """Вертикальный паттерн 1080 * 1350: картинка 1080 * 1350, 1/2 текста, градиент 1080 * 450, горизонтальная линия 800 * 1."""

    CANVAS_NAME: Final[str] = 'vk_static_pattern_3_third'

    # ===== Изображения =====
    # IMAGE_1: Фоновое изображение
    IMAGE_1_WIDTH: Final[int] = 1080
    IMAGE_1_HEIGHT: Final[int] = 1350
    IMAGE_1_X: Final[int] = 0
    IMAGE_1_Y: Final[int] = 0
    IMAGE_1_Z: Final[int] = 1
    IMAGE_1_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_1_ROTATION: Final[float] = 0
    IMAGE_1_OPACITY: Final[float] = 1.0
    IMAGE_1_FLIP_X: Final[bool] = False
    IMAGE_1_FLIP_Y: Final[bool] = False

    # IMAGE_2: Градиент
    IMAGE_2_WIDTH: Final[int] = 1080
    IMAGE_2_HEIGHT: Final[int] = 450
    IMAGE_2_X: Final[int] = 0
    IMAGE_2_Y: Final[int] = 900
    IMAGE_2_Z: Final[int] = 2
    IMAGE_2_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_2_ROTATION: Final[float] = 0
    IMAGE_2_OPACITY: Final[float] = 1.0
    IMAGE_2_FLIP_X: Final[bool] = False
    IMAGE_2_FLIP_Y: Final[bool] = False

    # IMAGE_3: Линия
    IMAGE_3_WIDTH: Final[int] = 800
    IMAGE_3_HEIGHT: Final[int] = 1
    IMAGE_3_X: Final[int] = 140
    IMAGE_3_Y: Final[int] = 1300
    IMAGE_3_Z: Final[int] = 3
    IMAGE_3_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_3_ROTATION: Final[float] = 0
    IMAGE_3_OPACITY: Final[float] = 1.0
    IMAGE_3_FLIP_X: Final[bool] = False
    IMAGE_3_FLIP_Y: Final[bool] = False

    # ===== Тексты =====
    # TEXT_1: Основной текст
    TEXT_1_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_1_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_1_COLOR: Final[str] = '#FFFFFF'
    TEXT_1_WIDTH: Final[int] = 980
    TEXT_1_HEIGHT: Final[int] = 600
    TEXT_1_X: Final[int] = 50
    TEXT_1_Y: Final[int] = 536
    TEXT_1_Z: Final[int] = 1
    TEXT_1_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_1_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_1_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_1_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING


class VK_StaticPattern_4_First_Defaults(VKDefaults):
    """Вертикальный паттерн 1080 * 1350: 1/3 картинка 1080 * 450, 2/3 бэкграунд, 1/2 текста, градиент 1080 * 450, свитчер, текстовый логотип, горизонтальная линия 800 * 1."""

    CANVAS_NAME: Final[str] = 'vk_static_pattern_4_first'

    # ===== Изображения =====
    # IMAGE_1: Фоновое изображение
    IMAGE_1_WIDTH: Final[int] = 1080
    IMAGE_1_HEIGHT: Final[int] = 450
    IMAGE_1_X: Final[int] = 0
    IMAGE_1_Y: Final[int] = 0
    IMAGE_1_Z: Final[int] = 1
    IMAGE_1_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_1_ROTATION: Final[float] = 0
    IMAGE_1_OPACITY: Final[float] = 1.0
    IMAGE_1_FLIP_X: Final[bool] = False
    IMAGE_1_FLIP_Y: Final[bool] = False

    # IMAGE_2: Линия
    IMAGE_2_WIDTH: Final[int] = 980
    IMAGE_2_HEIGHT: Final[int] = 1
    IMAGE_2_X: Final[int] = 50
    IMAGE_2_Y: Final[int] = 1250
    IMAGE_2_Z: Final[int] = 3
    IMAGE_2_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_2_ROTATION: Final[float] = 0
    IMAGE_2_OPACITY: Final[float] = 1.0
    IMAGE_2_FLIP_X: Final[bool] = False
    IMAGE_2_FLIP_Y: Final[bool] = False

    # IMAGE_3: Стрелка
    IMAGE_3_WIDTH: Final[int] = 65
    IMAGE_3_HEIGHT: Final[int] = 65
    IMAGE_3_X: Final[int] = 975
    IMAGE_3_Y: Final[int] = 1267
    IMAGE_3_Z: Final[int] = 3
    IMAGE_3_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_3_ROTATION: Final[float] = 0
    IMAGE_3_OPACITY: Final[float] = 1.0
    IMAGE_3_FLIP_X: Final[bool] = False
    IMAGE_3_FLIP_Y: Final[bool] = False

    # IMAGE_4: Бэкграунд
    IMAGE_4_WIDTH: Final[int] = 1080
    IMAGE_4_HEIGHT: Final[int] = 900
    IMAGE_4_X: Final[int] = 0
    IMAGE_4_Y: Final[int] = 450
    IMAGE_4_Z: Final[int] = 2
    IMAGE_4_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_4_ROTATION: Final[float] = 0
    IMAGE_4_OPACITY: Final[float] = 1.0
    IMAGE_4_FLIP_X: Final[bool] = False
    IMAGE_4_FLIP_Y: Final[bool] = False

    # ===== Тексты =====
    # TEXT_1: Заголовок
    TEXT_1_FONT: Final[str] = VKDefaults.TITLE_FONT
    TEXT_1_SIZE: Final[int] = VKDefaults.TITLE_SIZE
    TEXT_1_COLOR: Final[str] = '#FFFFFF'
    TEXT_1_WIDTH: Final[int] = 980
    TEXT_1_HEIGHT: Final[int] = 150
    TEXT_1_X: Final[int] = 50
    TEXT_1_Y: Final[int] = 500
    TEXT_1_Z: Final[int] = 3
    TEXT_1_ALIGNMENT_X: Final[str] = VKDefaults.TITLE_ALIGNMENT_X
    TEXT_1_ALIGNMENT_Y: Final[str] = VKDefaults.TITLE_ALIGNMENT_Y
    TEXT_1_LINE_HEIGHT: Final[int] = VKDefaults.TITLE_LINE_HEIGHT
    TEXT_1_LETTER_SPACING: Final[int] = VKDefaults.TITLE_LETTER_SPACING

    # TEXT_2: Основной текст
    TEXT_2_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_2_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_2_COLOR: Final[str] = '#FFFFFF'
    TEXT_2_WIDTH: Final[int] = 980
    TEXT_2_HEIGHT: Final[int] = 500
    TEXT_2_X: Final[int] = 50
    TEXT_2_Y: Final[int] = 700
    TEXT_2_Z: Final[int] = 3
    TEXT_2_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_2_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_2_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_2_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING

    # TEXT_3: Текстовый логотип
    TEXT_3_FONT: Final[str] = VKDefaults.LOGO_FONT
    TEXT_3_SIZE: Final[int] = VKDefaults.LOGO_SIZE
    TEXT_3_COLOR: Final[str] = '#FFFFFF'
    TEXT_3_WIDTH: Final[int] = 500
    TEXT_3_HEIGHT: Final[int] = 50
    TEXT_3_X: Final[int] = 50
    TEXT_3_Y: Final[int] = 1275
    TEXT_3_Z: Final[int] = 3
    TEXT_3_ALIGNMENT_X: Final[str] = VKDefaults.LOGO_ALIGNMENT_X
    TEXT_3_ALIGNMENT_Y: Final[str] = VKDefaults.LOGO_ALIGNMENT_Y
    TEXT_3_LINE_HEIGHT: Final[int] = VKDefaults.LOGO_LINE_HEIGHT
    TEXT_3_LETTER_SPACING: Final[int] = VKDefaults.LOGO_LETTER_SPACING


class VK_StaticPattern_4_Second_Defaults(VKDefaults):
    """Вертикальный паттерн 1080 * 1350: 1/3 картинка 1080 * 450, 2/3 бэкграунд, 1/2 текста, градиент 1080 * 450, свитчер, текстовый логотип, горизонтальная линия 800 * 1."""

    CANVAS_NAME: Final[str] = 'vk_static_pattern_4_second'

    # ===== Изображения =====
    # IMAGE_1: Фоновое изображение
    IMAGE_1_WIDTH: Final[int] = 1080
    IMAGE_1_HEIGHT: Final[int] = 450
    IMAGE_1_X: Final[int] = 0
    IMAGE_1_Y: Final[int] = 0
    IMAGE_1_Z: Final[int] = 1
    IMAGE_1_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_1_ROTATION: Final[float] = 0
    IMAGE_1_OPACITY: Final[float] = 1.0
    IMAGE_1_FLIP_X: Final[bool] = False
    IMAGE_1_FLIP_Y: Final[bool] = False

    # IMAGE_2: Линия
    IMAGE_2_WIDTH: Final[int] = 980
    IMAGE_2_HEIGHT: Final[int] = 1
    IMAGE_2_X: Final[int] = 50
    IMAGE_2_Y: Final[int] = 1250
    IMAGE_2_Z: Final[int] = 3
    IMAGE_2_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_2_ROTATION: Final[float] = 0
    IMAGE_2_OPACITY: Final[float] = 1.0
    IMAGE_2_FLIP_X: Final[bool] = False
    IMAGE_2_FLIP_Y: Final[bool] = False

    # IMAGE_3: Стрелка
    IMAGE_3_WIDTH: Final[int] = 65
    IMAGE_3_HEIGHT: Final[int] = 65
    IMAGE_3_X: Final[int] = 975
    IMAGE_3_Y: Final[int] = 1267
    IMAGE_3_Z: Final[int] = 3
    IMAGE_3_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_3_ROTATION: Final[float] = 0
    IMAGE_3_OPACITY: Final[float] = 1.0
    IMAGE_3_FLIP_X: Final[bool] = False
    IMAGE_3_FLIP_Y: Final[bool] = False

    # IMAGE_4: Бэкграунд
    IMAGE_4_WIDTH: Final[int] = 1080
    IMAGE_4_HEIGHT: Final[int] = 900
    IMAGE_4_X: Final[int] = 0
    IMAGE_4_Y: Final[int] = 450
    IMAGE_4_Z: Final[int] = 2
    IMAGE_4_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_4_ROTATION: Final[float] = 0
    IMAGE_4_OPACITY: Final[float] = 1.0
    IMAGE_4_FLIP_X: Final[bool] = False
    IMAGE_4_FLIP_Y: Final[bool] = False

    # ===== Тексты =====
    # TEXT_1: Основной текст
    TEXT_1_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_1_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_1_COLOR: Final[str] = '#FFFFFF'
    TEXT_1_WIDTH: Final[int] = 980
    TEXT_1_HEIGHT: Final[int] = 750
    TEXT_1_X: Final[int] = 50
    TEXT_1_Y: Final[int] = 500
    TEXT_1_Z: Final[int] = 3
    TEXT_1_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_1_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_1_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_1_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING

    # TEXT_2: Текстовый логотип
    TEXT_2_FONT: Final[str] = VKDefaults.LOGO_FONT
    TEXT_2_SIZE: Final[int] = VKDefaults.LOGO_SIZE
    TEXT_2_COLOR: Final[str] = '#FFFFFF'
    TEXT_2_WIDTH: Final[int] = 500
    TEXT_2_HEIGHT: Final[int] = 50
    TEXT_2_X: Final[int] = 50
    TEXT_2_Y: Final[int] = 1275
    TEXT_2_Z: Final[int] = 3
    TEXT_2_ALIGNMENT_X: Final[str] = VKDefaults.LOGO_ALIGNMENT_X
    TEXT_2_ALIGNMENT_Y: Final[str] = VKDefaults.LOGO_ALIGNMENT_Y
    TEXT_2_LINE_HEIGHT: Final[int] = VKDefaults.LOGO_LINE_HEIGHT
    TEXT_2_LETTER_SPACING: Final[int] = VKDefaults.LOGO_LETTER_SPACING


class VK_StaticPattern_4_Third_Defaults(VKDefaults):
    """Вертикальный паттерн 1080 * 1350: 1/3 картинка 1080 * 450, 2/3 бэкграунд, 1/2 текста, градиент 1080 * 450, текстовый логотип, горизонтальная линия 800 * 1."""

    CANVAS_NAME: Final[str] = 'vk_static_pattern_4_third'

    # ===== Изображения =====
    # IMAGE_1: Фоновое изображение
    IMAGE_1_WIDTH: Final[int] = 1080
    IMAGE_1_HEIGHT: Final[int] = 450
    IMAGE_1_X: Final[int] = 0
    IMAGE_1_Y: Final[int] = 0
    IMAGE_1_Z: Final[int] = 1
    IMAGE_1_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_1_ROTATION: Final[float] = 0
    IMAGE_1_OPACITY: Final[float] = 1.0
    IMAGE_1_FLIP_X: Final[bool] = False
    IMAGE_1_FLIP_Y: Final[bool] = False

    # IMAGE_2: Линия
    IMAGE_2_WIDTH: Final[int] = 980
    IMAGE_2_HEIGHT: Final[int] = 1
    IMAGE_2_X: Final[int] = 50
    IMAGE_2_Y: Final[int] = 1250
    IMAGE_2_Z: Final[int] = 3
    IMAGE_2_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_2_ROTATION: Final[float] = 0
    IMAGE_2_OPACITY: Final[float] = 1.0
    IMAGE_2_FLIP_X: Final[bool] = False
    IMAGE_2_FLIP_Y: Final[bool] = False

    # IMAGE_3: Бэкграунд
    IMAGE_3_WIDTH: Final[int] = 1080
    IMAGE_3_HEIGHT: Final[int] = 900
    IMAGE_3_X: Final[int] = 0
    IMAGE_3_Y: Final[int] = 450
    IMAGE_3_Z: Final[int] = 2
    IMAGE_3_BORDER_RADIUS: Final[int] = 0
    
    # Transform
    IMAGE_3_ROTATION: Final[float] = 0
    IMAGE_3_OPACITY: Final[float] = 1.0
    IMAGE_3_FLIP_X: Final[bool] = False
    IMAGE_3_FLIP_Y: Final[bool] = False

    # ===== Тексты =====
    # TEXT_1: Основной текст
    TEXT_1_FONT: Final[str] = VKDefaults.TEXT_FONT
    TEXT_1_SIZE: Final[int] = VKDefaults.TEXT_SIZE
    TEXT_1_COLOR: Final[str] = '#FFFFFF'
    TEXT_1_WIDTH: Final[int] = 980
    TEXT_1_HEIGHT: Final[int] = 750
    TEXT_1_X: Final[int] = 50
    TEXT_1_Y: Final[int] = 500
    TEXT_1_Z: Final[int] = 3
    TEXT_1_ALIGNMENT_X: Final[str] = VKDefaults.TEXT_ALIGNMENT_X
    TEXT_1_ALIGNMENT_Y: Final[str] = VKDefaults.TEXT_ALIGNMENT_Y
    TEXT_1_LINE_HEIGHT: Final[int] = VKDefaults.TEXT_LINE_HEIGHT
    TEXT_1_LETTER_SPACING: Final[int] = VKDefaults.TEXT_LETTER_SPACING

    # TEXT_2: Текстовый логотип
    TEXT_2_FONT: Final[str] = VKDefaults.LOGO_FONT
    TEXT_2_SIZE: Final[int] = VKDefaults.LOGO_SIZE
    TEXT_2_COLOR: Final[str] = '#FFFFFF'
    TEXT_2_WIDTH: Final[int] = 500
    TEXT_2_HEIGHT: Final[int] = 50
    TEXT_2_X: Final[int] = 50
    TEXT_2_Y: Final[int] = 1275
    TEXT_2_Z: Final[int] = 3
    TEXT_2_ALIGNMENT_X: Final[str] = VKDefaults.LOGO_ALIGNMENT_X
    TEXT_2_ALIGNMENT_Y: Final[str] = VKDefaults.LOGO_ALIGNMENT_Y
    TEXT_2_LINE_HEIGHT: Final[int] = VKDefaults.LOGO_LINE_HEIGHT
    TEXT_2_LETTER_SPACING: Final[int] = VKDefaults.LOGO_LETTER_SPACING
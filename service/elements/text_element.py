import logging
import os
from dataclasses import is_dataclass
from typing import List

from PIL import Image as PILImage
from PIL import ImageDraw, ImageFont

from config_loader import config
from decorators.def_decorators import handle_errors
from models.dataclasses import Text


class TextElement:
    """Класс для описания текста."""

    def __init__(self, element: Text, canvas: PILImage.Image):
        self.logger = logging.getLogger(__name__)
        self.canvas = canvas

        self.text_element = element
        self.text = None
        self.font = None
        self.size = None
        self.color = None
        self.width = None
        self.height = None
        self.x = None
        self.y = None
        self.alignment_x = None
        self.alignment_y = None
        self.catched_fonts = {}

    @handle_errors
    def add_element(self) -> bool:
        """Добавляет текст."""
            
        if not self.text_element or not is_dataclass(self.text_element):
            self.logger.error('🔴 Ошибка в получении параметров')
            return False

        self.text = self.text_element.text
        self.font = self.text_element.font
        self.size = self.text_element.size
        self.color = self.text_element.color
        self.width = self.text_element.width
        self.height = self.text_element.height
        self.x = self.text_element.x
        self.y = self.text_element.y
        self.alignment_x = self.text_element.alignment_x
        self.alignment_y = self.text_element.alignment_y
        self.line_height = self.text_element.line_height
        self.letter_spacing = self.text_element.letter_spacing
                
        required_values = {
            'text': self.text,
            'font': self.font,
            'size': self.size,
            'color': self.color,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
            'alignment_x': self.alignment_x,
            'alignment_y': self.alignment_y,
            'line_height': self.line_height,
            'letter_spacing': self.letter_spacing,
        }

        missing = [name for name, value in required_values.items() if value is None]
        if missing:
            self.logger.error(f'🔴 Ошибка в получении параметров, отсутствуют: {missing}')
            return False

        self.logger.info(f'🟢 Текст: {self.text[:30]}...')
        self.logger.info(f'🟢 Шрифт: {self.font}')
        self.logger.info(f'🟢 Размер: {self.size}')
        self.logger.info(f'🟢 Цвет: {self.color}')
        self.logger.info(f'🟢 Выравнивание по горизонтали: {self.alignment_x}')
        self.logger.info(f'🟢 Позиция текстового блока: ({self.x}, {self.y})')
        self.logger.info(f'🟢 Размер текстового блока: ({self.width}, {self.height})')

        if self.alignment_y:
            self.y = self._apply_alignment_y(self.text, self.y, self.height)
        
        # Проверяем, есть ли в тексте принудительные переносы
        if '\n' in self.text:
            self.logger.info('🟢 Обнаружены принудительные переносы строк (\\n)')
            
            # Разбиваем текст по \n
            lines = self.text.split('\n')
            
            # Удаляем пустые строки
            lines = [line for line in lines if line.strip()]
            
            if not lines:
                self.logger.error('🔴 Текст состоит только из переносов')
                return False
            
            # Вычисляем высоту одной строки
            line_height = self._get_text_height(lines[0], self.font)
            if line_height and self.line_height:
                line_height += self.line_height
            
            # Рисуем каждую строку с отступом
            current_y = self.y
            for line in lines:
                # Проверяем, помещается ли строка по ширине
                line_width = self._get_text_width(line, self.font)
                
                if line_width <= self.width:
                    # Строка помещается - рисуем как есть
                    if not self._add_string(line, self.x, current_y):
                        return False
                else:
                    # Строка слишком длинная - разбиваем автоматически
                    self.logger.info(f'🟢 Строка слишком длинная, разбиваем автоматически: {line[:30]}...')
                    sub_lines = self._separate_text(line, self.width)
                    for sub_line in sub_lines:
                        if not self._add_string(sub_line, self.x, current_y):
                            return False
                        current_y += line_height
                    continue
                
                current_y += line_height
            
            self.logger.info(f'🟢 Текст с переносами добавлен, строк: {len(lines)}')
            return True
        
        # Проверяем уберется ли текст в свой блок по ширине
        all_text_width = self._get_text_width(self.text, self.font)
        if not all_text_width:
            return False
        
        if self._get_text_width_fit(all_text_width, self.width):
            self.logger.info(f'🟢 Исходный текст подходит под ширину текстового блока')
            if not self._add_string(self.text, self.x, self.y):
                return False

        else:
            self.logger.info(f'🟢 Исходный текст слишком длинный для своего блока')
            text_strings = self._separate_text(self.text, self.width)
            text_height = self._get_text_height(self.text, self.font)
            text_offset_y = self.y
            if text_strings:
                for string in text_strings:
                    success = self._add_string(string, self.x, text_offset_y)
                    text_offset_y += text_height

                    if not success:
                        return False
            else: 
                return False
            
            return True

        self.logger.info(f'🟢 Текст добавлен')
        return True

    def _get_text_width(self, text: str, font: str) -> int:
        """Находит ширину текста в пикселях."""

        font = self._load_font(font, self.size)
        draw = ImageDraw.Draw(self.canvas)
        width = draw.textlength(text=text, font=font)
        return int(width)

    def _get_text_height(self, text: str, font: str) -> int:
        """Находит высоту текста в пикселях."""
        
        font = self._load_font(font, self.size)
        draw = ImageDraw.Draw(self.canvas)
        
        bbox = draw.textbbox((0, 0), text, font=font)
        height = bbox[3] - bbox[1]  # bottom - top
        
        return int(height)


    def _get_text_width_fit(self, text_width: int, place_width: int) -> bool:
        """Проверяет уберется ли текст по ширине."""

        return text_width <= place_width


    @handle_errors
    def _add_string(self, text: str, x: int, y: int) -> bool:
        """Добавляет строку на канвас с поддержкой межбуквенного интервала."""

        try:
            font = self._load_font(self.font, self.size)
            draw = ImageDraw.Draw(self.canvas)

            if self.alignment_x:
                x = self._apply_alignment_x(text, x, self.width)

            # Если есть межбуквенный интервал, рисуем каждую букву отдельно
            if self.letter_spacing != 0:
                current_x = x
                for char in text:
                    draw.text((current_x, y), char, font=font, fill=self.color)
                    char_width = draw.textlength(char, font=font)
                    current_x += char_width + self.letter_spacing
            else:
                draw.text((x, y), text, font=font, fill=self.color)
            
            return True
            
        except FileNotFoundError:
            self.logger.error(f'🔴 Шрифт не найден: {self.font}')
            return False
        except OSError as e:
            self.logger.error(f'🔴 Ошибка шрифта: {e}')
            return False


    def _apply_alignment_x(self, text: str, x: int, place_width: int) -> int:
        """Выравнивает строку по горизонтали."""

        try: 
            self.logger.info(f'🟢 Применяем выравнивание по горизонтали')
            text_width = self._get_text_width(text, self.font)

            match self.alignment_x:
                case 'left':
                    pass
                case 'center':
                    x += (place_width / 2 - text_width / 2)
                case 'right':
                    x += (place_width - text_width)
                case _:
                    pass
            return x
        except Exception as e:
            self.logger.error(f'🔴 Не удалось применить выравнивание по горизонтали: {e}')
            return x


    def _apply_alignment_y(self, text: str, y: int, place_height: int) -> int:
        """Выравнивает текстовый блок по вертикали."""

        try:
            self.logger.info(f'🟢 Применяем выравнивание по вертикали')
            text_height = self._get_text_height(text, self.font)

            match self.alignment_y:
                case 'top':
                    pass
                case 'center':
                    y += (place_height / 2 - text_height / 2)
                case 'bottom':
                    y += (place_height - text_height)
                case _:
                    pass
            return y
        except Exception as e:
            self.logger.error(f'🔴 Не удалось применить выравнивание по вертикали: {e}')
            return y

    @handle_errors
    def _separate_text(self, text: str, place_width: int) -> List[str] | None:
        """Разделяет текст для переноса на другую строку по словам."""
        
        if not text:
            return []
        
        # Если текст помещается целиком
        text_width = self._get_text_width(text, self.font)
        if text_width <= place_width:
            return [text]
        
        words = text.split(' ')

        fitting_words = []
        current_width = 0
        
        for word in words:
            word_width = self._get_text_width(word + ' ', self.font)
            if current_width + word_width <= place_width:
                fitting_words.append(word)
                current_width += word_width
            else:
                break
        
        if not fitting_words:
            fitting_words = [words[0]]
            remaining_words = words[1:]
        else:
            remaining_words = words[len(fitting_words):]
        
        line = ' '.join(fitting_words)
        
        remaining_text = ' '.join(remaining_words)
        rest_lines = self._separate_text(remaining_text, place_width)
        
        return [line] + rest_lines

    @handle_errors
    def _load_font(self, font_name: str, size: int) -> ImageFont:
        """Загружает шрифт из папки fonts."""

        cache_key = f"{font_name}_{size}"
        if cache_key in self.catched_fonts:
            self.logger.info(f'🟢 Шрифт из кеша: {font_name} ({size}px)')
            return self.catched_fonts[cache_key]
        
        possible_paths = [
            os.path.join(config.FONTS_DIR, font_name),           
        ]
        
        fallback_fonts = [
            'Arial.ttf',
        ]
        
        for path in possible_paths:
            try:
                self.logger.info(f'🟢 Пробуем шрифт: {path}')
                loaded_font = ImageFont.truetype(path, size)
                self.catched_fonts[cache_key] = loaded_font
                return loaded_font
            except Exception:
                continue
        
        for font in fallback_fonts:
            try:
                path = os.path.join(config.FONTS_DIR, font)
                self.logger.info(f'🟢 Пробуем fallback шрифт: {path}')
                loaded_font = ImageFont.truetype(path, size)
                self.catched_fonts[cache_key] = loaded_font
                return loaded_font
            except Exception:
                continue

        self.logger.error(f'🔴 Не удалось загрузить шрифты')
        return ImageFont.load_default()
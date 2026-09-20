import base64
import io
import logging
import os
from dataclasses import is_dataclass

import cairosvg
from PIL import Image as PILImage
from PIL import ImageDraw

from config_loader import config
from decorators.def_decorators import handle_errors
from models.dataclasses import Image


class ImageElement:
    """Класс для описания картинки."""

    def __init__(self, element: Image, canvas: PILImage.Image):
        self.logger = logging.getLogger(__name__)
        self.canvas = canvas

        self.image = element
        self.img = None
        self.width = None
        self.height = None
        self.x = None
        self.y = None
        self.border_radius = None
        self.rotation = None
        self.opacity = None
        self.flip_x = None
        self.flip_y = None


    @handle_errors
    def add_element(self) -> bool:
        """Добавляет изображение."""

        if not self.image or not is_dataclass(self.image):
            self.logger.error('🔴 Ошибка в получении параметров')
            return False

        self.img = self.image.img
        self.width = self.image.width
        self.height = self.image.height
        self.x = self.image.x
        self.y = self.image.y
        self.border_radius = self.image.border_radius
        self.rotation = self.image.rotation
        self.opacity = self.image.opacity
        self.flip_x = self.image.flip_x
        self.flip_y = self.image.flip_y

        required_values = {
            'img': self.img,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
            'border_radius': self.border_radius,
            'rotation': self.rotation,
            'opacity': self.opacity, 
            'flip_x': self.flip_x, 
            'flip_y': self.flip_y, 
        }

        missing = [name for name, value in required_values.items() if value is None]
        if missing:
            self.logger.error(f'🔴 Ошибка в получении параметров, отсутствуют: {missing}')
            return False

        self.logger.info(f'🟢 Изображение: {self.img[:30]}...')
        self.logger.info(f'🟢 Размер: {self.width}x{self.height}')
        self.logger.info(f'🟢 Позиция: ({self.x}, {self.y})')

        try:
            if self._is_base64(self.img):
                overlay = self._decode_base64_image(self.img)
            else:
                full_path = os.path.join(config.RESOURCES_DIR, self.img)
                overlay = self._load_image(full_path)

            if not overlay:
                self.logger.error('🔴 Не удалось открыть изображение')
                return False

            if self.width and self.height:
                overlay = overlay.resize((self.width, self.height))
                self.logger.info(f'🟢 Изменён размер: {overlay.size}')

            if self.flip_x:
                overlay = overlay.transpose(
                    PILImage.Transpose.FLIP_LEFT_RIGHT
                )
                self.logger.info('🟢 Flip X применён')

            if self.flip_y:
                overlay = overlay.transpose(
                    PILImage.Transpose.FLIP_TOP_BOTTOM
                )
                self.logger.info('🟢 Flip Y применён')

            if self.rotation:
                overlay = overlay.rotate(
                    -self.rotation,
                    expand=True,
                    resample=PILImage.Resampling.BICUBIC
                )
                self.logger.info(
                    f'🟢 Поворот: {self.rotation} градусов'
                )

            if self.opacity is not None and self.opacity < 1:
                overlay = overlay.convert("RGBA")
                alpha = overlay.getchannel("A")
                alpha = alpha.point(
                    lambda p: int(p * self.opacity)
                )

                overlay.putalpha(alpha)
                self.logger.info(f'🟢 Прозрачность: {self.opacity}')

            if self.border_radius > 0:
                overlay = self._apply_border_radius(
                    overlay,
                    self.border_radius
                )

            if self.rotation:
                center_x = self.x + self.width / 2
                center_y = self.y + self.height / 2

                paste_x = int(center_x - overlay.width / 2)
                paste_y = int(center_y - overlay.height / 2)

            else:
                paste_x = self.x
                paste_y = self.y

            if overlay.mode == 'RGBA':
                self.canvas.paste(
                    overlay,
                    (paste_x, paste_y),
                    overlay
                )
            else:
                self.canvas.paste(
                    overlay,
                    (paste_x, paste_y)
                )

        except FileNotFoundError:
            self.logger.error(f'🔴 Файл не найден: {self.img}')
            return False
                
        except Exception as e:
            self.logger.error(f'🔴 Ошибка при открытии изображения: {e}')
            return False

        self.logger.info(f'🟢 Изображение добавлено')
        return True

    def _load_image(self, file_path: str) -> PILImage.Image:
        """Загружает изображение из файла (поддерживает PNG, JPG, SVG)."""
        
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.svg':
            
            self.logger.info(f'🟢 Загружаем SVG: {file_path}')
            try:
                if self.width and self.height:
                    png_data = cairosvg.svg2png(
                        url=file_path,
                        output_width=self.width,
                        output_height=self.height
                    )
                else:
                    png_data = cairosvg.svg2png(url=file_path)
                
                image_bytes = io.BytesIO(png_data)
                return PILImage.open(image_bytes).convert('RGBA')
                
            except Exception as e:
                self.logger.error(f'🔴 Ошибка конвертации SVG: {e}')
                raise
        
        else:
            return PILImage.open(file_path)

    def _is_base64(self, img_str: str) -> bool:
        """Проверяет, является ли строка base64."""

        if not img_str or not isinstance(img_str, str):
            return False
        
        if img_str.startswith('data:image'):
            return True
        
        return False

    def _decode_base64_image(self, base64_str: str) -> PILImage.Image:
        """Декодирует base64 строку в PIL Image."""

        try:
            if 'data:image/svg+xml' in base64_str:

                if base64_str.startswith('data:image'):
                    base64_str = base64_str.split(',')[1]
                
                svg_data = base64.b64decode(base64_str).decode('utf-8')
                
                png_data = cairosvg.svg2png(
                    bytestring=svg_data.encode('utf-8'),
                    output_width=self.width or 500,
                    output_height=self.height or 500
                )
                
                image_bytes = io.BytesIO(png_data)
                return PILImage.open(image_bytes).convert('RGBA')
            
            if base64_str.startswith('data:image'):
                base64_str = base64_str.split(',')[1]
            
            image_data = base64.b64decode(base64_str)
            image_bytes = io.BytesIO(image_data)
            return PILImage.open(image_bytes)
            
        except Exception as e:
            self.logger.error(f'🔴 Ошибка декодирования base64: {e}')
            raise


    def _apply_border_radius(self, image: PILImage.Image, radius: int) -> PILImage.Image:
        """Применяет скругление углов к изображению."""

        try:
        
            self.logger.info(f'🟢 Применяем скругление углов: {radius}px')
             

            if radius <= 0:
                return image

            result_img = image 
            if result_img.mode != 'RGBA':
                result_img = result_img.convert('RGBA')
                self.logger.info('🟢 Изображение конвертировано в RGBA')

            # Если радиус больше половины размера - делаем круг
            min_side = min(result_img.width, result_img.height)
            if radius >= min_side // 2:
                self.logger.info(f'🟢 Радиус {radius}px >= половины размера ({min_side // 2}px), создаём круг')
                return self._make_circle(result_img)
            
            # Иначе делаем скруглённые углы
            mask = PILImage.new('L', result_img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle(
                [(0, 0), result_img.size],
                radius=radius,
                fill=255
            )
            
            result_img.putalpha(mask)
            
            self.logger.info(f'🟢 Скругление углов применено: {radius}px')
            return result_img

        except Exception as e:
            self.logger.error(f'🔴 Не удалось применить скругление углов: {e}')
            return image


    def _make_circle(self, image: PILImage.Image) -> PILImage.Image:
        """Превращает квадратное изображение в круг."""
        
        size = min(image.width, image.height)
        
        left = (image.width - size) // 2
        top = (image.height - size) // 2
        image = image.crop((left, top, left + size, top + size))
        
        mask = PILImage.new('L', (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse([(0, 0), (size, size)], fill=255)
        
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        image.putalpha(mask)
        
        self.logger.info(f'🟢 Изображение превращено в круг: {size}x{size}')
        return image
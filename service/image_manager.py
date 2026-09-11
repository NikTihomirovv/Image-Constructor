import base64
import io
import logging
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

from PIL import Image as PILImage

from config_loader import config
from decorators.def_decorators import handle_errors
from elements.factory import ElementFactory
from models.dataclasses import Canvas, Image, Text
from patterns.patterns import PatternFactory


class ImageManager:
    """Менеджер для создания изображений."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.img_constructor_factory = ImgConstructorFactory()
        self.pattern_factory = PatternFactory()


    def create_custom(self, data: List[Dict]) -> List[Dict] | None:
        """Создает изображение."""

        if not data or not isinstance(data, list):
            self.logger.error('🔴 Ошибка в получении параметров')
            return None

        result = []
        for idx, item in enumerate(data, 1):
            try:
                self.logger.info(f'🟢 Создаем изображение {idx}')

                if not item or not isinstance(item, dict):
                    self.logger.error('🔴 Элемент не является словарём')
                    continue

                # --- Верхний уровень ---
                required_fields = ['name', 'platform_name', 'canvas']
                missing = [f for f in required_fields if item.get(f) is None]
                if missing:
                    self.logger.error(f'🔴 Ошибка в получении параметров, отсутствуют: {missing}')
                    continue

                name = item.get('name')
                platform_name = item.get('platform_name')
                canvas = item.get('canvas')

                # --- Канвас ---
                required_fields = ['name', 'width', 'height', 'bg_color', 'color_mode', 'images', 'texts']
                missing = [f for f in required_fields if canvas.get(f) is None]
                if missing:
                    self.logger.error(f'🔴 Ошибка в получении параметров канваса, отсутствуют: {missing}')
                    continue

                canvas_images = canvas.get('images')
                canvas_texts = canvas.get('texts')

                # --- Картинки ---
                images = []
                image_required = ['img', 'width', 'height', 'x', 'y', 'z', 'border_radius']
                for canvas_image in canvas_images:
                    missing = [f for f in image_required if canvas_image.get(f) is None]
                    if missing:
                        self.logger.error(f'🔴 Ошибка в параметрах картинки, отсутствуют: {missing}')
                        return None

                    images.append(Image(
                        img=canvas_image.get('img'),
                        width=canvas_image.get('width'),
                        height=canvas_image.get('height'),
                        x=canvas_image.get('x'),
                        y=canvas_image.get('y'),
                        z=canvas_image.get('z'),
                        border_radius=canvas_image.get('border_radius'),
                    ))

                # --- Тексты ---
                texts = []
                text_required = [
                    'text', 'font', 'size', 'color', 'width', 'height',
                    'x', 'y', 'z', 'alignment_x', 'alignment_y',
                    'line_height', 'letter_spacing',
                ]
                for canvas_text in canvas_texts:
                    missing = [f for f in text_required if canvas_text.get(f) is None]
                    if missing:
                        self.logger.error(f'🔴 Ошибка в параметрах текста, отсутствуют: {missing}')
                        return None

                    texts.append(Text(
                        text=canvas_text.get('text'),
                        font=canvas_text.get('font'),
                        size=canvas_text.get('size'),
                        color=canvas_text.get('color'),
                        width=canvas_text.get('width'),
                        height=canvas_text.get('height'),
                        x=canvas_text.get('x'),
                        y=canvas_text.get('y'),
                        z=canvas_text.get('z'),
                        alignment_x=canvas_text.get('alignment_x'),
                        alignment_y=canvas_text.get('alignment_y'),
                        line_height=canvas_text.get('line_height'),
                        letter_spacing=canvas_text.get('letter_spacing'),
                    ))

                # --- Сборка канваса ---
                custom_pattern = Canvas(
                    name=canvas.get('name'),
                    width=canvas.get('width'),
                    height=canvas.get('height'),
                    bg_color=canvas.get('bg_color'),
                    color_mode=canvas.get('color_mode'),
                    images=images,
                    textes=texts,
                )

                obj = self.img_constructor_factory.create(custom_pattern)
                img = obj.create()

                if not img:
                    self.logger.error('🔴 Ошибка в создании изображения')
                    continue

                if config.SAVE_TO_FOLDER:
                    self._save_to_folder(img, name, platform_name, 'custom_pattern')

                img_converted = self._image_to_base64(img)

                if not img_converted:
                    self.logger.error('🔴 Ошибка при конвертации')
                    continue

                result.append({'name': name, 'img': img_converted})

            except Exception as e:
                self.logger.exception(f'🔴 Не удалось создать изображение: {e}')
                continue

        if result:
            return result

        return None
        

    @handle_errors
    def create_from_pattern(self, data: List[Dict]) -> List[Dict] | None:
        """Создает изображение."""

        self.logger.info('🟢 Начинаем создание изображений')

        if not data or not isinstance(data, list):
            self.logger.error('🔴 Ошибка в получении параметров')
            return None

        result = []
        for idx, item in enumerate(data, 1):

            self.logger.info(f'🟢 Создаем изображение {idx}')

            if not item or not isinstance(item, dict):
                self.logger.error('🔴 Ошибка в получении параметров')
                continue

            required_fields = ['name', 'platform_name', 'pattern_name', 'pattern_elements']
            if not all(item.get(field) for field in required_fields):
                self.logger.error('🔴 Ошибка в получении параметров')
                continue

            name = item.get('name')
            platform_name = item.get('platform_name')
            pattern_name = item.get('pattern_name')
            pattern = self.pattern_factory.create(item)
            obj = self.img_constructor_factory.create(pattern)
            img = obj.create()

            if not img:
                self.logger.error('🔴 Ошибка в создании изображения')
                continue

            if config.SAVE_TO_FOLDER:
                self._save_to_folder(img, name, platform_name, pattern_name)  

            img_converted = self._image_to_base64(img)

            if not img_converted:
                self.logger.error('🔴 Ошибка при конвертации')
                continue

            result.append({'name': name, 'img': img_converted})

        if result and len(result) > 0:
            return result

        else:
            return None


    def _image_to_base64(self, image: PILImage.Image, format: str = 'PNG') -> Optional[str]:
        """Конвертирует PIL Image в base64 строку."""

        try:
            buffer = io.BytesIO()
            image.save(buffer, format=format)
            buffer.seek(0)
        
            return base64.b64encode(buffer.read()).decode('utf-8')
        
        except Exception as e:
            self.logger.error(f'🔴 Не удалось конвертировать картинку: {e}')
            return None

    @handle_errors
    def _save_to_folder(self, image: PILImage.Image, name: str, platform_name: str, pattern_name: str) -> bool:
        """Сохраняет изображение в папку платформы."""
        
        if not config.OUTPUT_DIR:
            self.logger.error('🔴 Не найден путь для сохранения (OUTPUT_DIR не задан)')
            return False
        
        platform_dir = os.path.join(config.OUTPUT_DIR, platform_name)
        
        try:
            os.makedirs(platform_dir, exist_ok=True)
            self.logger.info(f'🟢 Создана папка платформы: {platform_dir}')
        except Exception as e:
            self.logger.error(f'🔴 Не удалось создать папку {platform_dir}: {e}')
            return False
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{name}_{pattern_name}_{timestamp}.png"
        filepath = os.path.join(platform_dir, filename)
        
        try:
            image.save(filepath)
            self.logger.info(f'🟢 Изображение сохранено: {filepath}')
            return True
        
        except Exception as e:
            self.logger.error(f'🔴 Не удалось сохранить изображение: {e}')
            return False


class ImgConstructorFactory:
    """Фабрика для создания изображений."""

    @staticmethod
    def create(pattern):
        return ImgConstructor(pattern)


class ImgConstructor:
    """Класс для создания изображения."""

    def __init__(self, pattern: Canvas):
        self.logger = logging.getLogger(__name__)
        self.element_factory = ElementFactory()
        self.pattern = pattern
        self.canvas = None
        self.sorted_elements = None


    @handle_errors
    def create(self) -> PILImage.Image:
        """Создает готовое изображение."""

        # Собирает все элементы в паттерне и сортирует их по z-index
        success = self._sort_by_z_index()
        if not success or len(self.sorted_elements) == 0:
            return None

        # Создает пустое изображение как канвас-основу для добавления отдельных элементов
        success = self._create_canvas()
        if not success or not self.canvas:
            return None

        # Создает элементы на канвас-основу
        success = self._create_element()
        if not success:
            return None
        
        return self.canvas


    def _create_canvas(self) -> bool:
        """Создает пустое изображение как канвас."""

        self.logger.info('🟢 Создаем пустое изображение')

        width = self.pattern.width
        height = self.pattern.height
        bg_color = self.pattern.bg_color
        color_mode = self.pattern.color_mode

        if None in (width, height, bg_color, color_mode):
            self.logger.error('🔴 Ошибка в получении параметров')
            return False

        self.logger.info(f'🟢 Ширина: {width}')
        self.logger.info(f'🟢 Высота: {height}')
        self.logger.info(f'🟢 Цвет: {bg_color}')
        self.logger.info(f'🟢 Цветовая модель: {color_mode}')

        self.canvas = PILImage.new(
            color_mode, 
            (width, height), 
            bg_color
        )

        if not self.canvas:
            self.logger.error('🔴 Не удалось создать изображение')
            return False

        self.logger.info('🟢 Создано пустое изображение')
        return True


    @handle_errors
    def _sort_by_z_index(self) -> bool:
        """Сортирует элементы паттерна по z-index."""

        self.logger.info('🟢 Сортируем элементы по z-index')

        images = self.pattern.images or []
        textes = self.pattern.textes or []

        if not isinstance(images, list):
            self.logger.error('🔴 images должен быть списком')
            return False

        if not isinstance(textes, list):
            self.logger.error('🔴 textes должен быть списком')
            return False

        elements = images + textes
        elements = sorted(elements, key=lambda el: el.z or 0)

        if not elements:
            self.logger.error('🔴 Нет элементов для отрисовки')
            return False

        self.logger.info(f'🟢 Отсортировано элементов: {len(elements)}.')
        self.sorted_elements = elements
        return True


    @handle_errors
    def _create_element(self) -> bool:
        """Создает элементы через фабрику."""

        for element in self.sorted_elements:
            obj = self.element_factory.create(element, self.canvas)

            if not obj:
                return False

            success = obj.add_element()
            if not success:
                return False

        return True
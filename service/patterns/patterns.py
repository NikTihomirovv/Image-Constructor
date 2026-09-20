from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from models.dataclasses import Canvas, Image, Text
from patterns.simple_patterns.static_patterns_defaults_tg import (
    TG_StaticPattern_1_Defaults, TG_StaticPattern_2_Defaults,
    TG_StaticPattern_3_First_Defaults, TG_StaticPattern_3_Second_Defaults,
    TG_StaticPattern_3_Third_Defaults, TG_StaticPattern_4_First_Defaults,
    TG_StaticPattern_4_Second_Defaults, TG_StaticPattern_4_Third_Defaults)
from patterns.simple_patterns.static_patterns_defaults_vk import (
    VK_StaticPattern_1_Defaults, VK_StaticPattern_2_Defaults,
    VK_StaticPattern_3_First_Defaults, VK_StaticPattern_3_Second_Defaults,
    VK_StaticPattern_3_Third_Defaults, VK_StaticPattern_4_First_Defaults,
    VK_StaticPattern_4_Second_Defaults, VK_StaticPattern_4_Third_Defaults)


# ============================================================================
# БАЗОВЫЕ КЛАССЫ
# ============================================================================
class Pattern(ABC):
    """Абстрактный базовый класс для всех паттернов."""
    
    @abstractmethod
    def validate(self, data: dict[str, Any]) -> bool:
        pass
    
    @abstractmethod
    def create(self, data: dict[str, Any]) -> Optional[Canvas]:
        pass


class BasePattern(Pattern):
    """Базовый класс с автоматическим созданием Canvas."""
    
    def _get_image_count(self) -> int:
        """Автоматически определяет количество изображений по наличию IMAGE_N_* атрибутов."""
        count = 0
        d = self.defaults_class
        while hasattr(d, f'IMAGE_{count + 1}_WIDTH'):
            count += 1
        return count

    def _get_text_count(self) -> int:
        """Автоматически определяет количество текстов по наличию TEXT_N_* атрибутов."""
        count = 0
        d = self.defaults_class
        while hasattr(d, f'TEXT_{count + 1}_FONT'):
            count += 1
        return count

    def _build_image_mappings(self) -> list[dict]:
        """Автоматически строит маппинги для изображений."""
        mappings = []
        for i in range(1, self._get_image_count() + 1):
            mappings.append({
                'key': f'img_{i}',  # ← всегда с индексом
                'width': f'IMAGE_{i}_WIDTH',
                'height': f'IMAGE_{i}_HEIGHT',
                'x': f'IMAGE_{i}_X',
                'y': f'IMAGE_{i}_Y',
                'z': f'IMAGE_{i}_Z',
                'border_radius': f'IMAGE_{i}_BORDER_RADIUS',
                'rotation': f'IMAGE_{i}_ROTATION',
                'opacity': f'IMAGE_{i}_OPACITY',
                'flip_x': f'IMAGE_{i}_FLIP_X',
                'flip_y': f'IMAGE_{i}_FLIP_Y',
            })
        return mappings

    def _build_text_mappings(self) -> list[dict]:
        """Автоматически строит маппинги для текстов."""
        
        mappings = []
        for i in range(1, self._get_text_count() + 1):
            mappings.append({
                'key': f'text_{i}',  # ← всегда с индексом
                'font': f'TEXT_{i}_FONT',
                'size': f'TEXT_{i}_SIZE',
                'color': f'TEXT_{i}_COLOR',
                'width': f'TEXT_{i}_WIDTH',
                'height': f'TEXT_{i}_HEIGHT',
                'x': f'TEXT_{i}_X',
                'y': f'TEXT_{i}_Y',
                'z': f'TEXT_{i}_Z',
                'alignment_x': f'TEXT_{i}_ALIGNMENT_X',
                'alignment_y': f'TEXT_{i}_ALIGNMENT_Y',
                'line_height': f'TEXT_{i}_LINE_HEIGHT',
                'letter_spacing': f'TEXT_{i}_LETTER_SPACING',
            })
        return mappings

    def _get_required_fields(self) -> list[str]:
        """Возвращает список обязательных полей с индексами."""
        fields = []
        for i in range(1, self._get_image_count() + 1):
            fields.append(f'img_{i}')
        for i in range(1, self._get_text_count() + 1):
            fields.append(f'text_{i}')
        return fields

    
    def validate(self, data: dict[str, Any]) -> bool:
        """Проверяет наличие всех обязательных полей."""
        if not data or not isinstance(data, dict):
            return False
        
        elements = data.get('pattern_elements')
        if not elements or not isinstance(elements, dict):
            return False
        
        required = self._get_required_fields()
        for field in required:
            value = elements.get(field)
            if not value or not isinstance(value, str):
                return False
        
        return True
    
    def create(self, data: dict[str, Any]) -> Optional[Canvas]:
        if not self.defaults_class:
            return None
        
        elements = data.get('pattern_elements', {})
        d = self.defaults_class
        
        # Создаем изображения
        images = []
        for mapping in self._build_image_mappings():
            img_data = elements.get(mapping['key'])
            if img_data:
                images.append(Image(
                    img=img_data,
                    width=getattr(d, mapping['width']),
                    height=getattr(d, mapping['height']),
                    x=getattr(d, mapping['x']),
                    y=getattr(d, mapping['y']),
                    z=getattr(d, mapping['z']),
                    border_radius=getattr(d, mapping['border_radius']),
                    rotation=getattr(d, mapping['rotation'], 0),
                    opacity=getattr(d, mapping['opacity'], 1.0),
                    flip_x=getattr(d, mapping['flip_x'], False),
                    flip_y=getattr(d, mapping['flip_y'], False),
                ))
        
        # Создаем тексты
        textes = []
        for mapping in self._build_text_mappings():
            text_data = elements.get(mapping['key'])
            if text_data:
                textes.append(Text(
                    text=text_data,
                    font=getattr(d, mapping['font']),
                    size=getattr(d, mapping['size']),
                    color=getattr(d, mapping['color']),
                    width=getattr(d, mapping['width']),
                    height=getattr(d, mapping['height']),
                    x=getattr(d, mapping['x']),
                    y=getattr(d, mapping['y']),
                    z=getattr(d, mapping['z']),
                    alignment_x=getattr(d, mapping['alignment_x']),
                    alignment_y=getattr(d, mapping['alignment_y']),
                    line_height=getattr(d, mapping['line_height']),
                    letter_spacing=getattr(d, mapping['letter_spacing']),
                ))
        
        return Canvas(
            name=d.CANVAS_NAME,
            width=d.CANVAS_WIDTH,
            height=d.CANVAS_HEIGHT,
            bg_color=d.CANVAS_BG_COLOR,
            color_mode=d.CANVAS_COLOR_MODE,
            images=images,
            textes=textes,
        )

# ============================================================================
# VK - ПАТТЕРНЫ 
# ============================================================================
class VK_StaticPattern_1(BasePattern):
    defaults_class = VK_StaticPattern_1_Defaults


class VK_StaticPattern_2(BasePattern):
    defaults_class = VK_StaticPattern_2_Defaults


class VK_StaticPattern_3_First(BasePattern):
    defaults_class = VK_StaticPattern_3_First_Defaults


class VK_StaticPattern_3_Second(BasePattern):
    defaults_class = VK_StaticPattern_3_Second_Defaults


class VK_StaticPattern_3_Third(BasePattern):
    defaults_class = VK_StaticPattern_3_Third_Defaults


class VK_StaticPattern_4_First(BasePattern):
    defaults_class = VK_StaticPattern_4_First_Defaults


class VK_StaticPattern_4_Second(BasePattern):
    defaults_class = VK_StaticPattern_4_Second_Defaults


class VK_StaticPattern_4_Third(BasePattern):
    defaults_class = VK_StaticPattern_4_Third_Defaults

# ============================================================================
# TG - ПАТТЕРНЫ
# ============================================================================
class TG_StaticPattern_1(BasePattern):
    defaults_class = TG_StaticPattern_1_Defaults


class TG_StaticPattern_2(BasePattern):
    defaults_class = TG_StaticPattern_2_Defaults


class TG_StaticPattern_3_First(BasePattern):
    defaults_class = TG_StaticPattern_3_First_Defaults


class TG_StaticPattern_3_Second(BasePattern):
    defaults_class = TG_StaticPattern_3_Second_Defaults


class TG_StaticPattern_3_Third(BasePattern):
    defaults_class = TG_StaticPattern_3_Third_Defaults


class TG_StaticPattern_4_First(BasePattern):
    defaults_class = TG_StaticPattern_4_First_Defaults


class TG_StaticPattern_4_Second(BasePattern):
    defaults_class = TG_StaticPattern_4_Second_Defaults


class TG_StaticPattern_4_Third(BasePattern):
    defaults_class = TG_StaticPattern_4_Third_Defaults


# ============================================================================
# ГЛАВНАЯ ФАБРИКА
# ============================================================================

class PatternFactory:
    """Главная фабрика, объединяющая все платформы."""
    
    def __init__(self):
        self._factories: Dict[str, PlatformFactory] = {
            'vk': VKFactory(),
            'tg': TGFactory(),
        }

    def create(self, data: dict[str, Any]) -> Optional[Canvas]:
        platform = data.get('platform_name', 'vk')
        factory = self._factories.get(platform)
        return factory.create(data) if factory else None


# ============================================================================
# ФАБРИКИ ПЛАТФОРМ
# ============================================================================
class PlatformFactory(ABC):
    """Абстрактная фабрика для платформы."""
    
    @abstractmethod
    def create_pattern(self, pattern_name: str) -> Optional['Pattern']:
        pass
    
    def create(self, data: dict[str, Any]) -> Optional[Canvas]:
        pattern_name = data.get('pattern_name')
        pattern = self.create_pattern(pattern_name)
        if pattern and pattern.validate(data):
            return pattern.create(data)
        return None



class VKFactory(PlatformFactory):
    def __init__(self):
        self._patterns: Dict[str, Pattern] = {
            'vk_static_pattern_1': VK_StaticPattern_1(),
            'vk_static_pattern_2': VK_StaticPattern_2(),
            'vk_static_pattern_3_first': VK_StaticPattern_3_First(),
            'vk_static_pattern_3_second': VK_StaticPattern_3_Second(),
            'vk_static_pattern_3_third': VK_StaticPattern_3_Third(),
            'vk_static_pattern_4_first': VK_StaticPattern_4_First(),
            'vk_static_pattern_4_second': VK_StaticPattern_4_Second(),
            'vk_static_pattern_4_third': VK_StaticPattern_4_Third(),
        }
    
    def create_pattern(self, pattern_name: str) -> Optional[Pattern]:
        return self._patterns.get(pattern_name)


class TGFactory(PlatformFactory):
    def __init__(self):
        self._patterns: Dict[str, Pattern] = {
            'tg_static_pattern_1': TG_StaticPattern_1(),
            'tg_static_pattern_2': TG_StaticPattern_2(),
            'tg_static_pattern_3_first': TG_StaticPattern_3_First(),
            'tg_static_pattern_3_second': TG_StaticPattern_3_Second(),
            'tg_static_pattern_3_third': TG_StaticPattern_3_Third(),
            'tg_static_pattern_4_first': TG_StaticPattern_4_First(),
            'tg_static_pattern_4_second': TG_StaticPattern_4_Second(),
            'tg_static_pattern_4_third': TG_StaticPattern_4_Third(),
        }
    
    def create_pattern(self, pattern_name: str) -> Optional[Pattern]:
        return self._patterns.get(pattern_name)
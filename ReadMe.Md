<h1 align="center">🖼️ ImageConstructor</h1>

<p align="center">
  <b>Сервис сборки изображений для VK и Telegram</b><br>
  Принимает JSON-описание — возвращает готовое изображение в base64.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/Pillow-12.0-3776AB.svg" alt="Pillow">
  <img src="https://img.shields.io/badge/docker-ready-blue.svg" alt="Docker">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="License">
</p>

<p align="center">
  <img src="docs/demo.gif" alt="Demo" width="700">
</p>

---

## ✨ Возможности

- 🎨 **16 готовых статических паттернов** — 8 для VK, 8 для Telegram
- 🧩 **Кастомные паттерны** — полный контроль над канвасом, изображениями и текстом
- 🖼️ **Форматы:** JPG, PNG, SVG (включая base64)
- 📐 **Точное позиционирование** — x, y, z-index, скругление углов
- 🔤 **Работа с текстом** — переносы, выравнивание, межбуквенный интервал, кеш шрифтов
- ⚡ **FastAPI + async** — CPU-bound отрисовка вынесена в threadpool
- 🐳 **Docker из коробки** — healthcheck, read-only volumes

## 🚀 Быстрый старт

### Локально

```bash
git clone https://github.com/<user>/ImageConstructor.git
cd ImageConstructor

python -m venv venv
venv/Scripts/activate          # Windows
# source venv/bin/activate     # Linux/macOS

pip install -r requirements.txt

cd service
python run.py                  # http://127.0.0.1:8000
```

### Docker

```bash
docker compose up --build -d
```

API поднимется на `http://localhost:8000`, документация — на `/api/docs`.

## 📖 API

### `POST /api/v1/create_from_static_patterns`

Готовые паттерны — достаточно передать пути к изображениям и текст.

```bash
curl -X POST http://localhost:8000/api/v1/create_from_static_patterns \
  -H "Content-Type: application/json" \
  -d '[
    {
      "name": "VK Static Pattern 1",
      "platform_name": "vk",
      "pattern_name": "vk_static_pattern_1",
      "pattern_elements": {
        "img_1": "static_patterns/vk/vk_static_pattern_img_1080_900.jpg",
        "text_1": "Текст\nСтрока 2\nСтрока 3"
      }
    }
  ]'
```

<details>
<summary>Пример ответа</summary>

```json
{
  "success": true,
  "total": 1,
  "images": [
    {
      "name": "VK Static Pattern 1",
      "img": "iVBORw0KGgoAAAANSUhEUg..."
    }
  ]
}
```
</details>

### `POST /api/v1/create_custom`

Полное описание канваса: изображения и тексты с координатами, шрифтами и z-index.

```json
[
  {
    "name": "Custom Post",
    "platform_name": "vk",
    "canvas": {
      "name": "custom_canvas",
      "width": 1080,
      "height": 1350,
      "bg_color": "#FFFFFF",
      "color_mode": "RGB",
      "images": [
        {
          "img": "static_patterns/vk/vk_static_pattern_img_1080_450.jpg",
          "width": 1080,
          "height": 450,
          "x": 0,
          "y": 0,
          "z": 1,
          "border_radius": 0
        }
      ],
      "texts": [
        {
          "text": "Основной текст поста",
          "font": "inner.ttf",
          "size": 40,
          "color": "#FFFFFF",
          "width": 980,
          "height": 750,
          "x": 50,
          "y": 500,
          "z": 3,
          "alignment_x": "left",
          "alignment_y": "top",
          "line_height": 10,
          "letter_spacing": 0
        }
      ]
    }
  }
]
```

### `GET /health`

Liveness / readiness probe.

## 🧩 Доступные паттерны

| Паттерн | Платформа | Назначение |
|---|---|---|
| `*_static_pattern_1` | VK / TG | Текст + фоновое изображение |
| `*_static_pattern_2` | VK / TG | Текст + линия + фон |
| `*_static_pattern_3_first` | VK / TG | Полноэкранный фон + заголовок + свайп |
| `*_static_pattern_3_second` | VK / TG | Полноэкранный фон + текст + свайп |
| `*_static_pattern_3_third` | VK / TG | Полноэкранный фон + текст |
| `*_static_pattern_4_first` | VK / TG | Картинка сверху + заголовок + логотип + свайп |
| `*_static_pattern_4_second` | VK / TG | Картинка сверху + текст + логотип + свайп |
| `*_static_pattern_4_third` | VK / TG | Картинка сверху + текст + логотип |

Полное описание — в [`Patterns.Md`](Patterns.Md).

## 🏗️ Структура проекта

```
ImageConstructor/
├── docker-compose.yml
├── requirements.txt
├── Patterns.Md              # Описание паттернов
└── service/
    ├── run.py               # Точка входа
    ├── config.yaml          # Настройки
    ├── config_loader.py
    ├── image_manager.py     # Оркестрация сборки
    ├── api/                 # FastAPI: роуты, middleware, DI
    │   ├── main.py
    │   ├── middleware/
    │   └── routes/
    ├── elements/            # Отрисовка (Pillow, cairosvg)
    │   ├── factory.py
    │   ├── image_element.py
    │   └── text_element.py
    ├── models/              # Датаклассы Canvas, Image, Text
    ├── patterns/            # Фабрики и дефолты паттернов
    ├── decorators/
    ├── resources/           # Изображения, SVG
    ├── fonts/               # Шрифты
    └── output/              # Сохранённые изображения
```

## 🛠️ Стек

- **Python 3.11+**
- **FastAPI** + **Uvicorn** — HTTP-слой
- **Pillow** — растровая графика
- **cairosvg** — конвертация SVG
- **PyYAML** — конфигурация
- **Docker / docker-compose** — деплой

## ⚙️ Конфигурация

Основные настройки в `service/config.yaml`:

```yaml
storage:
  save_to_folder: true
  output_dir: "output/"
  fonts_dir: "fonts/"
  resources_dir: "resources/"

logging:
  level: "DEBUG"
  format: "%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s"
```

## 📄 Лицензия

MIT — см. [LICENSE](LICENSE).

---


# Advanced File System Project (Python)

## 📚 Описание

Этот проект демонстрирует продвинутую работу с файловой системой в Python:

- создание и управление папками
- работа с текстами в разных кодировках (UTF-8, ISO-8859-1)
- преобразование текста (смена регистра)
- сериализация данных в JSON
- сбор метаданных файлов
- резервное копирование и восстановление (ZIP)
- валидация JSON по схеме
- генерация отчёта о выполнении

---

## 📁 Структура проекта

project_root/
├── data/
│ ├── raw/
│ ├── processed/
├── logs/
├── backups/
├── output/
└── restored_data/


---

## 🛠 Скрипты

| Скрипт | Назначение |
|--------|------------|
| `create_structure.py` | Создание структуры проекта |
| `write_raw_files.py` | Запись файлов с разными кодировками |
| `process_files.py` | Обработка текста: смена регистра |
| `serialize_to_json.py` | Сериализация содержимого файлов в JSON |
| `file_info.py` | Сбор метаинформации о файлах |
| `validate_json.py` | Проверка JSON через JSON Schema |
| `backup_restore.py` | Архивация и восстановление данных |
| `generate_report.py` | Финальный отчёт по проекту |

---

## 📦 Выходные данные

Все результаты сохраняются в `project_root/output/`:

- `processed_data.json` — оригинальные и обработанные тексты
- `file_info.json` — метаинформация о файлах
- `report.json` — отчёт по выполнению задания

---

## ▶️ Как запустить

Выполняйте скрипты по очереди в терминале:

```bash
python create_structure.py
python write_raw_files.py
python process_files.py
python serialize_to_json.py
python file_info.py
python validate_json.py
python backup_restore.py
python generate_report.py


📌 Требования
Python 3.8+

Установить библиотеку:
pip install jsonschema

👤 Автор
Проект выполнен в рамках задания на тему «Работа с файлами, путями, сериализацией и резервным копированием в Python».


📌 Сохрани как `README.md` и закоммить:

```bash
git add README.md
git commit -m "Добавлен README с описанием проекта"
git push


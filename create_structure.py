# Скрипт для создания базовой структуры проекта
# Создает папки data/raw, data/processed, logs, backups, output внутри project_root

from pathlib import Path

def create_project_structure():
    base_path = Path("project_root")
    dirs = [
        "data/raw",
        "data/processed",
        "logs",
        "backups",
        "output"
    ]

    for dir in dirs:
        path = base_path / dir
        path.mkdir(parents=True, exist_ok=True)  # создаёт директории, если не существуют

    print("✅ Структура проекта создана.")

if __name__ == "__main__":
    create_project_structure()

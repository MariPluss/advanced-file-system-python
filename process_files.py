# Скрипт читает все файлы из data/raw, меняет регистр букв и сохраняет новые версии в data/processed

from pathlib import Path

def swap_case(text):
    return text.swapcase()

def process_files():
    raw_dir = Path("project_root/data/raw")
    processed_dir = Path("project_root/data/processed")

    for file in raw_dir.iterdir():
        try:
            content = file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = file.read_text(encoding="ISO-8859-1")

        transformed = swap_case(content)
        new_name = file.stem + "_processed" + file.suffix
        new_path = processed_dir / new_name
        new_path.write_text(transformed, encoding="utf-8")

    print("✅ Обработка файлов завершена.")

if __name__ == "__main__":
    process_files()

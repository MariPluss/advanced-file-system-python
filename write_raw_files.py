# Скрипт создает два текстовых файла с разными кодировками в папке data/raw
# Записывает лог о создании файлов в logs/log.txt

from pathlib import Path
from datetime import datetime

def write_sample_files():
    base_path = Path("project_root/data/raw")
    samples = {
        "utf8_file.txt": ("Привет, как дела?", "utf-8"),
        "latin1_file.txt": ("Bonjour, ça va?", "ISO-8859-1"),
    }

    for filename, (text, encoding) in samples.items():
        path = base_path / filename
        with open(path, "w", encoding=encoding) as f:
            f.write(text)

    # Логируем в файл
    log_path = Path("project_root/logs/log.txt")
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] Файлы записаны: {', '.join(samples.keys())}\n")

    print("✅ Файлы созданы и лог записан.")

if __name__ == "__main__":
    write_sample_files()

# Сериализует обработанные файлы из data/processed в JSON
# Сохраняет информацию: имя файла, оригинальный и преобразованный текст, размер и дату

import json
from pathlib import Path
from datetime import datetime

def serialize_processed_files():
    processed_dir = Path("project_root/data/processed")
    output_file = Path("project_root/output/processed_data.json")
    data = []

    for file in processed_dir.iterdir():
        content = file.read_text(encoding="utf-8")
        swapped = content.swapcase()
        info = {
            "filename": file.name,
            "original_text": content,
            "swapped_text": swapped,
            "size_bytes": file.stat().st_size,
            "last_modified": datetime.fromtimestamp(file.stat().st_mtime).isoformat()
        }
        data.append(info)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("✅ JSON-файл успешно создан.")

if __name__ == "__main__":
    serialize_processed_files()

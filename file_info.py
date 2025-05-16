# Класс FileInfo собирает метаинформацию о файлах в data/processed и сохраняет в JSON

import json
from pathlib import Path
from datetime import datetime

class FileInfo:
    def __init__(self, path: Path):
        self.filename = path.name
        self.full_path = str(path.resolve())
        self.size = path.stat().st_size
        self.created = datetime.fromtimestamp(path.stat().st_ctime).isoformat()
        self.modified = datetime.fromtimestamp(path.stat().st_mtime).isoformat()

    def to_dict(self):
        return self.__dict__

def collect_file_infos():
    processed_dir = Path("project_root/data/processed")
    infos = [FileInfo(f).to_dict() for f in processed_dir.iterdir()]
    output_path = Path("project_root/output/file_info.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(infos, f, indent=4, ensure_ascii=False)

    print(f"✅ Информация о файлах сохранена в {output_path}")

if __name__ == "__main__":
    collect_file_infos()

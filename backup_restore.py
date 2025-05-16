# Скрипт создает ZIP-архив всей папки data и восстанавливает его в папку restored_data

import shutil
from datetime import datetime
from pathlib import Path

def create_backup():
    date_str = datetime.now().strftime("%Y%m%d")
    backup_dir = Path("project_root/backups")
    backup_dir.mkdir(exist_ok=True)
    archive_name = backup_dir / f"backup_{date_str}"
    shutil.make_archive(str(archive_name), 'zip', "project_root/data")
    print(f"✅ Архив создан: {archive_name}.zip")

def restore_backup():
    date_str = datetime.now().strftime("%Y%m%d")
    archive_path = Path(f"project_root/backups/backup_{date_str}.zip")
    restore_path = Path("project_root/restored_data")
    restore_path.mkdir(exist_ok=True)
    shutil.unpack_archive(str(archive_path), str(restore_path), 'zip')
    print(f"✅ Архив восстановлен в: {restore_path}")

if __name__ == "__main__":
    create_backup()
    restore_backup()

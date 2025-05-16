# Создает отчет в формате JSON с описанием процесса выполнения проекта

import json
from datetime import datetime

report = {
    "summary": {
        "created_at": datetime.now().isoformat(),
        "challenges": [
            "Работа с кодировками (ISO-8859-1, UTF-8)",
            "Обработка ошибок чтения/записи",
            "Создание архива и восстановление"
        ],
        "time_spent": {
            "structure_setup": "10 мин",
            "file_creation": "10 мин",
            "processing": "15 мин",
            "serialization": "15 мин",
            "backup_restore": "10 мин",
            "schema_validation": "10 мин"
        },
        "conclusions": "Проект охватывает работу с файловой системой, логами, сериализацией и проверкой схем. Отличная практика.",
        "improvements": "Добавить больше логирования и сделать CLI-интерфейс."
    }
}

with open("project_root/output/report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4, ensure_ascii=False)

print("✅ Отчёт сохранён: project_root/output/report.json")

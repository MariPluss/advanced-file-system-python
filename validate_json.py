# Валидация JSON-файла file_info.json с помощью JSON Schema

import json
from jsonschema import validate, ValidationError

# JSON Schema для файла file_info.json
schema = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["filename", "full_path", "size", "created", "modified"],
        "properties": {
            "filename": {"type": "string"},
            "full_path": {"type": "string"},
            "size": {"type": "number"},
            "created": {"type": "string", "format": "date-time"},
            "modified": {"type": "string", "format": "date-time"},
        }
    }
}

def validate_json_file():
    try:
        with open("project_root/output/file_info.json", encoding="utf-8") as f:
            data = json.load(f)

        validate(instance=data, schema=schema)
        print("✅ JSON соответствует схеме.")
    except ValidationError as e:
        print("❌ Ошибка валидации:", e)

if __name__ == "__main__":
    validate_json_file()

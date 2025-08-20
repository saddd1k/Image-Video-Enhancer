import os
import json

PRESETS_FILE = "presets.json"

def load_presets():
    if not os.path.exists(PRESETS_FILE):
        return {}
    with open(PRESETS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    data.pop("paths", None)
    return data

def save_presets(presets):
    data = {}
    if os.path.exists(PRESETS_FILE):
        with open(PRESETS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    paths = data.get("paths", {})
    data = presets.copy()
    if paths:
        data["paths"] = paths
    with open(PRESETS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_last_paths():
    data = {}
    if os.path.exists(PRESETS_FILE):
        with open(PRESETS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    return data.get("paths", {})

def save_last_paths(
    output_img=None,
    output_unique=None,
    output_vid=None,
    output_interpolate=None,
    ffmpeg_path=None,
    language=None,
    theme=None
):
    data = {}
    if os.path.exists(PRESETS_FILE):
        with open(PRESETS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    data.setdefault("paths", {})
    if output_img is not None:
        data["paths"]["output_folder_image"] = output_img
    if output_vid is not None:
        data["paths"]["output_folder_video"] = output_vid
    if output_interpolate is not None:
        data["paths"]["output_folder_interpolate"] = output_interpolate
    if ffmpeg_path is not None:
        data["paths"]["ffmpeg_path"] = ffmpeg_path
    if language is not None:
        data["paths"]["language"] = language
    if theme is not None:
        data["paths"]["theme"] = theme
    with open(PRESETS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

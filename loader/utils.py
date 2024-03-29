import json
from config import *
from exceptions import WrongImgType


def save_picture(picture):
    """Функция сохранения картинки"""
    
    allowed_type = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgType(f"Неверный формат файла! Допустимы только {', '.join(allowed_type)}")

    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path


def add_post(post_list, post):
    """Функция добавления поста"""

    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)

#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()

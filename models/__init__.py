#!/usr/bin/python3
"""__init__ magic method for models directory"""

from models.source.FileSys import FileStorage


storage = FileStorage()
storage.reload()

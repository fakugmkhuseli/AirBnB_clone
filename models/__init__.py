#!/usr/bin/python3
"""___init__ method for models directory."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

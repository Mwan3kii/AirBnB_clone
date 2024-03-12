#!/usr/bin/python3
"""Calls and saves to filestorage"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

from .engine.file_storage import FileStorage

storage = FileStorage()

# Reload the objects from the storage
storage.reload()

from models.engine.file_storage import FileStorage


# Instantiate a FileStorage object
# which will be save as an engine to the DataBase
storage = FileStorage()
# Return all object from the DataBase and
# make it available for user interactivity
storage.reload()

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Handler(FileSystemEventHandler):
    def __init__(self, logger):
        self.logger = logger

    def on_created(self, event):
        self.logger.info(f"Created: {event.src_path}")

    def on_deleted(self, event):
        self.logger.info(f"Deleted: {event.src_path}")

    def on_modified(self, event):
        self.logger.info(f"Modified: {event.src_path}")


def start(path, logger):
    event_handler = Handler(logger)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()
    logger.info(f"Watching: {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

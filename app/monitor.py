from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print("Created:", event.src_path)

    def on_deleted(self, event):
        print("Deleted:", event.src_path)

    def on_modified(self, event):
        print("Modified:", event.src_path)


def start():
    path = "watch_dir"

    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    observer.start()
    print("Watching:", path)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

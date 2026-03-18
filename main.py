from app.monitor import start
from app.logger import setup_logger

if __name__ == "__main__":
    logger = setup_logger()
    start("watch_dir", logger)

from app.monitor import start
from app.logger import setup_logger
from app.config_loader import load_config

if __name__ == "__main__":
    config = load_config()

    logger = setup_logger(
        config["log_file"],
        config["log_level"]
    )

    start(
        config["watch_directory"],
        logger
    )

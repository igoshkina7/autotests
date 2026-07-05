import logging
import os
from datetime import datetime

# создаём папку logs если её нет
os.makedirs("logs", exist_ok=True)

log_filename = datetime.now().strftime("logs/test_run_%Y_%m_%d.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
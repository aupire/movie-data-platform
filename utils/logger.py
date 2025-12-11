import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.basicConfig(
    level=logging.WARNING, format="WARNING %(asctime)s - %(levelname)s - %(message)s"
)
logging.basicConfig(
    level=logging.ERROR,
    format="**** ERROR **** %(asctime)s - %(levelname)s - %(message)s",
)

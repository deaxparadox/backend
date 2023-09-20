import logging

FORMAT = "%(levelname)s:%(message)s"
FILENAME = "logs"
logging.basicConfig(
    filename=FILENAME,
    format=FORMAT,
    level=logging.DEBUG
)

logging.debug("Log sever working")
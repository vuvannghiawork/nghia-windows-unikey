from environs import Env
from loguru import logger


log_file_format = "{time:YYYY-MM-DD}.log"
logger.add(f"logging/{log_file_format}", rotation="00:00", retention="7 days", enqueue=True)
logger.info(f"Loading environment variables...")


# Initialize Env
env = Env()
# Read .env file
env.read_env()


FILE_UNIKEY = env.str("FILE_UNIKEY")
logger.info(f"FILE_UNIKEY = {FILE_UNIKEY}")

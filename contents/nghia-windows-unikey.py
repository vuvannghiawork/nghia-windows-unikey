import os
import settings
from loguru import logger


file_main = os.path.abspath(__file__)
logger.info(f"file_main = {file_main}")


nghia_windows_unikey_txt = os.path.join(os.path.dirname(file_main), "nghia-windows-unikey.txt")
logger.info(f"nghia_windows_unikey_txt = {nghia_windows_unikey_txt}")


try:
    if os.path.exists(settings.FILE_UNIKEY):
        os.remove(settings.FILE_UNIKEY)
        print(f"Đã xóa symlink: {settings.FILE_UNIKEY}")
    os.symlink(os.path.abspath(nghia_windows_unikey_txt), settings.FILE_UNIKEY)
    print(f"Tạo link: {settings.FILE_UNIKEY}")
except OSError as e:
    print(f"Lỗi: {e}")

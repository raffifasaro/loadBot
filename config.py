import os
import tempfile
from dotenv import load_dotenv


load_dotenv()

# Bot 
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN")

# Download limits
MAX_FILE_SIZE_BYTES: int = 25 * 1024 * 1024

# Temporary directory for downloaded files (cleaned up after each send)
_OS_TEMP_DIR = os.path.join(tempfile.gettempdir(), "loadBot_downloads")

TEMP_DIR: str = _OS_TEMP_DIR

# Compression settings
COMPRESSION_MODE: bool = False
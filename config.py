import json

# Load configuration from config.json
with open("config.json") as f:
    _config_data = json.load(f)

# Bot 
DISCORD_TOKEN: str = _config_data.get("bot_token", "")

# Download limits
MAX_FILE_SIZE_BYTES: int = 25 * 1024 * 1024

# Temporary directory for downloaded files (cleaned up after each send)
TEMP_DIR: str = _config_data.get("temp_dir", "/tmp/discord_bot_downloads")
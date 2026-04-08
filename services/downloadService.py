import yt_dlp
import config
import os
import pathlib
import uuid


def download_file(url: str) -> str:
    # Create a unique filename for the downloaded file
    unique_filename = f"{uuid.uuid4()}.%(ext)s"
    output_path = os.path.join(config.TEMP_DIR, unique_filename)

    # Ensure the temporary directory exists
    pathlib.Path(config.TEMP_DIR).mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        'outtmpl': output_path,
        'format': 'best',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'max_filesize': config.MAX_FILE_SIZE_BYTES,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=True)
            if info_dict is None:
                raise Exception("Failed to extract information from the URL.")
            return ydl.prepare_filename(info_dict)
        except Exception as e:
            print(f"Error downloading file: {e}")
            return None
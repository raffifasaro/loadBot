import time
import yt_dlp
import config
import os
import pathlib
import uuid
import subprocess


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
        
def compress_video(input_path, crf=28, preset="medium"):
  
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_compressed.mp4"

    command = [
        "ffmpeg",
        "-i", input_path,
        "-vcodec", "libx264",
        "-crf", str(crf),
        "-preset", preset,
        "-acodec", "aac",
        "-b:a", "128k",
        output_path
    ]

    subprocess.run(command, check=True)

    return output_path


def wait_for_file(path, timeout=30):
    start = time.time()
    while not os.path.exists(path):
        if time.time() - start > timeout:
            return False
        time.sleep(0.5)
    return True
    
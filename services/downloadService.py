import time
import yt_dlp
import config
import os
import pathlib
import uuid
import cv2


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
        
def compress_video(input_path):
  
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_compressed.mp4"

    cap = cv2.VideoCapture(input_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) // 2)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2)
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (width, height))
        out.write(frame)

    cap.release()
    out.release()

    os.remove(input_path)
    return output_path


def wait_for_file(path, timeout=30):
    start = time.time()
    while not os.path.exists(path):
        if time.time() - start > timeout:
            return False
        time.sleep(0.5)
    return True
    
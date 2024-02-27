import os
import threading
import time
from multiprocessing import Process
from pathlib import Path

import requests


def encrypt_file(file_path: Path):
    start_time = time.perf_counter()
    print(f"Processing file from {file_path} in process {os.getpid()}")
    _ = [i for i in range(100_000_000)]
    end_time = time.perf_counter()
    print(f"Time taken for encryption task: {end_time - start_time} seconds")


def download_image(image_url: str):
    start_time = time.perf_counter()
    print(f"Downloading image from {image_url} in process {os.getpid()}")
    response = requests.get(image_url)
    image_path = Path("downloaded_image.jpg")
    with open(image_path, "wb") as f:
        f.write(response.content)
    end_time = time.perf_counter()
    print(f"Time taken for download task: {end_time - start_time} seconds")


if __name__ == "__main__":
    start_time_total = time.perf_counter()

    file_path = Path("rockyou.txt")
    image_url = "https://picsum.photos/1000/1000"

    try:
        thread1 = threading.Thread(target=encrypt_file, args=(file_path,))
        thread2 = threading.Thread(target=download_image, args=(image_url,))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        procces1 = Process(target=encrypt_file, args=(file_path,))
        procces2 = Process(target=download_image, args=(image_url,))

        procces1.start()
        procces2.start()

        procces1.join()
        procces2.join()

        end_time_total = time.perf_counter()
        print(f"Total time taken: {end_time_total - start_time_total} seconds")

    except Exception as e:
        print(f"Error occurred: {e}")

import os
import time
import sys


def clean_logs():
    if len(sys.argv) != 3:
        sys.exit(1)
    log_dir = sys.argv[1]
    threshold = time.time() - (int(sys.argv[2]) * 86400)
    files_to_delete = []

    if not os.path.isdir(log_dir):
        print(f"Ошибка: Директория {log_dir} не найдена.")
        return

    for filename in os.listdir(log_dir):
        if filename.endswith(".log"):
            file_path = os.path.join(log_dir, filename)
            if os.path.getmtime(file_path) < threshold:
                files_to_delete.append(file_path)

    for f in files_to_delete:
        print(f"Найден: {f}")


if __name__ == "__main__":
    clean_logs()

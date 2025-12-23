import sys


def clean_logs():
    if len(sys.argv) != 3:
        sys.exit(1)
    log_dir = sys.argv[1]
    days = sys.argv[2]
    print(f"Сканируем директорию {log_dir} на файлы старше {days} дней...")


if __name__ == "__main__":
    clean_logs()

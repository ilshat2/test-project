import os
import time
import sys


def clean_logs():
    # 1. Проверка аргументов и вывод справки (Задание B1.5)
    if len(sys.argv) != 3:
        print("Справка: скрипт удаляет .log файлы старше N дней.")
        print(f"Использование: python {sys.argv[0]} <путь_к_логам> <количество_дней>")
        sys.exit(1)

    log_dir = sys.argv[1]
    # Вычисляем порог времени
    try:
        days = int(sys.argv[2])
    except ValueError:
        print("Ошибка: количество дней должно быть числом.")
        sys.exit(1)

    threshold = time.time() - (days * 86400)
    files_to_delete = []

    if not os.path.isdir(log_dir):
        print(f"Ошибка: Директория {log_dir} не найдена.")
        return

    # 2. Поиск файлов (Задание B1.2)
    for filename in os.listdir(log_dir):
        if filename.endswith(".log"):
            file_path = os.path.join(log_dir, filename)
            if os.path.getmtime(file_path) < threshold:
                files_to_delete.append(file_path)

    if not files_to_delete:
        print("Старых логов не обнаружено.")
        return

    # 3. Вывод списка файлов (B1.3)
    print(f"\nНайдены следующие файлы (старше {days} дней):")
    for f in files_to_delete:
        print(f" - {os.path.basename(f)}")

    # 4. Подтверждение и удаление (Задание B1.4)
    confirm = input(f"\nУдалить эти файлы ({len(files_to_delete)} шт.)? (y/n): ").lower()

    if confirm == 'y':
        for f in files_to_delete:
            try:
                os.remove(f)
                print(f"Удален: {os.path.basename(f)}")
            except OSError as e:
                print(f"Ошибка при удалении {f}: {e}")
        print("Очистка завершена успешно.")
    else:
        print("Операция отменена.")


if __name__ == "__main__":
    clean_logs()

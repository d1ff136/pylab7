"""
Лабораторна робота №7
Тема: Аналіз та збір статистики файлової системи
Файл: template_lab_7.py
Варіант 9, Варіант А: Загальна статистика каталогу
"""

import locale
import os
import sys
from datetime import datetime


def show_help():
    """
    Виводить коротку інструкцію з використання програми в консоль.
    """
    script_name = os.path.basename(sys.argv[0])

    print(f"""
ОПИС ПРОГРАМИ:
  Рекурсивно обходить вказану папку та всі її підпапки і виводить
  загальну статистику: кількість вкладених підпапок, кількість файлів
  та сумарний розмір усіх файлів у байтах. Також виводиться дата
  і час формування звіту.

ЗАГАЛЬНИЙ СИНТАКСИС:
  python {script_name} <шлях_до_папки>

ПРАПОРЦІ ДОВІДКИ:
  --help, -h, /?     показати цю довідку

ПРИКЛАДИ ВИКЛИКУ:
  python {script_name} ./test
  python {script_name} C:\\Users\\Student\\Documents
  python {script_name} --help
""")


def main():
    # =========================================================================
    # КРОК 1. Робота з аргументами командного рядка (модуль sys)
    # =========================================================================
    help_flags = ("--help", "/?", "-h")

    if len(sys.argv) < 2 or sys.argv[1] in help_flags:
        show_help()
        sys.exit(0)

    dir_path = sys.argv[1]

    # =========================================================================
    # КРОК 2. Перевірка існування директорії (модуль os.path)
    # =========================================================================
    if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
        print(f"Помилка: папку '{dir_path}' не знайдено!", file=sys.stderr)
        sys.exit(1)

    # =========================================================================
    # КРОК 3. Рекурсивний обхід папки та збір статистики (ВАРІАНТ А)
    # =========================================================================
    total_folders = 0
    total_files = 0
    total_size = 0

    for root, dirs, files in os.walk(dir_path):
        total_folders += len(dirs)
        total_files += len(files)

        for file_name in files:
            full_path = os.path.join(root, file_name)
            try:
                total_size += os.path.getsize(full_path)
            except OSError:
                # Файл недоступний або "битий" лінк - пропускаємо
                pass

    # =========================================================================
    # КРОК 4. Дата звіту, регіональна локалізація та виведення результатів
    # =========================================================================
    locale.setlocale(locale.LC_ALL, "")

    report_date = datetime.now().strftime("%d.%m.%Y %H:%M")
    size_str = locale.format_string("%d", total_size, grouping=True)

    print(f"Звіт про папку: {os.path.abspath(dir_path)}")
    print(f"Дата формування: {report_date}")
    print("-" * 40)
    print(f"Кількість підпапок: {total_folders}")
    print(f"Кількість файлів:   {total_files}")
    print(f"Загальний розмір:   {size_str} байт")


if __name__ == "__main__":
    main()

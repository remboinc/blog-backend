import os
from bs4 import BeautifulSoup

# Папка, в которой находятся ваши HTML-шаблоны Django
target_folder = '/Users/ok_user/PycharmProjects/blog_on_django/blog-backend/templates'

# Проход по всем файлам в папке
for root, dirs, files in os.walk(target_folder):
    for filename in files:
        if filename.endswith('.html'):  # Проверяем, что файл - это HTML-шаблон
            file_path = os.path.join(root, filename)

            # Открываем файл для чтения и чтения его содержимого
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()

            # Парсим HTML-код с использованием BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            # Определяем настройки отступов
            formatter = "html"  # Тип форматирования, "html" или "xml"

            # Отформатируем HTML с отступами для лучшей читаемости
            formatted_html = soup.prettify(formatter=formatter)
            # formatted_html = formatted_html.replace("\n", "")
            # Записываем отформатированный HTML обратно в файл
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(formatted_html)

            print(f'Файл {file_path} отформатирован.')


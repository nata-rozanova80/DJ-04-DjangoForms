# Домашнее задание Zerocoder. Урок DJ-04-DjangoForms
Приложене Django, сайт №2, формы, новости

##Задание
- **Создайте проект с именем movie_project и приложение в нем films. Создайте модель(таблицу) в которой будет поле для названия фильма, поле для описание фильма и поле для отзыва.

- **Создайте две html страницы, на одной из которых нужно заполнить 3 поля и отправить эту информацию в базу данных, а на второй будет публиковаться информация которую вы записали в базу данных.

# Movie Project

**Movie Project** — это Django приложение для работы с фильмами. В проекте предусмотрено отображение списка фильмов, создание новых записей и использование форм для ввода данных.

## Структура проекта

Проект состоит из двух основных частей:

- **films** — приложение для работы с фильмами:
  - **models.py** — содержит модель для фильма.
  - **views.py** — содержит логику для отображения и создания фильмов.
  - **forms.py** — форма для добавления нового фильма.
  - **templates/films** — HTML-шаблоны для отображения информации о фильмах.
  - **urls.py** — маршруты для приложения `films`.

- **movie_project** — основной каталог проекта:
  - **settings.py** — настройки проекта, включая подключение базы данных и подключенные приложения.
  - **urls.py** — глобальные маршруты для всего проекта.
  - **wsgi.py** — конфигурация WSGI для развертывания проекта.
  - **asgi.py** — конфигурация ASGI для работы с асинхронными задачами.

## Функции

- **Список фильмов**: Главная страница отображает список всех фильмов, добавленных в систему.
- **Создание фильмов**: Пользователи могут добавлять фильмы, заполняя форму с названием, описанием и отзывом.
- **Админка Django**: Администраторы могут управлять фильмами через административную панель Django.



### Админ-панель
Для доступа к административной панели Django используйте команду для создания суперпользователя:

python manage.py createsuperuser

Затем войдите в панель по адресу http://127.0.0.1:8000/admin.

Модель Film имеет следующие поля:

- **title: Название фильма (строка, до 200 символов).
- **description: Описание фильма (текст).
- **review: Отзыв о фильме (текст).

Примечания
При добавлении нового фильма через форму данные сохраняются в базе данных.
В проекте используется SQLite база данных по умолчанию, которая будет автоматически создана при первом запуске.

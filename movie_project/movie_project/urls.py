from django.contrib import admin
from django.urls import path, include
from films.views import film_list  # Импортируйте представление для списка фильмов

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include('films.urls')),  # Подключите URLs из films
    path('', film_list, name='film_list'),  # Добавьте маршрут для корневого URL
]

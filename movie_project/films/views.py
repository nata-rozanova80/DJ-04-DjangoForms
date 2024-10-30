from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

def film_create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базе данных
            return redirect('film_list')  # Перенаправляем на страницу со списком фильмов
    else:
        form = FilmForm()
    return render(request, 'films/film_create.html', {'form': form})

def film_list(request):
    films = Film.objects.all()  # Получаем все фильмы из базы данных
    return render(request, 'films/film_list.html', {'films': films})
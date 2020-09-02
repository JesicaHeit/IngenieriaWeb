from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import RecetasForm
from Proyecto1 import views
from Proyecto1.views import home

# Create your views here.
def post_new(request):
    if request.method == "POST":
        form = RecetasForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/home')
    else:
        form = RecetasForm()
    return render(request, 'recetas/post_edit.html', {'form': form})
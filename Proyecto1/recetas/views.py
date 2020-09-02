from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import RecetasForm
from Proyecto1 import views
from Proyecto1.views import home
from .models import Receta

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

def post_list(request):
    receta = Receta.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'recetas/post_list.html', {'receta': receta})

def post_detail (request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/post_detail.html', {'receta': receta})

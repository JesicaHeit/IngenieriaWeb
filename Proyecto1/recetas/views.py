from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import RecetasForm
from Proyecto1 import views
from Proyecto1.views import home
from .models import Receta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
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
    ''
    #if request.user.is_authenticated:
    receta = Receta.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'recetas/post_list.html', {'receta': receta})

def post_list2(request):
    if request.user.is_authenticated:
        profile = request.user
        receta = Receta.objects.filter(author=request.user,published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'recetas/post_list2.html', {'page_user': profile,'receta': receta})

def post_detail (request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/post_detail.html', {'receta': receta})

def post_detail2 (request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/post_detail2.html', {'receta': receta})

def post_edit(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == "POST":
        form = RecetasForm(request.POST, instance=receta)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.author = request.user
            receta.published_date = timezone.now()
            receta.save()
            return redirect('post_detail', pk=receta.pk)
    else:
        form = RecetasForm(instance=receta)
    return render(request, 'recetas/post_edit.html', {'form': form})
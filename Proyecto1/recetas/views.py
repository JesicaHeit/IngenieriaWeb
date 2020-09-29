from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Exists, Count
from django.utils import timezone
from .forms import RecetasForm
from Proyecto1 import views
from Proyecto1.views import home
from .models import Receta
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required()
def post_new(request):
    if request.method == "POST":
        form = RecetasForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/receta_user')
    else:
        form = RecetasForm()
    return render(request, 'recetas/post_edit.html', {'form': form})

def post_list(request):
    ''
    #if request.user.is_authenticated:
    receta = Receta.objects.all().annotate(like_count=Count('likes')).order_by('-like_count')
    return render(request, 'recetas/post_list.html', {'receta': receta})

def post_list2(request):
    if request.user.is_authenticated:
        profile = request.user
        receta = Receta.objects.filter(author=request.user,published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'recetas/post_list2.html', {'page_user': profile,'receta': receta})

def post_detail (request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    total_likes=receta.total_likes()
    liked=False
    if receta.likes.filter(id=request.user.id):
        liked=True
    return render(request, 'recetas/post_detail.html', {'receta': receta, 'total_likes':total_likes, 'liked':liked})

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

def borrar_receta(request, pk):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Receta.objects.get(pk=pk)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('receta_user')



def LikeView (request, pk):
    receta = get_object_or_404(Receta, id=request.POST.get('receta_id'))
    liked=True
    if receta.likes.filter(id=request.user.id):
        receta.likes.remove(request.user)
        liked=False
    else:
        receta.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))

@login_required()
def add_comment_to_post(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = receta
            comment.save()
            return redirect('post_detail', pk=receta.pk)
    else:
        form = CommentForm(initial={'author':request.user})
    return render(request, 'Comment/add_comment_to_post.html', {'form': form})
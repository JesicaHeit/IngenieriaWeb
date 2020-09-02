from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse

from .tokens import account_activation_token
from .forms import CustomUserForm

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "users/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save(commit= False)
            user.is_active = False
            user.save()

            uidb64= urlsafe_base64_encode(force_bytes(user.pk)) # crea el token encodeado

            domain = get_current_site(request).domain
            link= reverse('activate', kwargs={'uidb64':uidb64,'token':account_activation_token.make_token(user)}) # arma el link de activacion

            activate_url = domain+link # le agrega el dominio al link

            mail_subject = 'Activa tu cuenta' 

            message = 'Hola '+ user.username + \
                ' Verifica tu cuenta con el siguiente link:\n' + activate_url

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
            mail_subject, message, to=[to_email]
            )
            email.send(fail_silently=False)

            return HttpResponse('Por favor confirme su dirección de correo para completar el registro')
        else:
            form = UserCreationForm(request.POST)
            # Si llegamos al final renderizamos el formulario
            return render(request, "users/register.html", {'form': form})
             
        # Si existe el usuario
        if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/pantalla_intermedia')

    # Si queremos borramos los campos de ayuda
  
  # form.fields['username'].help_text = None
  #  form.fields['password1'].help_text = None
  #  form.fields['password2'].help_text = None

def activate(request, uidb64=None, token=None):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if not account_activation_token.check_token(user,token):
            return HttpResponseRedirect('/login'+'?message='+'El usuario ya esta activado')

        if user.is_active:
            return HttpResponseRedirect('/login')
        user.is_active=True
        user.save()   

        # messages.success(request,'La cuenta se activo correctamente')
        return HttpResponseRedirect('/login')

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

   
    return HttpResponseRedirect('/login')


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/recipes')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
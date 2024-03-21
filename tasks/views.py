from django.shortcuts import render
# creamos el fromulario
from django.contrib.auth.forms import UserCreationForm
# para registrar el usuario
from django.contrib.auth.models import User
# enviamos texto
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    # si es una petición de la web nos muestra el formulario
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    # si son los datos pedidos por post, nos comprueba las contraseñas
    #     y las guarda
    else:
        if request.POST['password1'] == request.POST['password2']:
            # manejo de errores
            try:
                # registrar y crea usuario en user. Espera dos parametros. Usuario y contraseña
                user = User.objects.create_user(username=request.POST['username'], 
                                     password=request.POST['password1'])
                # guardamos el usuario en la DB
                user.save()
                return HttpResponse('User created succesfully')
            # si falla hace el except
            except:
                return HttpResponse('Username already exist')
        return HttpResponse('Password do not match')
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages  # Importation ajoutée ici
from .models import Feature

def index(request):
    features = Feature.objects.all() 
    context = {
        'name': 'Chorouk',
        'features': features 
    }
    return render(request, 'index.html', context)

def counter(request):
    # Sécurité pour éviter l'erreur MultiValueDictKeyError si on accède en GET
    if request.method == 'POST':
        text = request.POST['text']
        amount_of_words = len(text.split())
        return render(request, 'counter.html', {'amount': amount_of_words})
    else:
        return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Ce nom d\'utilisateur est déjà pris.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Cet email est déjà utilisé.')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, 
                    password=password, 
                    email=email, 
                    first_name=first_name, 
                    last_name=last_name
                )
                user.save()
                return redirect('login') 
        else:
            messages.info(request, 'Les mots de passe ne correspondent pas.')
            return redirect('register')
    else:
        return render(request, 'register.html')

# Sortie de l'indentation de register pour ces fonctions
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/') 
        else:
            messages.info(request, 'Nom d\'utilisateur ou mot de passe incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
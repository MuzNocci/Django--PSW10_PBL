from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages



def cadastro(request):

    if request.method == 'GET':

        return render(request, 'cadastro.html')

    elif request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        error = 0

        if username:
            users = User.objects.filter(username=username)
            if users.exists():
                messages.add_message(request, messages.constants.ERROR, 'O usuário informado já existe.')
                error += 1
        else:
            messages.add_message(request, messages.constants.ERROR, 'Você deve informar um nome de usuário.')
            error += 1
        
        if senha != confirmar_senha:
            messages.add_message(request, messages.constants.ERROR, 'A senha e a confirmação de senha são diferentes.')
            error += 1
        
        if len(senha) < 6:
            messages.add_message(request, messages.constants.ERROR, 'A senha deve ter mais de 6 dígitos.')
            error += 1
        
        if error > 0:
            context = {
                'request': request.POST,
            }
            return render(request, 'cadastro.html', context)
        else:
            try:
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=senha,
                )
                messages.add_message(request, messages.constants.SUCCESS, 'Usuário cadastrado com sucesso.')
                return redirect('login')
            except:
                messages.add_message(request, messages.constants.ERROR, 'Não foi possível cadastrar o usuário.')
                return render(request, 'cadastro.html')


def login(request):

    if request.method == "GET":

        return render(request, 'login.html')

    elif request.method == "POST":

        username = request.POST.get('username')
        senha = request.POST.get("senha")
        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('home')
        
        messages.add_message(request, messages.constants.ERROR, 'Usuário ou senha incorretos')
        context = {
            'request': request.POST
        }
        return render(request, 'login.html', context)
    

def logout(request):

    if request.user.is_authenticated:
        auth.logout(request)

    return redirect('login')
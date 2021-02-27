from django.shortcuts import render, HttpResponse, redirect

from .forms import SignInForm, SignUpForm

from django.contrib.auth import get_user_model, login, authenticate, logout

# Create your views here.

# TODO : class base view
def auth(request):
    if not request.user.is_authenticated:
        context = {
            "signInForm" : SignInForm,
            "signUpForm" : SignUpForm,
        }
        return render(request, 'auth/auth.html', context)
    else:
        return redirect('/nd')

def signIn(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignInForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/nd')
                else:
                    return HttpResponse('User not found')
        else:
            return redirect('/')
    else:
        return redirect('/nd')

User = get_user_model()
def signUp(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('/')
            return redirect('/')
    else:
        return redirect('/nd')

def logOut(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            logout(request)
            return redirect('/')
    else:
        return redirect('/nd')
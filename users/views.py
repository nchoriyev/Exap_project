from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect to a success page after saving
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')


def login_view(request, ):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            context = {"message": "Login yoki password xato!"}
            return render(request, 'auth/login.html', context)

    return render(request, "auth/login.html")


def register_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password1']
        user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, "auth/register.html")


def logout_view(request):
    logout(request)
    return redirect('home')




def show_user(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email
        }
        return render(request, 'show_user.html', context)
    else:
        return redirect('login')






from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm, EditUserDetail
from .models import  Profile
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'authenticate/home.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Loggin Successfully ..."))
            return redirect('home')

        else:
            messages.success(request, ('Invalid password or username!'))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been loged out Successfully ..."))
    return redirect('login')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']            
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password,)
            login(request, user)
            messages.success(request, ("Registration was Successfully ..."))
            return redirect('edit_profile')

    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required(login_url='login')
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if request.user.profile:
            update = EditUserDetail(
                request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and update.is_valid():
            form.save()
            update.save()

            messages.success(request, ("Update was Successfully ..."))
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)
        update = EditUserDetail(instance=request.user.profile)
    context = {'form': form, 'update': update}
    return render(request, 'authenticate/edit_profile.html', context)

@login_required(login_url='login')
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # keeps the user login in after the update
            update_session_auth_hash(request, form.user)

            messages.success(request, ("Password Update was Successfully ..."))
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)


from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from home.models import Contacts
# Create your views here.


class RegisterView(View):
    def get(self, request):
        create_form = CustomUserForm()
        context = {
            'form': create_form
        }
        return render(request, 'register.html', context)

    def post(self, request):
        create_form = CustomUserForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'register.html', context)


class LoginView(View):
    def get(self, request):
        create_form = AuthenticationForm()
        context = {
            'form': create_form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        create_form = AuthenticationForm(data=request.POST)
        if create_form.is_valid():
            user = create_form.get_user()
            login(request, user)
            return redirect('home:home')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'login.html', context=context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:home')


class ProfileView(View):
    def get(self, request):
        context = {
            'user': request.user
        }
        return render(request, 'profile.html', context=context)


class ProfileUpdateView(View):
    def get(self, request):
        update_form = ProfileUpdateForm(instance=request.user)
        context = {
            'form': update_form
        }
        return render(request, 'profile_update.html', context=context)

    def post(self, request):
        update_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('users:profile')
        else:
            context = {
                'form': update_form
            }
            return render(request, 'profile_update.html', context=context)
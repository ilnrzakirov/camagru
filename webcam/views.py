from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import RegisterForm
from .models import Post, Profile
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


class HomePageView(ListView):
    model = Post
    template_name = "index.html"

    def get_queryset(self):
        return Post.objects.all().order_by('pub_date')[:10]


class LoginView(LoginView):
    template_name = 'login.html'
    next_page = "home"


class LogoutView(LogoutView):
    next_page = "home"


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            avatar = form.cleaned_data['avatar']
            raw_password = form.cleaned_data.get('password1')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            Profile.objects.create(
                user=user,
                email=email,
                phone=phone,
                avatar=avatar
            )
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', context={'form': form})


def create_photo_view(request):
    return render(request, 'create.html')

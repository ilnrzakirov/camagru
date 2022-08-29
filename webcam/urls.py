
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .views import HomePageView, LogoutView, LoginView, register_view
from django.conf import settings

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('logout/', LogoutView.as_view, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
]


if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
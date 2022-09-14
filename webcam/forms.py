from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from webcam.models import ImageFilter


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=20, required=False, help_text='Фамилия')
    phone = forms.IntegerField(max_value=9999999999, min_value=1111111111, help_text='Номер телефона без 8')
    email = forms.EmailField(max_length=200, required=False, help_text="Электронная почта")
    avatar = forms.FileField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2', 'avatar')


class ImageChoicesForm(forms.Form):
    images = ImageFilter.objects.all()
    choices = []
    for image in images:
        choices.append((image.name, image.name))
    image_name = forms.ChoiceField(choices=choices)

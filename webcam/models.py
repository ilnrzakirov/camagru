from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    phone = models.IntegerField(default=0,
                                validators=[MinValueValidator(1111111111),
                                            MaxValueValidator(9999999999)],
                                verbose_name="Номер телефона")
    email = models.EmailField(max_length=200,
                              blank=True,
                              verbose_name="Электровнная почта",
                              null=True)
    verification = models.BooleanField(default=False,
                                       verbose_name="Верефикация")
    avatar = models.ImageField(default=None,
                               upload_to='img/avatar',
                               verbose_name="Фотография профиля")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.user.username


class Picture(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Заголовок")
    img = models.ImageField(upload_to="img/profile_pictures",
                            verbose_name="Фотография")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображении"

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(Profile,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    text = models.TextField(max_length=500,
                            verbose_name="Комментарий")
    datetime = models.DateTimeField(auto_now=True,
                                    verbose_name="Дата и время")

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return f"{self.user.user.username} + ': ' {self.text}"


class Post(models.Model):
    image = models.ForeignKey(Picture,
                              on_delete=models.CASCADE,
                              verbose_name="Изображение")
    pub_date = models.DateTimeField(verbose_name="Дата и время публикации",
                                    auto_now=True)
    user = models.ForeignKey(Profile,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    comment = models.ManyToManyField(Comment,
                                     verbose_name="Коментарий",
                                     blank=True,
                                     related_name='posts')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.user.user.username} - {self.pub_date}"


class ImageFilter(models.Model):
    image = models.ImageField(upload_to='filter/', verbose_name="Фильтр для снимков")

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры для снимков"

    def __str__(self):
        return self.image.name

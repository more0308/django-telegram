from django.db import models

class Client(models.Model):
    user_id = models.PositiveIntegerField(unique=True, verbose_name='ID пользователя')
    username = models.CharField(max_length=255, verbose_name='Ник')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')
    lastname = models.CharField(max_length=255, blank=True, null=True, verbose_name='Фамилия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Currency(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Слаг')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Криптовалюта'
        verbose_name_plural = 'Криптовалюты'


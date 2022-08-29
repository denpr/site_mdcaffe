from weakref import proxy
from django.db import models
from datetime import datetime, timedelta

class Category(models.Model):
    title = models.CharField('Название категории', max_length=50)
    description = models.TextField('Описание', default='-')
    position = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.position} - {self.title}'

    class Meta:
        verbose_name = 'Меню - Категория'
        verbose_name_plural = 'Меню - Категории'

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    title = models.CharField('Название позиции', max_length=50)
    description = models.TextField('Описание')
    price_float = models.FloatField(default=1.25)
    position = models.IntegerField(default=0)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.category}, приоритет - {self.position}, {self.title}, price -> {self.price_float} BYN'

    class Meta:
        verbose_name = 'Меню - Позиция'
        verbose_name_plural = 'Меню - Позиции'
    
    def get_cover(self):
        try:
            return mark_safe(f'<img src={self.cover.url} width="100"')
        except:
            return ""
    get_cover.short_description = "Изображение"

class IncomingMessage(models.Model):
    name = models.CharField('Name',max_length=12)
    phone = models.CharField('Phone', max_length=12, blank=False)
    email = models.EmailField('Email', max_length=200, blank=False)
    created = models.DateTimeField('Дата создания',auto_now_add=True)
    message = models.TextField('Введите сообщение',blank=False)
    answered = models.BooleanField('Отвечено', default=False)
    def __str__(self):
        d_delta = self.created + timedelta(hours=3)
        d = d_delta.strftime('%Y-%M-%d %H:%M')
        return f'{d}   {self.name}  --> {self.message[:30]}'

    class Meta:
        verbose_name = 'Входящее сообщение'
        verbose_name_plural = 'Входящие сообщения'
        ordering = ['-created']

class InformCategory(models.Model):
    title = models.CharField('Название информ. категории', max_length=50)
    description = models.TextField('Описание', default='-')
    position = models.IntegerField(default=0)
    type_inform_cat = models.CharField('Тип блока "banner/menu"', max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информ - Категория'
        verbose_name_plural = 'Информ - Категории'

class InformBlockMenuContent(models.Model):
    informCategory = models.ForeignKey(InformCategory, on_delete = models.CASCADE)
    title = models.CharField('Title', max_length=50)
    weight = models.IntegerField(default=0)
    price_float = models.FloatField(default=0.0)
    position = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.informCategory} - {self.position} - {self.title}'

    class Meta:
        ordering = ("informCategory", "title", "weight", "price_float", "position")
        verbose_name = 'Информ. Контент меню'
        verbose_name_plural = 'Информ. Контент меню'
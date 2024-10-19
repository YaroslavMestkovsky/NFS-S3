from django.db import models

class Document(models.Model):
    title = models.CharField(
        verbose_name='Наименование объекта',
        max_length=255,
    )
    file = models.FileField(
        verbose_name='Хранимый объект',
        upload_to='documents/',
    )
    uploaded_time = models.DateTimeField(
        verbose_name='Дата загрузки',
        auto_now_add=True,
    )


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.ImageField()

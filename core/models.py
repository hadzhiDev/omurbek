from django.db import models

from django_resized import ResizedImageField

from utils.models import TimeStampAbstractModel


class Photo(TimeStampAbstractModel):

    class Meta:
        verbose_name = 'изображения'
        verbose_name_plural = 'изображение'

    image = ResizedImageField('изображение', upload_to='photos/', force_format='WEBP', quality=90)

    def __str__(self):
        return f'{self.created_at}'


class Resource(TimeStampAbstractModel):

    class Meta:
        verbose_name = 'электронный ресурс'
        verbose_name_plural = 'электронные ресурсы'
        ordering = ('-created_at',)

    name = models.CharField(max_length=200, verbose_name='название')
    image = ResizedImageField('изображение', upload_to='resources/', force_format='WEBP', quality=90)
    description = models.CharField(max_length=400, verbose_name='описание')
    pdf = models.FileField(upload_to='books_pdf/', verbose_name='пдф файл')

    def __str__(self):
        return f'{self.name}'


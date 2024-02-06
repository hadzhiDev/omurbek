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

    name = models.CharField(max_length=20, verbose_name='название')
    image = ResizedImageField('изображение', upload_to='resources/', force_format='WEBP', quality=90)
    description = models.CharField(max_length=400, verbose_name='описание')
    pdf = models.FileField(upload_to='books_pdf/', verbose_name='пдф файл')

    def __str__(self):
        return f'{self.name}'


class StartEndTime(models.Model):

    class Meta:
        verbose_name = 'время начала и окончания урока'
        verbose_name_plural = 'время начала и окончания урока'

    start = models.CharField(max_length=100, verbose_name='время начала')
    end = models.CharField(max_length=100, verbose_name='время конца')

    def __str__(self):
        return f'{self.start} - {self.end}'


class Group(TimeStampAbstractModel):

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
        ordering = ('-created_at',)

    name = models.CharField(max_length=200, verbose_name='названия группа')

    def __str__(self):
        return self.name


class DailyLesson(TimeStampAbstractModel):

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    WEEK_DAYS = (
        (MONDAY, 'понедельник'),
        (TUESDAY, 'вторник'),
        (WEDNESDAY, 'среда'),
        (THURSDAY, 'четверг'),
        (FRIDAY, 'пятница'),
        (SATURDAY, 'суббота'),
        (SUNDAY, 'воскресенье')
    )

    class Meta:
        verbose_name = 'урок по расписанию'
        verbose_name_plural = 'уроки по расписанию'
        ordering = ('-created_at',)

    science = models.CharField(max_length=200, verbose_name='наук')
    day_of_week = models.CharField(choices=WEEK_DAYS, verbose_name='день недели', max_length=150)
    group = models.ForeignKey('core.Group', models.CASCADE, verbose_name='группа', related_name='lesson')
    start_end_time = models.ForeignKey('core.StartEndTime', models.CASCADE, verbose_name='время начала и окончания урока',
                                       related_name='lesson')

    def __str__(self):
        return f'{self.science} - {self.group}'


class ScientificWork(TimeStampAbstractModel):

    class Meta:
        verbose_name = 'научная работа'
        verbose_name_plural = 'научные работы'
        ordering = ('-created_at',)

    title = models.CharField(verbose_name='название', max_length=300)
    image = ResizedImageField('изображение', upload_to='resources/', force_format='WEBP', quality=90)
    description = models.CharField(max_length=400, verbose_name='описание')
    pdf = models.FileField(upload_to='scientific_work_pdf/', verbose_name='пдф файл')

    def __str__(self):
        return f'{self.title} - {self.created_at}'


class Lesson(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('-created_at',)

    name = models.CharField(verbose_name='название урока', max_length=300)


class Topic(models.Model):

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'темы'

    lesson = models.ForeignKey('core.Lesson', on_delete=models.CASCADE, verbose_name='урок', related_name='topics')
    name = models.CharField(verbose_name='название', max_length=300)
    pdf = models.FileField(upload_to='topics_pdf', verbose_name='пдф файл')

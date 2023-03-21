from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField('Название категории', max_length=256,)
    slug = models.SlugField('Слаг', max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=256)
    slug = models.SlugField('Слаг', max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class Series(models.Model):
    name = models.CharField('Серия книги')
    slug = models.SlugField('Слаг', max_length=50, unique=True)


class Book(models.Model):
    ''''''
    name = models.CharField('Название книги', max_length=256)
    author = models.ManyToManyField(
        User,
        verbose_name='Автор книги',
        on_delete=models.CASCADE,
        related_name='books',
        help_text='Автор книги',
    )
    series = models.ManyToManyField(
        Series,
        verbose_name='Серия книги',
        on_delete=models.CASCADE,
        related_name='books',
        help_text='Автор книги',
    )
    year = models.PositiveSmallIntegerField('Год выхода')
    genre = models.ManyToManyField(
        Genre,
        related_name='books',
        verbose_name='Жанры',
    )
    tags = models.ManyToManyField(
        Genre,
        related_name='books',
        verbose_name='Жанры',
    )
    description = models.TextField(
        'Описание книги',
        blank=True,
        null=True,
    )
    page_count = models.PositiveSmallIntegerField('Количество страниц')
    price = models.PositiveSmallIntegerField('Цена')
    epub = models.BooleanField()
    epub = models.BooleanField()
    epub = models.BooleanField()
    comments = models.ForeignKey()
    volume = models.PositiveSmallIntegerField('Объем')
    age_limit = models.PositiveSmallIntegerField('Возрастное ограничение')
    translator = models.ForeignKey()
    copyright_holder = models.ForeignKey()
    publisher = models.ForeignKey()
    image = models.ImageField(
        'Обложка книги',
        upload_to='books_images/',
        help_text='Загрузите фотографию блюда',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        through='TagRecipe',
        related_name='recipes',
        help_text='Выберите теги'
    )
    transfer_date = models.DateTimeField(
        'Дата публикации рецепта',
        auto_now_add=True,
    )
    writing_date = models.DateTimeField(
        'Дата публикации рецепта',
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.name

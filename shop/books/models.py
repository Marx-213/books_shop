from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=256)
    slug = models.SlugField('Слаг', max_length=50, unique=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField('Название тега', max_length=256)
    slug = models.SlugField('Слаг', max_length=50, unique=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.name


class Series(models.Model):
    name = models.CharField('Серия книги')
    slug = models.SlugField('Слаг', max_length=50, unique=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Из серии'
        verbose_name_plural = 'Из серии'


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
        verbose_name='Из серии',
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
    age_limit = models.PositiveSmallIntegerField('Возрастное ограничение')
    price = models.PositiveSmallIntegerField('Цена')
    fb2 = models.BooleanField('FB2 версия книги')
    epub = models.BooleanField('EPUB версия книги')
    pdf = models.BooleanField('PDF версия книги')
    # translator = models.ForeignKey()
    # copyright_holder = models.ForeignKey()
    # publisher = models.ForeignKey()
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
    transfer_date = models.PositiveSmallIntegerField(
        'Дата перевода',
        help_text='Введите дату перевода книги'
    )
    writing_date = models.PositiveSmallIntegerField(
        'Дата написания',
        help_text='Введите дату написания книги'
    )

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    text = models.TextField()
    review = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
    )

    def __str__(self):
        return self.text

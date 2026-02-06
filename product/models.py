from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    photo = models.ImageField(upload_to="categories/", verbose_name="Фото")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Черновик"
        PUBLISHED = "published", "Опубликовано"
        ARCHIVED = "archived", "Архив"

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name="Статус",
    )
    cover = models.ImageField(upload_to="covers/", verbose_name="Обложка")
    video = models.FileField(upload_to="videos/", verbose_name="Видео")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    is_hot = models.BooleanField(default=False, verbose_name="Горячее")
    categories = models.ManyToManyField(
        Category, related_name="products", verbose_name="Категории"
    )
    tags = models.ManyToManyField(Tag, related_name="products", verbose_name="Теги")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ["-is_hot", "-added_at"]

    def __str__(self) -> str:
        return self.title
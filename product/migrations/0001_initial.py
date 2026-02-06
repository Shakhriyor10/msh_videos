from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, unique=True, verbose_name="Название")),
                ("photo", models.ImageField(upload_to="categories/", verbose_name="Фото")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80, unique=True, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "Черновик"),
                            ("published", "Опубликовано"),
                            ("archived", "Архив"),
                        ],
                        default="draft",
                        max_length=20,
                        verbose_name="Статус",
                    ),
                ),
                ("cover", models.ImageField(upload_to="covers/", verbose_name="Обложка")),
                ("video", models.FileField(upload_to="videos/", verbose_name="Видео")),
                ("added_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")),
                ("is_hot", models.BooleanField(default=False, verbose_name="Горячее")),
                (
                    "categories",
                    models.ManyToManyField(related_name="products", to="product.Category", verbose_name="Категории"),
                ),
                ("tags", models.ManyToManyField(related_name="products", to="product.Tag", verbose_name="Теги")),
            ],
            options={
                "verbose_name": "Видео",
                "verbose_name_plural": "Видео",
                "ordering": ["-is_hot", "-added_at"],
            },
        ),
    ]

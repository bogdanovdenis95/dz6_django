# Generated by Django 5.0.6 on 2024-07-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_remove_blogpost_created_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите заголовок",
                        max_length=50,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        help_text="Введите ссылку", max_length=50, verbose_name="Ссылка"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите содержимое",
                        null=True,
                        verbose_name="Содержимое",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="Изображение (превью)",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Укажите дату создания",
                        null=True,
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False,
                        help_text="Опубликовать запись",
                        verbose_name="Опубликовано",
                    ),
                ),
                (
                    "views",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Укажите количество просмотров",
                        verbose_name="Количество просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
            },
        ),
        migrations.DeleteModel(
            name="BlogPost",
        ),
    ]

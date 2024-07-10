# Generated by Django 5.0.6 on 2024-07-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_blogpost_delete_blog_alter_category_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogpost",
            old_name="published",
            new_name="is_published",
        ),
        migrations.RemoveField(
            model_name="blogpost",
            name="preview_image",
        ),
        migrations.AddField(
            model_name="blogpost",
            name="preview",
            field=models.ImageField(blank=True, null=True, upload_to="blog_previews/"),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]

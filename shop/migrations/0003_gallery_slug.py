# Generated by Django 4.1.6 on 2023-02-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_post_comment_product_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(default=1, max_length=260, unique=True),
            preserve_default=False,
        ),
    ]

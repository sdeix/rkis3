# Generated by Django 3.2.23 on 2023-12-22 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0009_remove_comment_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='com_img',
            field=models.ImageField(blank=True, upload_to='comments/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])], verbose_name='изображение комментария'),
        ),
    ]
# Generated by Django 2.2.24 on 2021-07-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caos_news', '0004_formu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='portada',
            field=models.ImageField(default='404.jpg', upload_to='noticias'),
        ),
    ]

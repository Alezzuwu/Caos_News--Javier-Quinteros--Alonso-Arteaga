# Generated by Django 2.2.24 on 2021-07-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caos_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.CharField(default='ugu', max_length=60),
        ),
    ]
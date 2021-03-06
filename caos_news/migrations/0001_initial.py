# Generated by Django 2.2.24 on 2021-07-05 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('nombre_cat', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='periodistas',
            fields=[
                ('nombre', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='noticia',
            fields=[
                ('titulo', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('subtitulo', models.CharField(max_length=300)),
                ('fecha', models.DateField()),
                ('ubicacion', models.CharField(max_length=60)),
                ('portada', models.ImageField(null=True, upload_to='noticias')),
                ('contenido', models.TextField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caos_news.categoria')),
            ],
        ),
    ]

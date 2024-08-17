# Generated by Django 5.0.2 on 2024-03-31 08:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(max_length=250, upload_to='libro/', verbose_name='Imagen')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('autor', models.CharField(max_length=50, verbose_name='Autor')),
                ('genero', models.CharField(choices=[('Comedia', 'Comedia'), ('Acción', 'Acción'), ('Fantasía', 'Fantasía'), ('Drama', 'Drama')], max_length=50, verbose_name='Genero')),
                ('sinopsis', models.TextField(verbose_name='Sinopsis')),
                ('precio', models.PositiveIntegerField(default=250, verbose_name='Precio')),
                ('fecha_publicado', models.DateField(verbose_name='Fecha de Publicación')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.libro', verbose_name='Libro')),
            ],
            options={
                'verbose_name': 'Favorito',
                'verbose_name_plural': 'Favoritos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(choices=[(4, 4), (1, 1), (3, 3), (2, 2)], verbose_name='Cantidad')),
                ('revisado', models.BooleanField(default=False, verbose_name='Revision')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.libro', verbose_name='Libro')),
            ],
            options={
                'verbose_name': 'Carrito',
                'verbose_name_plural': 'Carritos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.carrito', verbose_name='Pedido')),
            ],
        ),
    ]
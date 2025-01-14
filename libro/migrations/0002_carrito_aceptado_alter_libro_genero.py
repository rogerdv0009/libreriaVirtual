# Generated by Django 5.0.2 on 2024-03-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='aceptado',
            field=models.BooleanField(default=False, verbose_name='Aceptacion'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.CharField(choices=[('Acción', 'Acción'), ('Drama', 'Drama'), ('Fantasía', 'Fantasía'), ('Comedia', 'Comedia')], max_length=50, verbose_name='Genero'),
        ),
    ]

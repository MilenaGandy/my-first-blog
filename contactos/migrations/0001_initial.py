# Generated by Django 4.2.11 on 2024-11-10 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=15)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefonos', to='contactos.persona')),
            ],
        ),
    ]

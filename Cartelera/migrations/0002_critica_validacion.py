# Generated by Django 4.0.4 on 2022-06-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='critica',
            name='validacion',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.2.13 on 2022-07-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='anio',
            field=models.IntegerField(null=True, verbose_name='Año'),
        ),
    ]

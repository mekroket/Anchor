# Generated by Django 3.1.7 on 2021-04-04 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0009_fiyatlarmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DerslerModel',
        ),
        migrations.AlterModelOptions(
            name='fiyatlarmodel',
            options={'verbose_name': 'Fiyatlar', 'verbose_name_plural': 'Fiyatlandırma'},
        ),
    ]

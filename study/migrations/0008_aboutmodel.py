# Generated by Django 3.1.7 on 2021-04-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0007_auto_20210402_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=20)),
                ('ünvan', models.CharField(max_length=30)),
                ('resim', models.ImageField(upload_to='hakkımda')),
                ('tanıma', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Hakkimda',
                'verbose_name_plural': 'Ceo',
                'db_table': 'Hakkimda',
            },
        ),
    ]

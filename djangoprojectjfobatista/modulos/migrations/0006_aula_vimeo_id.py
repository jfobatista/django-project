# Generated by Django 4.1.4 on 2022-12-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(default='1', max_length=32),
        ),
    ]

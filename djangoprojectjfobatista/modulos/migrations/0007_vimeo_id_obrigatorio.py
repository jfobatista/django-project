# Generated by Django 4.1.4 on 2022-12-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_aula_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(max_length=32),
        ),
    ]

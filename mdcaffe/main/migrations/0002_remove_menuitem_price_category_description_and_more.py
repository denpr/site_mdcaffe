# Generated by Django 4.0.4 on 2022-05-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='price',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='-', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.0.13 on 2019-06-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=70),
        ),
    ]
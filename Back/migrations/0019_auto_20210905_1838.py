# Generated by Django 3.2.6 on 2021-09-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0018_auto_20210905_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
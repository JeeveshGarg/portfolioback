# Generated by Django 3.2.6 on 2021-09-04 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0013_category_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='body',
        ),
    ]

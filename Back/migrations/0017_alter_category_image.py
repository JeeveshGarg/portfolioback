# Generated by Django 3.2.6 on 2021-09-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0016_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
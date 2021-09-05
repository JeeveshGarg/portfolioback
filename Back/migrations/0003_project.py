# Generated by Django 3.2.6 on 2021-09-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0002_category_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('need', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('web', models.URLField(blank=True)),
                ('github', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]

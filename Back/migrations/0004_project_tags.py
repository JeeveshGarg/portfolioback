# Generated by Django 3.2.6 on 2021-09-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='Back.Category'),
        ),
    ]

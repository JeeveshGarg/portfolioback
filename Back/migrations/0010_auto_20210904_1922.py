# Generated by Django 3.2.6 on 2021-09-04 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0009_rename_slug_sluger_sluger'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sluger',
            new_name='Value',
        ),
        migrations.RenameModel(
            old_name='Work',
            new_name='Worker',
        ),
        migrations.RenameField(
            model_name='value',
            old_name='sluger',
            new_name='name',
        ),
    ]

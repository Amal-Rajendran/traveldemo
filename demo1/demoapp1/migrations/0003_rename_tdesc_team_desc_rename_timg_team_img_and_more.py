# Generated by Django 4.2 on 2023-05-01 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp1', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='Tdesc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='Timg',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='Tname',
            new_name='name',
        ),
    ]

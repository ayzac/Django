# Generated by Django 3.2.9 on 2021-12-02 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='raza',
            new_name='empresa',
        ),
    ]

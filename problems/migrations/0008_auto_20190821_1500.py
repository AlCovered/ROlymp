# Generated by Django 2.2.4 on 2019-08-21 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0007_compiler'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Compiler',
            new_name='Code',
        ),
    ]

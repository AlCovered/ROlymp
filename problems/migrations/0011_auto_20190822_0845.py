# Generated by Django 2.2.4 on 2019-08-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0010_auto_20190821_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='condition',
            name='answer',
            field=models.TextField(default='Some'),
        ),
        migrations.AlterField(
            model_name='code',
            name='code_language',
            field=models.CharField(choices=[('24', 'Python'), ('1', 'C#'), ('19', 'Prolog')], default='Python', max_length=20),
        ),
    ]

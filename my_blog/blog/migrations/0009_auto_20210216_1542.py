# Generated by Django 3.0.5 on 2021-02-16 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210210_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='uesr_liked',
            new_name='user_liked',
        ),
    ]
# Generated by Django 4.1 on 2022-08-27 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created']},
        ),
    ]

# Generated by Django 4.0.2 on 2022-10-16 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moji_talk', '0004_roommessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roommessage',
            name='img',
        ),
    ]

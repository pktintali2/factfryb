# Generated by Django 4.0.2 on 2022-10-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moji_talk', '0002_gameroom_op1_gameroom_op2_gameroom_op3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameroom',
            name='op1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gameroom',
            name='op2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gameroom',
            name='op3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

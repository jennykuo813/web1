# Generated by Django 3.2.10 on 2022-01-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0009_auto_20211208_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='winner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

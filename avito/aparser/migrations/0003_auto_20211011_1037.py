# Generated by Django 3.0.3 on 2021-10-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0002_auto_20211009_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

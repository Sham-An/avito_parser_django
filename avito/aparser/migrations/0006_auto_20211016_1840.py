# Generated by Django 3.0.3 on 2021-10-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0005_category_jsid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='JsId',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='JsonKey'),
        ),
    ]

# Generated by Django 3.0.3 on 2021-10-16 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='JsId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='aparser.Task', verbose_name='JsonKey'),
        ),
    ]
